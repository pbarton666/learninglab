#py_decorators.py
from functools import wraps

def big_fish(input_function):
    def inner_function(input_function):
        @wraps
        def wrapped(*args, **kwargs):
            print("{} here".format(__name__))
            print ("Yum.  I just ate a {}".format(input_function()))
            return inner_function()

@big_fish			  
def little_fish():
    user_input=input("Please type something:  ") 
    return user_input

little_fish()
	
