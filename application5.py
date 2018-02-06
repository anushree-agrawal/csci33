from flask import Flask, render_template, request

app = Flask(__name__)

names = []

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/names", methods=["GET", "POST"])
def say_hello():
    if request.method == "POST":
        name = request.form.get("name")
        names.append(name)

    return render_template("say_hello.html", names=names)