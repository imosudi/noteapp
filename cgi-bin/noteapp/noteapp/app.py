#import virtualenv python library directory
import os
import sys
sys.path.insert(0, '/var/www/clients/client6/web28/cgi-bin/venv/lib/python2.7/site-packages')


#import installed library
from flask import Flask, render_template, request, url_for




#Create application
app = Flask(__name__)
#bootstrap = Bootstrap(app)
#moment = Moment(app)



@app.route('/')
def home():
    return 'Welcome to noteapp'













if __name__ == '__main__':
    app.run()
