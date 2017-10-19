class Animal:
	def __init__(self):
		self.name='fauna'
	@classproperty
	def name(self):
		Animal.name="fauna"
class Dog(Animal):
	def __repr__(self):
		return("Woof!")
	
class Cat(Animal):
	def __repr__(self):
		return("Derp.")		
	
class Dat_1(Dog, Cat):
	pass
dat1=Dat_1()
print(dat1.__repr__())

class Dat_2(Cat, Dog):
	pass
dat2=Dat_2()
print(dat2.__repr__())

x=1
	