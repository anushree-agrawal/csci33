class Restaurant:

    '''
    class Restaurant has id, name, cuisine, and list of dishes
    '''

    count = 1
    
    def __init__(self, name, cuisine):
        # fill in here

    def add_dish(self, new_dish):
        # fill in here
 
    def __str__(self):
        # fill in here

class Dish:
    '''
    class Dish has name, list of ingredients, and a spicy level
    '''
    def __init__(self, name, ingredients, spicy_level):
        # fill in here
    
    def __str__(self):
        # fill in here
    
    def change_spicy_level(self, new_level):
        # fill in here

def main():
    mcdonalds = Restaurant("McDonalds", "fast-food")
    mcdonalds.add_dish(Dish("Big Mac", ["fake beef", "cheese"], 0))
    print(mcdonalds.__str__())
    print(mcdonalds)

