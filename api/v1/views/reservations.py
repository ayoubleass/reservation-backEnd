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



