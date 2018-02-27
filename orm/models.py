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

    def remove_dish(self, id):
        db.session.delete(Dish.query.get(id))
        db.session.commit()

    def __repr__(self):
        dishes_str = []
        for dish in self.dishes:
            dishes_str.append(dish.__repr__())
        return "%s serves %s and has the following dishes: %s " % (self.name, self.cuisine, "\n".join(dishes_str))

class Dish(db.Model):
    __tablename__ = "dishes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=True)
    spicy_level = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)

    def __repr__(self):
        return "%s contains %s and has a spicy level of %d" % (self.name, self.ingredients, self.spicy_level)
        # Add another field or function here
