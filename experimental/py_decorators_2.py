#py_decorators_2.py

"""Demonstrates (sometimes) unwanted behavior of a decorator
     changing the original function's name"""

def decorator(func):
    "we can return a function, if we want"
    def decorated_func( *args, **kwargs):		
        print ("Originating function:  {}".format(func.__name__))
        return func( *args, **kwargs)
    return decorated_func

@decorator
def ordinary_function(x):
    print("hi, there from {}!\n".format(ordinary_function.__name__))
    return x ** 3

print("Check this out, the __name__ or ordinary function has been replaced")
print(ordinary_function.__name__ + "\n")

try:		
    print("{} -> {}".format(3, ordinary_function(3)))
except TypeError:
    print("ordinary_function exists in namespace, but is None type")
    print("is ordinary_function None?   {}".format(ordinary_function is None))


