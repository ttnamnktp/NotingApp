from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

#initialization
def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'jhuen j'
    app.secret_key = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
     
    #import User and Note 
    from .models import User, Note 

    create_database()

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)
        print('Created Database!')