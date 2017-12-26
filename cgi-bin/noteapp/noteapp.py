#import virtualenv python library directory
import os
import sys
sys.path.insert(0, '/var/www/clients/client6/web28/cgi-bin/venv/lib/python2.7/site-packages')


#import installed library
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_moment import Moment
from datetime import datetime
#from flask_script import Manager
from flask_wtf import FlaskForm

#Import 3rd Party
from flask_mysqldb import MySQL
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required
from passlib.hash import sha256_crypt


#Third party imports
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

#Create application
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'This is really hard to guess string'  

# init Flask Bootstrap  
bootstrap = Bootstrap(app)  
moment = Moment(app)  
admin = Admin(app)

  
#manager = Manager(app)  

#SQLITE SQLALCHEMY
basedir = os.path.abspath(os.path.dirname(__file__))  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  
db = SQLAlchemy(app) 

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'c6noteapp' 
app.config['MYSQL_PASSWORD'] = 'imosudi@gmail.com' 
app.config['MYSQL_DB'] = 'c6noteapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MySQL  
mysql = MySQL(app)

                     
"""
python
from noteapp import db
db.create_all()

"""

from models import *


# Check user login status
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
	if 'logged_in' in session:
	    return f(*args, **kwargs)
	else:
	    flash(u'Unauthorized, Please login', 'danger')
	    return redirect(url_for('login'))
    return wrap


@app.route("/")
def home():
    pageName = "home"
    return render_template("home.html", pageName=pageName, current_time=datetime.utcnow())


@app.route("/notes/create", methods=["GET", "POST"])  
@is_logged_in
def create_note():
    pageName = "/notes/create"
    form = createNoteForm(request.form)
    if request.method == "POST" and  form.validate():
	title = form.title.data
	#notebody = form.notebody.data
	body = form.body.data
	# Creating cursor
	cur = mysql.connection.cursor()
	
	cur.execute("INSERT INTO notes(title, body) VALUES(%s,	\
	  %s)", (title, body))
	
	# Commit to Database
	mysql.connection.commit()

	#Close connection
	cur.close()

	flash(u"Note created and saved", "success")

	return redirect(url_for('create_note'))
    else:
        return render_template("create_note.html", form=form, pageName=pageName, current_time=datetime.utcnow())
 


@app.route("/notes", methods=["GET", "POST"])  
@is_logged_in
def notes():
    pageName = "/notes"
    notes = Note.query.all()
    users = RegistrationForm.query.all()
    return render_template("notes.html", users=users, notes=notes, pageName=pageName, current_time=datetime.utcnow())

@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName= "/register"
    form = registrationForm(request.form)
    #form2 = registrationForm()
    #if form.method == 'POST' and  form.validate_on_submit():
    if request.method == 'POST' and  form.validate():
	name = form.name.data
	username = form.username.data 
	email = form.email.data
	password = sha256_crypt.encrypt(str(form.password.data))
	
	# Creating cursor
	cur = mysql.connection.cursor()
	
	cur.execute("INSERT INTO users(name, username, email, password) VALUES(%s,	\
	 %s, %s,%s)", (name, username, email, password))
	
	# Commit to Database
	mysql.connection.commit()

	#Close connection
	cur.close()

	flash(u"Registration Complete, you may proceed to login", "success")

	return redirect(url_for('home'))
        """user = RegistrationForm(form.user.name, form.username.data, form.email.data, 
               form.password.data)
        db.session.add(user)
        flash('Thanks for registering')
        #return redirect(url_for('notes'))"""
    else:
	return render_template('register.html', form=form, pageName=pageName,  current_time=datetime.utcnow())


# User login
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm(request.form)
    pageName = "login"
    if request.method == 'POST': #and  form.validate():
	"""username = form.username.data 
	password = sha256_crypt.encrypt(str(form.password.data))"""
	

	# login form data
	username = request.form['username']
	password_candidate = request.form['password']

	# login cursor
	cur = mysql.connection.cursor()

	# Getting looking up for the user in the database by username
	result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

	if result > 0:
	    #Extract hash
	    data = cur.fetchone()
	    password = data['password']
	    name = data['name'] #Fetching Name Details from Database

	    #Compare passwords
	    if sha256_crypt.verify(password_candidate, password):
		#Getting seeion details
		session['logged_in'] = True		
		session['username'] = username
		session['name'] = name

		#app.logger.info('PASSWORD MATCHED')
		flash(u'Login successful', 'success')
		return redirect(url_for('dashboard'))

	    else:
		#app.logger.info('PASSWORD NOT MATCHED')
		error = 'Invalid login'
		return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow(), error=error)
	else:
	    #app.logger.info('NO USER FOUND')
	    error = 'Username not found'
	    return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow(), error=error)

    return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow())

# Application Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    pageName = "dashboard"
    	# Creating cursor
	cur = mysql.connection.cursor()
	
	result = cur.execute("SELECT * FROM notes)
	
	notes = cur.fetchall()

	if result > 0:
	    return render_template('dashboard.html', pageName=pageName, notes=notes, current_time=datetime.utcnow())
	
	else:
	    msg = "No Notes Found"
	    return render_template('dashboard.html', pageName=pageName, msg=msg current_time=datetime.utcnow())
    #return render_template('dashboard.html', pageName=pageName, current_time=datetime.utcnow())
	

# User Dashboard and Session
@app.route('/<username>/dashboard/')
@is_logged_in
def userDashboard(username):
    pageName = "userDashboard"
    return render_template('dashboard.html', pageName=pageName, current_time=datetime.utcnow())




	
# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash(u"You are now logged out", "success")
    return redirect(url_for('login')) 




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #manager.run(



