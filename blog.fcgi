#!/usr/bin/env python
from flup.server.fcgi import WSGIServer
from blog import app
if __name__ == "__main__":
	WSGIServer(app).run()