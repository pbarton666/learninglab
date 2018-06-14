#py_screener.py

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