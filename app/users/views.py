from . import user_bp


@user_bp.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return 'Users Dashboard'