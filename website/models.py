# this file we will be storing database models

# there will be 2 database models/tables (1) users (2)notes

from . import db # importing from the current package which is website and importing db object .  we can access anything from init.py .same as from website import db
from flask_login import UserMixin # helps us log users in
from sqlalchemy.sql import func



class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)  # id will be automatically be set for you 
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())

    # all of the notes must belong to a user
    user_id = db.Column(db.Integer,db.ForeignKey("user.id")) # one to many relationship -> one user have many notes

# user model/table or schema of each user
class User(db.Model , UserMixin):
    # we will define all the columns which will be stored in this table . defining a schema
    id = db.Column(db.Integer,primary_key=True) 
    email = db.Column(db.String(150),unique=True) 
    password = db.Column(db.String(150)) 
    firstname = db.Column(db.String(150)) 

    # user shoul find all is notes
    notes = db.relationship("Note")