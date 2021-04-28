from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_uploads import UploadSet, IMAGES, configure_uploads

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
photos = UploadSet('photos', IMAGES)


def create_app(config_classname):
    """
    Initialize and configure the FLask application.
    :param config_classname: Specifies the configuration class
    :return: Return a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_classname)
    # app.static_folder = 'static'

    # Initialize the SQAlchemy object for the Flask app instance
    db.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    csrf.init_app(app)
    configure_uploads(app, photos)

    # CSRFProtect extension conflicted with Dash, line below exclude Dash from CSRFProtect
    # (Adapted from https://stackoverflow.com/questions/51585596/dash-callbacks-not-working-if-dash-app-is-created-and-called-from-flask)
    #csrf.exempt_views.add('dash.dash.dispatch')

    with app.app_context():
        # Import User
        from my_app.models import User, Profile
        db.create_all()

        # Import Dash application
        from dash_app.navigation_application import init_dashboard
        app = init_dashboard(app)

    from my_app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from my_app.community.routes import community_bp
    app.register_blueprint(community_bp)

    from my_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from my_app.forum.routes import forum_bp
    app.register_blueprint(forum_bp)

    return app
