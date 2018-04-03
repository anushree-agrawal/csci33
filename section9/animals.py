class Dog:
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed
        self.barks = 0
        self.hungry = False
        self.size = 5

    def bark(self):
        self.barks += 1

    def feed(self):
        if self.hungry:
            self.hungry = False
        else:
            raise ValueError("Dog is already fed")

    def set_hungry(self):
        self.hungry = True

    def grow(self):
        self.size += 1

class DogHouse:
    def __init__(self, color, capacity):
        self.color = color
        self.capacity = capacity
        self.dogs = []

    def add_dog(self, dog):
        if self.capacity <= len(self.dogs):
            raise ValueError("No room left in dog house")
        else:
            self.dogs.append(dog)

    def remove_dog(self):
        if self.dogs:
            return self.dogs.pop()
        else:
            raise ValueError("No dogs to remove")
