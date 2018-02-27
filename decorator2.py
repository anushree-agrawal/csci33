def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")

# print(my_decorator(just_some_function()))

# just_some_function = my_decorator(just_some_function)
# my_decorator(just_some_function)()

# just_some_function()

from decorator07 import my_decorator

# try_function = my_decorator(try_function)
@my_decorator
def try_function():
    print("Hello!")

try_function()
