#import virtualenv python library directory
import os
import sys
sys.path.insert(0, '/var/www/clients/client6/web28/cgi-bin/venv/lib/python2.7/site-packages')

#Import from noteapp.py
from noteapp import db


#import installed library
from flask_wtf import FlaskForm 
 
from wtforms import Form, StringField, SubmitField, IntegerField, HiddenField, validators, BooleanField, PasswordField
from wtforms.validators import Required
from wtforms.widgets import TextArea



class Note(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
 
    def __init__(self, title, body): 
        self.title = title
        self.body = body
"""
class registrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [ 
        validators.DataRequired(), 
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Complete Registeration')

class RegistrationForm(db.Model):
    __tablename__ = 'registrationforms'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    accept_tos = db.Column(db.Boolean)


    def __init__(self, username, email, password, accept_tos):
        self.username = username
        self.email = email
        self.password = password
        self.accept_tos = accept_tos
"""

class registrationForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [ 
        validators.DataRequired(), 
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    #submit = SubmitField('Complete Registeration')

class loginForm(Form):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Login Password', validators=[Required()])

class createNoteForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=12)])
    #notebody = StringField('Take a note', [validators.Length(min=2, max=250)])
    body = StringField(u'Take a note', widget=TextArea())
#CREATE TABLE notes(id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(14), notebody TEXT(270), body VARCHAR(270), create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

