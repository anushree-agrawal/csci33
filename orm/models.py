from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cuisine = db.Column(db.String, nullable=False)
    dishes = db.relationship("Dish", backref="restaurant", lazy=True)

    def add_dish(self, name, ingredients, spicy_level):
        d = Dish(name=name, ingredients=ingredients, spicy_level=spicy_level, restaurant_id=self.id)
        db.session.add(d)
        db.session.commit()

class Dish(db.Model):
    __tablename__ = "dishes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=True)
    spicy_level = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)

    # Add another field or function here