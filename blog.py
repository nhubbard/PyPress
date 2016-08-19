from settings import *
import sys
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
app.config["FLATPAGES_MARKDOWN_EXTENSIONS"] = []
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
@app.errorhandler(404)
def error404(e):
	return render_template("error.html", title=TITLE, description=DESCRIPTION, code="404", explain="Page Not Found"), 404
@app.errorhandler(403)
def error403(e):
	return render_template("error.html", title=TITLE, description=DESCRIPTION, code="403", explain="Forbidden"), 403
@app.errorhandler(410)
def error410(e):
	return render_template("error.html", title=TITLE, description=DESCRIPTION, code="410", explain="Permanantly Deleted"), 410
@app.errorhandler(500)
def error500(e):
	return render_template("error.html", title=TITLE, description=DESCRIPTION, code="500", explain="Internal Server Error"), 500
if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	if len(sys.argv) > 1 and sys.argv[1] == "run":
		print(Fore.GREEN + "Your server is running with an adhoc SSL certificate on port 5000.")
		app.run(host="0.0.0.0", debug=DEBUG, ssl_context="adhoc")