from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def index():
    f_businesses = db.execute("SELECT COUNT(*) FROM yelp WHERE categories LIKE '%Food%'").fetchone()
    print(f_businesses)
    f_rating = db.execute("SELECT AVG(stars) FROM yelp WHERE categories LIKE '%Food%'").fetchone()
    f_stars = db.execute("SELECT COUNT(*) FROM yelp WHERE stars=4 AND categories LIKE '%Food%'").fetchone()
    return render_template("metrics.html", f_businesses=f_businesses[0], f_rating='%.3f' % f_rating[0], f_stars=f_stars[0])
