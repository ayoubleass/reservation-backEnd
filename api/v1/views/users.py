#!/usr/bin/python3
"""This module contains the endpoints for user resources."""

from helpers.helpers import *
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User
from models.role import Role
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity
#from sqlalchemy.dialects.mysql import insert


@app_views.route("/users", strict_slashes=False)
@jwt_required()
def show_users():
    """Show all the users """
    return jsonify([user.to_dict() 
                    for user in storage.all("User").values()])




@app_views.route("/users/<user_id>", strict_slashes=False)
def show_user(user_id):
    user = storage.get("User", user_id);
    if not user:
        abort(404, description="User not found")
    return jsonify(storage.get("User", user_id).to_dict()), 200





@app_views.route('/users', methods=['POST'],strict_slashes=False)
def create_user():
    request_body = request.get_json()
    response = {} 
    if not request.is_json:
        abort(400)
    if request_body.get('email'):
        email = request_body['email']
        if not unique("User","email",email):
            abort(400,description = "email alredy exists")
    new_user = User( email      = request_body.get('email'),
                    first_name  = request_body.get('first_name'),
                    last_name   = request_body.get('last_name'),
                    password    = generate_password_hash(request_body.get('password')),
                    phone_number= request_body.get('phone_number'))
    role = request_body.get("role", "travler")
    if role not in ["travler", "hote", "admin"]:
            abort(400, description="role  {} not allowed ".format(role))
    existing_role = storage.getSession().query(Role).filter_by(name=role).first()
    if existing_role is None:
        existing_role = Role(name=role)
        storage.new(existing_role).save()
    new_user.roles.append(existing_role)
    storage.new(new_user).save()
    response = storage.get('User', new_user.id).to_dict()
    response ["roles"] = [role.name for role in new_user.roles]
    response['token'] = create_access_token(identity=new_user.get('first_name'))
    return jsonify(response), 201
        
    





@app_views.route("/users/<user_id>", methods=["PUT"],strict_slashes=False)
@jwt_required()
def update_user(user_id):
    request_body = request.get_json()
    response = {}
    if not request.is_json:
        abort(400)
    user = storage.get("User", user_id);
    if not user:
        abort(404, description="User not found")
    if  not unique("User","email",request_body.get('email')) and request_body.get('email'):
        del request_body["email"]
           
    for key, value in request_body.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(user, key, value)
            if key == "Password":
                setattr(user, key, generate_password_hash(value))
    storage.merge(user).save()
    
    return jsonify(storage.get("User", user_id).to_dict()), 200



@app_views.route("/users/<user_id>", methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_user(user_id):
    """Delete a user """
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200



@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    if not request.is_json:
        abort(400, description="Request must be JSON")
    request_body = request.get_json()
    email = request_body.get('email')
    password = request_body.get('password')
    if not email or not password:
        abort(400, description="Email and password are required")
    user = storage.getSession().query(User).filter_by(email=email).first()
    if user is None:
        abort(400, description="Invalid email or password")
    if not check_password_hash(user.password, password):
        abort(400, description="Invalid email or password")
    response = user.to_dict()
    response['token'] = create_access_token(identity=user.get("first_name"))
    response ["roles"] = [role.name for role in user.roles]
    return jsonify(response), 200
    




        
    


