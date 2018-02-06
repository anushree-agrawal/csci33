from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/anushree")
def anushree():
    return "Hello, Anushree!"
