from animals import *
import unittest

class TestDog(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.a = Dog(color="black", breed="corgi")

    def test_bark(self):
        self.a.bark()
        self.assertEqual(self.a.barks, 1)

    def test_multiple_barks(self):
        self.a.bark()
        self.a.bark()
        self.assertEqual(self.a.barks, 2)

    def test_feeding_full(self):
        self.assertRaises(ValueError, self.a.feed)

    def test_setting_hungry(self):
        self.a.set_hungry()
        self.assertTrue(self.a.hungry)

    def test_feeding_hungry(self):
        self.a.set_hungry()
        self.assertTrue(self.a.hungry)

        self.a.feed()
        self.assertFalse(self.a.hungry)

    def test_grow(self):
        self.a.grow()
        self.assertEqual(self.a.size, 6)

class TestDogHouse(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.a = Dog(color="black", breed="corgi")
        self.b = Dog(color="orange", breed="poodle")
        self.c = Dog(color="green", breed="lab")
        self.d = DogHouse(color="red", capacity=2)

    def test_adding_not_full(self):
        self.d.add_dog(self.a)
        self.assertEqual(len(self.d.dogs), 1)

    def test_adding_multiple_not_full(self):
        self.d.add_dog(self.a)
        self.d.add_dog(self.b)
        self.assertEqual(len(self.d.dogs), 2)

    def test_adding_one_full(self):
        self.d.add_dog(self.a)
        self.d.add_dog(self.b)
        with self.assertRaises(ValueError):
            self.d.add_dog(self.c)

    def test_remove_one_present(self):
        self.d.add_dog(self.a)
        self.assertEqual(len(self.d.dogs), 1)
        self.d.remove_dog()
        self.assertEqual(len(self.d.dogs), 0)

    def test_remove_one_absent(self):
        self.assertRaises(ValueError, self.d.remove_dog)

if __name__ == '__main__':
    unittest.main()