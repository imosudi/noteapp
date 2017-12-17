#!/usr/bin/python

from wsgiref.handlers import CGIHandler
#from myapp import app
from noteapp.app import app


CGIHandler().run(app)
