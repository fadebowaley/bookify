from flask import Blueprint
bp = Blueprint('services', __name__, template_folder='templates',
               static_folder='static')

from app.services import views