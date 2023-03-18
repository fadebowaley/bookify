from app.views.appointments import *
from app.views.locations import *
from app.views.providers import *
from app.views.services import *
from app.views.auth import *
from app.views.index import *
from flask import Blueprint

bp = Blueprint('main', __name__)
