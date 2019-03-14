import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def candies():
    return render_template("index.html")

@app.route('/candy-data')
def data():
    return jsonify(
        [
            {
                "name": "Gummy bears",
                "brand": "Haribo",
                "quantity": 5
            },
            {
                "name": "Chocolate bar",
                "brand": "Hershey's",
                "quantity": 3
            },
            {
                "name": "Licorice",
                "brand": "Twizzlers",
                "quantity": 4
            },
            {
                "name": "Truffles",
                "brand": "Godiva",
                "quantity": 0
            }
        ]
        )