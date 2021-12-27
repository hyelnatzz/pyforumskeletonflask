from . import auth_bp


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return 'Register View'


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'Login View'


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'Logout View'


@auth_bp.route('/sanction', methods=['GET', 'POST'])
def sanction():
    return 'sanction View'
