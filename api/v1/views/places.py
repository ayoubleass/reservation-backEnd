
#!/usr/bin/python3
"""This module contains the endpoints for place resources."""

from helpers.helpers import *
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User
from models.role import Role
from models.image import Image
from models.place import Place
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity
from flask import send_from_directory
from flask import url_for

@app_views.route('/images/<path:image_filename>')
def get_image(image_filename):
    """Serve images from the 'storage' directory"""
    return send_from_directory(ROOT_DIR + "/storage", image_filename)


@app_views.route('/cities/<city_id>/places')
def show_places_by_city(city_id):
    """Show places in a city"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    response = {}
    images = []
    for place in city.places:
        image_urls = [" http://127.0.0.1:5000" +url_for('app_views.get_image', image_filename=image.url.split('\\')[-1]) for image in place.images]
        place_data =  place.to_dict()
        place_data['images'] = image_urls
        response.append(place_data)
    return jsonify(response),  200
        



@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def show_place(place_id):
    """show a place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404, description="Place not found")
    response = place.to_dict()
    response['images'] = [" http://127.0.0.1:5000" + 
                          url_for('app_views.get_image', image_filename=image.url.split('\\')[-1]) for image in place.images]
    #response['amenities'] = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(response), 200


@app_views.route('/users/<user_id>/places', methods=['GET'], strict_slashes=False)
def show_user_places(user_id):
    """show a place"""
    user = storage.get("User", user_id);
    if user is None:
        abort(404, description="User not found")
    response = []
    images = []
    for place in user.places:
        image_urls = [" http://127.0.0.1:5000" +url_for('app_views.get_image', image_filename=image.url.split('\\')[-1]) for image in place.images]
        place_data =  place.to_dict()
        place_data['images'] = image_urls
        response.append(place_data)
    return jsonify(response)





@app_views.route(
    '/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
@jwt_required()
def create_place(city_id):
    """Create a place"""
    city = storage.get("City", city_id)
    response = {}
    if city is None:
        abort(404, description="City not found")
    content_type = request.headers.get('Content-Type').split(";")[0]
    request_body = request.form.to_dict()
    user = storage.get("User", request_body.get("user_id"))
    if user is None:
        abort(404, description="User not found")
    role = storage.getSession().query(Role).filter_by(name="host").first()
    if role not in user.roles:
        user.roles.append(role)
    category = storage.get("Category", request_body.get("category_id"))
    if category is None:
        abort(404, description="Category not found") 
    new_place = Place(name= request_body.get('name'),
                      description= request_body.get('description'),
                      max_guest= request_body.get('max_guest'),
                      number_rooms = request_body.get('number_rooms'),
                      number_bathrooms = request_body.get('number_bathrooms'),
                      address = request_body.get('address'),
                      price_by_night = request_body.get('price_by_night'),
                      category_id = request_body.get('category_id'),
                      city_id = city_id,
                      user_id = request_body.get("user_id"))
    amenities_ids = request_body.get("amenities[]")
    amenities = None
    if ',' in amenities_ids:
        amenities = [storage.get('Amenity', amenity_id) for amenity_id in amenities_ids.split(',')]
    else:
        amenities = storage.get('Amenity', amenities_ids)
    storage.new(new_place).save()
    error_message = upload_images(request, new_place.id)
    if isinstance(error_message,str):
        abort(404, description=error_message)
    if isinstance(amenities, list):
        for amenity in amenities:
            new_place.amenities.append(amenity)
    else:
            new_place.amenities.append(amenities)
    storage.save()
    response = new_place.to_dict()
    return jsonify(new_place.to_dict()), 201





@app_views.route(
    '/places/<place_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_place(place_id):
    place = storage.get("Place",place_id)
    if place is None:
        abort(404, description="Place not found")
    storage.delete(place)
    storage.save()
    return jsonify({}), 200
    

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_place(place_id):
    """Update a place"""
    content_type = request.headers.get('Content-Type').split(";")[0]
    request_body = request.form.to_dict()
    user = storage.get("User", request_body.get("user_id"))
    if user is None:
        abort(404, description= "User is not found")
        role = storage.getSession().query(Role).filter_by(name="host").first()
    if role not in user.roles:
        user.roles.append(role)
    category = storage.get("Category", request_body.get("category_id"))
    if category is None:
        abort(404, description="Category not found") 
    place = storage.get('Place', place_id)
    if place is None:
        abort(404,description="place not found")
    for  attr in dir(place):
        if not attr.startswith('__') and  not attr.startswith('_') :
            setattr(place, request_body.get(attr))
    storage.save()
    return jsonify(place.to_dict()), 201





@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search_for_places():
    # Get JSON request body
    request_body = request.get_json()

    # Extract parameters from request body
    country_id = request_body.get('country_id')
    arrival_date = request_body.get('arrival')
    departure_date = request_body.get('departure')
    amenities = request_body.get('amenities')
    price_by_night = request_body.get('price_by_night')

    if not country_id or not arrival_date or not departure_date:
        return jsonify({"error": "Missing required parameters"}), 400

    cities = [city for city in storage.all("City").values()
              if city.country_id == country_id]
    places = []
    for city in cities:
        for place in city.places:
            image_urls = ["http://127.0.0.1:5000" + url_for('app_views.get_image', 
                            image_filename=image.url.split('\\')[-1]) for image in place.images]
            place_data = place.to_dict()
            place_data['images'] = image_urls

            if price_by_night and place_data.get('price_by_night') != price_by_night:
                continue  

            if amenities and not all(amenity in place_data.get('amenities', []) for amenity in amenities):
                continue  
            places.append(place_data)

    return jsonify(places), 200  
