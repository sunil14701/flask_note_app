# will make this website folder a python package . means we can import website folder and whatever is inside of __init__.py file will run automatically once we import website folder

# setting up/creating the flask application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # for database
from os import path
from flask_login import LoginManager


# defining new database and initilizing it
db = SQLAlchemy() # db is database object . db will be used to add something to database , create a new user
DB_NAME = "database.db" # database name


def create_app():
    app = Flask(__name__) # initiallsing our app
    app.config["SECRET_KEY"] = "ksdlfdsfldslfds" # in production we never share our secret key # secret key is going to encrypt or secure the cookies and session data related to our website
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"# mysql database is stored in this location . it will store the database in the website folder where there is init.py file is
    db.init_app(app)# initilizing our database by giveing our flask app


   

    # now we have to register those blueprint of website url in our __int__.py
    from .views import views # from views folder import views blueprint variable
    from .auth import auth

    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")

    from .models import User,Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app;

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app = app)
        print("database  created!")

