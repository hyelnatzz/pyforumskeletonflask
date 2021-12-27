from flask import Blueprint


main_bp = Blueprint('main_bp', __name__, url_prefix='/')



@main_bp.route('/', methods=['GET'])
def index():
    return 'Homepage View'
