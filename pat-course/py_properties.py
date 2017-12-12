#py_properties.py

"Illustrate use of properties"

class Dog():
	def getName(self):
		print('getName here')
		return self._private_name
	def setName(self, name):
		print('setName here')
		self._private_name=name
	def delName(self):
		print('delName here')
		del self._private_name
	name=property(getName, setName, delName, doc="name doc")
	
dog=Dog()          #make an instance
dog.name="Fido"    #assign a value to an instance attribute 
help(Dog.name)     #note, you've got to call help on the class
del dog.name       #delete the instance attribute

class SameThingButDifferent():
	@property
	def name(self):
		"docstring for name"
		print("name() here as getter")
		return self._private_name
	
	@name.setter
	def name(self, name):
		self._private_name=name
		
	@name.deleter
	def name(self):
		del self._private_name	


dog = SameThingButDifferent()  #create an instance
dog.name="Fido"                #assign a value to instance attribute
help(SameThingButDifferent.name)                 #note, you've got to call help on the class

del dog.name