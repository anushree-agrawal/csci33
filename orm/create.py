import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()
    
    mcdonalds = Restaurant(name="McDonalds", cuisine="fast-food")
    db.session.add(mcdonalds)
    db.session.commit()
    mcdonalds.add_dish(name="Big Mac", ingredients="fake beef, cheese", spicy_level=0)
    db.session.commit()

    # Add more dishes

if __name__ == "__main__":
    with app.app_context():
        main()