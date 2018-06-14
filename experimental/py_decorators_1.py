#py_decorators_1.py

"Demonstrates basic use of a decorator, and the equivalent code without."

use_decorator = True   #a pragma to allow it to run either way

if not use_decorator:
    #without a decorator, you can simpley pass one function to another

    def non_decorator(func):
        print("hi, there from non_decorator()!\n")
        print("originating function is:  {}".format(func.__name__))
        func()

    def ordinary_function():	
        print("hi, there from ordinary_function()!\n")

    non_decorator(ordinary_function)

else:
    #when decorator used, decorator called when function is defined
    def decorator(func):
        "A decorator is any callable object.  It *replaces* ordinary_function()."
        print("Hi there from decorator()!")
        print("originating function is:  {}".format(func.__name__))
        func()

    @decorator
    def ordinary_function():
        print("hi, there from ordinary_function()!\n")

if use_decorator:
    try:		
        ordinary_function()
    except TypeError:
        print("ordinary_function exists in namespace, but is None type")
        print("is ordinary_function None?   {}".format(ordinary_function is None))


