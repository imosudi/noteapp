#import virtualenv python library directory
import os
import sys
sys.path.insert(0, '/var/www/clients/client6/web28/cgi-bin/venv/lib/python2.7/site-packages')


#import installed library
from flask import Flask, render_template, redirect, request, session
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_moment import Moment
from datetime import datetime
#from flask_script import Manager
from flask_wtf import FlaskForm

from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required



#Third party imports
from flask_sqlalchemy import SQLAlchemy


#Create application
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'This is really hard to guess string'  
  
bootstrap = Bootstrap(app)  
moment = Moment(app)  
admin = Admin(app)  
#manager = Manager(app)  

#SQLITE SQLALCHEMY
basedir = os.path.abspath(os.path.dirname(__file__))  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  
db = SQLAlchemy(app)  
                     
"""
python
from main import db
db.create_all()

"""

from models import *



@app.route("/")
def home():
    pageName = "home"
    return render_template("home.html", pageName=pageName, current_time=datetime.utcnow())


@app.route("/notes/create", methods=["GET", "POST"])  
def create_note():
    pageName = "/notes/create"
    if request.method == "GET":
        return render_template("create_note.html", pageName=pageName, current_time=datetime.utcnow())
    else:
        title = request.form["title"]
        body = request.form["body"]  
        note = Note(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        return redirect("/notes/create", form=form, current_time=datetime.utcnow())

@app.route("/notes", methods=["GET", "POST"])  
def notes():
    pageName = "/notes"
    notes = Note.query.all()
    return render_template("notes.html", notes=notes, pageName=pageName, current_time=datetime.utcnow())

@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName= "/register"
    form = registrationForm()
    form2 = registrationForm()
    return render_template('register.html', form=form, form2=form2, pageName=pageName,  current_time=datetime.utcnow())



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #manager.run(



