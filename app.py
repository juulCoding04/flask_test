from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

# hello world function is visible from home page = 127.0.0.1/5000
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# hello function is visible from 127.0.0.1/5000/<name>
@app.route("/<name>")
def name(name):
    return f"Hello, {escape(name)}!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', person=name)