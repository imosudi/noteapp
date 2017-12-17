#!/usr/bin/python

from wsgiref.handlers import CGIHandler
#from myapp import app
from noteapp import *


CGIHandler().run(app)
