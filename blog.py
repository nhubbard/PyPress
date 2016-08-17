from settings import *
import sys, urllib, hashlib
if SSL == True:
	import ssl
	ssl = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
	ssl.load_cert_chain(SSL_CERT, SSL_KEY)
from flask import Flask, request, render_template, send_from_directory
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from flask_gravatar import Gravatar
from colorama import init as color_init
from colorama import Fore, Back, Style
color_init()
app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
gravatar = Gravatar(app, size=40, rating="g", default="https://s3.postimg.org/du6g05qbn/default_user.png", use_ssl=True)
app.config.from_object(__name__)
@app.route("/")
def posts():
	posts = [p for p in flatpages if p.path.startswith("posts")]
	posts.sort(key=lambda item:item["date"], reverse=False)
	return render_template("posts.html", title=TITLE, description=DESCRIPTION, posts=posts)
@app.route("/posts/<name>/")
def post(name):
	path = "{}/{}".format("posts", name)
	post = flatpages.get_or_404(path)
	return render_template("post.html", title=TITLE, description=DESCRIPTION, post=post)
@app.route("/assets/<path:path>")
def assets(path):
	return send_from_directory("public", path)
@app.route("/<name>")
def other(name):
	path = "{}/{}".format("extras", name)
	post = flatpages.get_or_404(path)
	return render_template("post.html", title=TITLE, description=DESCRIPTION, post=post)
if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		if SSL == True:
			app.run(host="0.0.0.0", debug=DEBUG, ssl_context=ssl)
			print(Fore.GREEN + "Your server is running with SSL on port 5000.")
		else:
			app.run(host="0.0.0.0", debug=DEBUG)
			print(Fore.YELLOW + "Your server is running without SSL on port 5000.")