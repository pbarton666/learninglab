# py_fractions.py

"""
Python has a rational number type, although it didn't always.

Suppose you wanted to write your own Fraction type, such 
that instances add, multiply etc. to give more Fractions?

Here's one such solution, tested by main():
"""

def main():
  "demo the Q type (rational number type)"
  q = Q(1,2)
  p = Q(2,5)
  print("p:       =", p)
  print("q:       =", q)
  print("p+q      =", p+q)
  print("p/q      =", p/q)
  print("p*q      =", p*q)
  print("p-q      =", p-q)
  print("q*q*q    =", q*q*q)
  print("q**3     =", q**3)
  print("p*p**-1  =", p*p**-1)  
  print("gcd(10,15) = ", Q._gcd(10, 15))
  
class Q:

  def __init__(self, n, d):
    gcd = self._gcd(n, d) # reduce to
    self.numer = n // gcd # lowest
    self.denom = d // gcd # terms
 
  @staticmethod
  def _gcd(a, b):
    """
    Euclid's Method used for 
    reducing to lowest terms
    """
    while b:
      a, b = b, a%b 
    return a
      
  def __add__(self, other):
    return Q(self.numer * other.denom 
        + other.numer * self.denom, 
          self.denom * other.denom)
    
  def __neg__(self):
    return Q(-self.numer, self.denom)
    
  def __sub__(self, other):
    "add the additive inverse"
    return self + -other
    
  def __mul__(self, other):
    return Q(self.numer * other.numer, 
             self.denom * other.denom)

  def __pow__(self, n):
    if not isinstance(n, int):
      raise ValueError("only integers supported")
    if n == 0:
      return Q(1,1)   # identity function
    me = self if n > 0 else ~self
    n = abs(n)
    for _ in range(n-1):
      me *= self # me times me times me...
    return me
    
  def __invert__(self):  # same as "reciprocate"
    return Q(self.denom, self.numer)
    
  def __truediv__(self, other):
    "multiply by 1/other i.e. ~other"
    return self * ~other
    
  def __str__(self):
    return "({}/{})".format(self.numer, self.denom)
    
  def __repr__(self):
    return "Q({},{})".format(self.numer, self.denom)

if __name__ == "__main__": 
    main()  