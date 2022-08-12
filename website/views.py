# this is going to store main views or url end points for the frontend of our website
# we will store the standart routed for our website  , where users can actually go to for eg hame page 

from flask import Blueprint # seperation of various URL is done . views can be defined in multiple files
from flask import render_template, url_for,request,flash,jsonify
from flask_login import  login_required,current_user
from .models import Note
from . import db
import json


# this file is a blueprint of our application , means this file contain routes/endpoints/URL's in it

views = Blueprint("views",__name__) # blueprint setup for flask app


# defining views
@views.route('/') #whenever we go to slash we go to the this below function
@views.route("/home",methods=["GET","POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if len(note)<1:
            flash("Note can not be Empty",category="error")
        else:
            new_note = Note(data =note , user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added" ,category="success")

    return render_template("home.html",user=current_user)

@views.route("/delete-note",methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

