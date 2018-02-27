def foo(bar):
    return bar+1

# print(foo(2))
# print(foo)
# print(type(foo))

# takes in a function and call it with those arguments
def call_foo(fun, arg):
    return fun(arg)

print(call_foo(foo, 3))

#
def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())

parent()
first_child()
