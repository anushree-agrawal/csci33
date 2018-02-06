from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/<string:name>")
def say_hello(name):
	return render_template("index.html", name=name)