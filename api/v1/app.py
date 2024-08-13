#!/usr/bin/python3
"""This is the entry to the api"""


from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from helpers.helpers import *
#from flask_api_key import APIKeyManager
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=5)
jwt = JWTManager(app)
UPLOAD_FOLDER =  os.path.join(ROOT_DIR, 'storage')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.errorhandler(400)
def bad_request(e):
    """Handle bas request"""
    return jsonify(error=e.description), 400


@app.teardown_appcontext
def close_storage(exception):
    """Close the storage"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors that returns a
    JSON-formatted 404 status code response"""
    return jsonify(error=error.description), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000, threaded=True, debug=True)