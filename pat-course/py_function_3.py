#py_function_3.py
def compose(g, f):
    """Take two functions as inputs and return a
    function that's their composition"""
    def newfunc(x):
        return g(f(x))
    return newfunc

# input function
def G(n):
    return n + 2

# input function
def F(n):
    return n * 2

# compare:
H = compose(G, F) # build a 3rd function from 1 & 2
print("G(F(x)):", H(100))  # G(F(x))

# ... now with 
H = compose(F, G)
print("F(G(x)):", H(100))  # F(G(x))