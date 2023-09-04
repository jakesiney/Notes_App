from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "notes_database.db"


def create_app():
    # __name__ is the name of the current file. Flask uses this to know where to look for templates and static files.
    app = Flask(__name__)
    # SECRET_KEY is used to encrypt and decrypt the data that is transferred between the client and the server. It is also used to create the CSRF token.
    app.config['SECRET_KEY'] = 'secret-key-123'
    # SQLALCHEMY_DATABASE_URI is the path to where the database file will be saved.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # Initialize the database with the Flask app.

    from .views import views
    from .auth import auth

    # url_prefix is used to add a prefix to all the routes in the blueprint.
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    # app_context() is used to make sure that the app is in the correct state.
    with app.app_context():
        db.create_all()

    return app
