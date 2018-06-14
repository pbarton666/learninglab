#py_function_2.py

def eats(*foods): # gather positional args in a tuple 
    print("foods: ", foods)  # foods is a tuple now

print("Tuple of positional arguments to eats():")

# open-ended number of positional arguments passed in...
eats("Spaghetti", "Oysters", "Chili", "Crackers", "Rice")
       
def example(*args, **kwargs): # gather keyword args in a dict
    """
    (* ) convert positionals --> tuple
    (**) convert keyword args --> dict
    """
    for arg in args:  # loop over the tuple
        print(arg, sep=", ", end="")
    print()
    for key, value in kwargs.items(): # ...now the dict
        print("Arg name:",key,"Value: ", value)

# positional + keyword (named) arguments
example( 1,2,3,4, on_vacation=True, at_work=False )

# same thing using "exploders" * and **
example( *(1,2,3,4), **dict(on_vacation=False, at_work=True) )