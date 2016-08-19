PyPress (1.x)
=============

Welcome! PyPress is the simple, unopinionated, lightweight blog system built on Flask and FlatPages. It currently is tested with Python 2.7.12.

We currently support static mode (using Flask-Freezer), adhoc script mode, CGI and FastCGI.

To use PyPress:

1. Clone the repository and enter it.
2. Run (with sudo if you need it): `(sudo -H) pip install -r requirements.txt`
3. Run: `python blog.py run`.

You can use the provided `blog.cgi` and `blog.fcgi` files to run it in CGI or FastCGI behind a server such as Apache2, Nginx, Lighttpd, or Rwasa.

Place your blog posts in the `content/posts` folder, using the `content/posts/welcome.md` as a starter template for both metadata and style.

To build a static site, replace `python blog.py run` with `python blog.py build`.