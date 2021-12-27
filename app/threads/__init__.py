from flask import Blueprint


threads_bp = Blueprint('threads_bp', __name__, url_prefix='/threads')


from .views import *