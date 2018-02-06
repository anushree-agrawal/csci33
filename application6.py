from flask import Flask, render_template, request

app = Flask(__name__)

names = []

@app.route("/")
def index():
    return render_template("index_l.html")

@app.route("/names", methods=["GET", "POST"])
def say_hello():
    if request.method == "POST":
        name = request.form.get("name")
        names.append(name)

    return render_template("say_hello_l.html", names=names)