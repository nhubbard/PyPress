#!/usr/bin/env python
from wsgiref.handlers import CGIHandler
from blog import app
CGIHandler().run(app)