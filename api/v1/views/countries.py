#!/usr/bin/python3
"""This module contains the State end points """


from api.v1.views import app_views
from flask import jsonify
from models import storage
import json
from flask import request
from models.country import Country
from flask import abort


@app_views.route("/countries/", strict_slashes=False)
def show_states():
    """Return all states objets"""
    
    countries = storage.all("Country").values()
    return jsonify([country.to_dict() for country in countries])
    


@app_views.route("/countries/<country_id>", strict_slashes=False)
def show_state(country_id):
    """Return a specifique State object or raise a 404 error"""
    country = storage.get("Country", country_id)
    if country is None:
        abort(404)
    return jsonify(country.to_dict())


@app_views.route(
    "/countries/<country_id>",
    methods=['DELETE'],
    strict_slashes=False)
def delete_state(country_id):
    """Delete a specifique State object or raise a 404 error"""
    country = storage.get("Country", country_id)
    if state is None:
        abort(404)
    storage.delete(country)
    storage.save()
    return jsonify({}), 200


@app_views.route("/Country", methods=['POST'], strict_slashes=False)
def create_state():
    """Create a new state """
    if not request.is_json:
        abort(400)
    request_body = request.get_json()
    if "name" not in request_body:
        return jsonify(error="Missing name"), 400
    country = Country(name=request_body.get("name"))
    country.save()
    return jsonify(country.to_dict()), 201


@app_views.route("/country/<country_id>", methods=['PUT'], strict_slashes=False)
def update_state(country_id):
    """Return a specifique State object or raise a 404 error"""
    country = storage.get("Country", country_id)
    if country is None:
        abort(404)
    if not request.is_json:
        abort(400)
    request_body = request.get_json()
    for key, value in request_body.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(country, key, value)
    storage.save()
    return jsonify(country.to_dict()), 200