#py_function_4.py

def addLetter(letters): # <-- pass in a string
    """
    A function factory builds and returns function objects. 
    L is a function that will add whatever letters are passed 
    in to be the ending letters.
    """

    def L(s):
        return s + letters
    return L

#these are functions (versions of the inner function L() returned from addLetters()    
add_s  = addLetter("s")
add_ed = addLetter("ed")

print(add_ed)

#and we can execute these functions like any others
print(add_s('Unhinged rant'))
print(add_ed('In an unhinged fashion rant'))
