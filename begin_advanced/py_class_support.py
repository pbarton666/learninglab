#py_class_support.py
"""Demonstrate basic class operations"""

#a simple class
class Mammal():
	pass

#a class instance (a specific Mammal)
m = Mammal()

#...upgraded to initialize with instance attribute
class Mammal():
	def __init__(self):
		self.warmblooded=True

#a class instance
m = Mammal()

#single inheritance, executing parent's __init__() method
class Dog(Mammal):
	def __init__(self, name):
		Mammal.__init__(self)
		self.name=name
	def speak(self):
		print("The dog {} says:  WOOF!".format(self.name))
		
dog = Dog("Fang")
dog.speak()
print("Warmblooded?  {}".format(dog.warmblooded))

#another subclass of Mammal
class Cat(Mammal):
	def __init__(self, name):
		self.name=name
		self.breath="bad"
		Mammal.__init__(self)
		
	def speak(self):
		print("The Cat {} says:  Derp.".format(self.name))
		
cat=Cat("Snarky")
cat.speak()
print(cat.breath)

#multiple inheritance

class Dat(Dog, Cat):
	"Dog/Cat combo - MRO favors left-most argument"
	def __init__(self):
		super().__init__("Dat")  
		print("\nDat:  MRO is Dog then Cat")
		self.speak()

dat=Dat()		

class Dat(Cat, Dog):
	"Cat/Dog combo - MRO favors left-most argument"
	def __init__(self):
		super().__init__("Dat")  
		print("\nDat:  MRO is Cat then Dog")
		self.speak()

dat=Dat()

class Dat(Cat, Dog):
	"Cat/Dog combo - MRO favors left-most argument"
	def __init__(self):
		super().__init__("Dat")  
		print("\nDat:  MRO is Cat then Dog \n")
		self.speak()
d=Dat()		
		
#method override

class Dat(Cat, Dog):
	"Cat/Dog combo - MRO favors left-most argument"
	def __init__(self):
		super().__init__("Dat")  
		self.speak()
	def speak(self):
		print("I'm a Dat, and I say 'DAT'!!!")
		
dat=Dat()		
	