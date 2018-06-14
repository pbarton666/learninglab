#solution_python1_chapter07_screener.py
"""A solution to Chapter 7.  Note that there is deliberate redundency is this script - 
       it shows different approaches to evaluating data now, and an opportunity to
       apply iterative revision / testing as an exercise for the unittest chapter."""


class IntException(Exception):
    def __init__(self, problem_child):
        if isinstance(problem_child, int):
            print("Darn it!  Another integer!")

class ComplexException(Exception):
    def __init__(self, problem_child):
        if isinstance(problem_child, complex):
            print("Gracious sir, there seems to be (ahem) complexity here.")	

def screener(user_inp=None):
    """A function to square only floating points.
       Returns custom exceptions if an int or complex is encountered."""

    #make sure something was input
    if not user_inp:
        print("Ummm...did you type in ANYTHING?")
        return

    #If it *might* be a float (has a ".") try to type-cast it and return
    if "." in user_inp:
        try:
            inp_as_float=float(user_inp)
            if isinstance(inp_as_float, float):
                square = inp_as_float**2
                print( "You gave me {}.  Its square is: {}".format(user_inp, square))
        except:
            return

    try:  #see if we need to return the ComplexException
        if "(" in user_inp:  #it might be complex if it has a (		
            inp_as_complex=complex(user_inp)
            if isinstance(inp_as_complex, complex):
                raise ComplexException(inp_as_complex)
    except:  #it's not complex
        pass

    try:
        #we already tried to type-cast to float, let's try casting to int
        inp_as_integer=int(user_inp)
        if isinstance(inp_as_integer, int):
            raise IntException(inp_as_integer)
    except:  
        pass

    #if we're here, the function hasn't returned anything or raised an exception
    print("Done processing  {} ".format(user_inp))

def call_screener(test_input=None):
    "utility function to operate in test or production mode"
    if not test_input:  #production mode
        user_inp=input("Please type in a floating-point number:  ")
        screener(user_inp)
    else:
        for inp in test_input:
            print("Processing: {}".format(inp))
            screener(inp)

test_input = ["1.0", "(2+3j)", "1", "1.0", "abc"]
call_screener()
call_screener(test_input=test_input)