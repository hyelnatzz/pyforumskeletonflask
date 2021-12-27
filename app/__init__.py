from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    admin = Admin(app)


    from .auth import auth_bp
    from .users import user_bp
    from .threads import threads_bp
    from .main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(threads_bp)
    app.register_blueprint(main_bp)
    

    with app.app_context():
        
        from .models import User
        admin.add_view(ModelView(User, db.session))
        
        db.create_all()
        return app
