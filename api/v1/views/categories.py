#!/usr/bin/python3
"""This Module has all the City end points """


from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
import json
from flask import request
from models.category import Category
from flask import url_for



@app_views.route('/categories')
def show_categories():
    categories = storage.all("Category").values()
    return jsonify([category.to_dict() for category in categories]), 200


@app_views.route('/categories/<category_id>')
def show_category(category_id):
    category = storage.get("Category", category_id)
    if category is None:
        abort(404, description="Category not found")
    return jsonify(category.to_dict()), 200



@app_views.route('/category/<category_id>/places', methods=['GET'], strict_slashes=False)
def show_places_by_categories(category_id):
    category = storage.get('Category', category_id)
    if category is None:
        abort(404, description='Category not found')
    response = []
    images = []
    for place in category.places:
        if place.is_valid:
            image_urls = [" http://127.0.0.1:5000" +url_for('app_views.get_image', image_filename=image.url.split('\\')[-1]) for image in place.images]
            place_data =  place.to_dict()
            place_data['images'] = image_urls
            response.append(place_data)
        image_urls = [" http://127.0.0.1:5000" +url_for('app_views.get_image', image_filename=image.url.split('\\')[-1]) for image in place.images]
        place_data =  place.to_dict()
        place_data['images'] = image_urls
        response.append(place_data)
    return jsonify(response), 200




@app_views.route('/categories/<category_id>/places')
def show_places_by_category(category_id):
    category = storage.get("Category",category_id)
    if category is None:
        abort(404, description="Category not found")
    return jsonify([place.to_dict() for place in category.places]), 200
    



