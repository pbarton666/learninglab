# py_compose.py
"""
Using the Compose class as a class decorator, we turn
ordinary functions into Compose type objects. 

These overload the multiplication and powering operators 
to implement composition of functions.

E.g.

(F * G)(x) == F(G(x))

once functions F, G have been turned into Compose instances.
"""

class Compose:
    """
    make function composible with multiply
    also make self powerable e.g. f ** 3 == f * f * f
    """
  
    def __init__(self, f):
        self.func = f

    def __mul__(self, other):
        return Compose(lambda x: self(other(x)))

    def __pow__(self, n):
        if n == 0:
            return Compose(lambda x: x) # identity function
        if n == 1:
            return self
        if n > 1:
            me = self
          
        for _ in range(n-1):
            me *= self # me times me times me...
        return me
    
    def __call__(self, x): # callable instances
        return self.func(x)

def main():        
    # First lets do composition using a lambda expression    
    # take any two functions as args and return their composition
    compose = lambda f, g: (lambda x: f(g(x)))
    
    # So now if I go...
    def S(x): return x * x
    def R(x): return x + (1/2)*x
    
    # we can then build new functions:
    print("="*10)
    H = compose(S, R)  # returns lambda x: S(R(x))
    J = compose(R, S)  # returns lambda x: R(S(x))
    
    print("S(R(x))   : ", H(10))  # (100 + 100/2)**2
    print("R(S(x))   : ", J(10))  # (10**2) + 50

    S = Compose(S)  # <--- this is what @decorator does
    R = Compose(R)  # <--- R is replaced with its proxy
    
    print("="*10)
    # multiply to compose
    H = S * R   # new H, same inner workings
    J = R * S   # expecting J to keep doing J
    
    print("(S * R)(x): ", H(10))  # (100 + 100/2)**2
    print("(R * S)(x): ", J(10))  # (10**2) + 50
    
    
    print("="*10)
    # decorate to compose
    
    @Compose
    def addK(s):
      return s + "K"
      
    @Compose
    def addBang(s):
      return s + "!"

    # addM and addK are actually Compose type thanks to decorator
    fun_func = (addBang ** 4) * addK # multiply and power!
    print("Test decorated versions: ", fun_func("O"))

if __name__ == "__main__":
    main()