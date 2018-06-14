#solution_python2_chapter02_tested.py

class NoneTypeError(Exception):
    pass

class WrongDataTypeError(Exception):
    pass

def add_numbers(first, second):
    "adds two numbers"
    #check if either is None
    if isinstance(first, type(None)) or isinstance(second, type(None)):
        raise NoneTypeError
    #see if the interpreter raises a TypeError
    try:
        answer=first+second
    except TypeError:
        #intercept the TypeError and return the custom one
        raise WrongDataTypeError
        
    #if we've made it this far, we should be golden so return 
    return answer

if __name__=='__main__':
    #stash local testing here
    add_numbers(None, None)