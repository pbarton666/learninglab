#intro to inheritance and encapsulation code
class A:
	def __init__(self, color="blue"):
		self.__name__="I am class A"
class B:
	def __init__(self, color='white'):
		super().__init__()
		print("Class B here." )
		self.color=color
		print("Class B here.  My color is {}".format(self.color))
		
	@property
	def color(self):
		print("returning a color")
		return self.__some_color
	
	@color.setter
	def color(self, color):
		print("setting a color")
		self.__some_color=color

b=B('orange')
x=1

"""
Exercise:
Please build a hierarchal class structure to represent some transportation.
Your code should include the following
     Vehicle (has a wheels attribute to keep a count)
     MotorVehicle (inherits from Vehicle, adds a motor)
         Car(inherits from Vehicle, has four wheels, adds has_AC attribute)
         MotorCycle (inherits from Vehicle, two wheels, adds has_fairing attribute)

Please include a __str__() method for each (returns what print() displays)
and a __repr__ method (returns what gets displayed when object name is typed at keyboard)

The Motorcycle should accept a 'fairing color' attribute, first testing to make sure that it's
a string, and not any permutation of PINK, Pink, etc.  (it's just wrong ;-).

Don't forget to use super() to make sure you get the parent(s) attributes.
"""

