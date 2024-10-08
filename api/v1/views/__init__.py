from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.cities import *
from api.v1.views.countries import *
from api.v1.views.categories import *
from api.v1.views.amenities import *
