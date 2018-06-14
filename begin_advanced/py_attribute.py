#py_attribute.py

"demonstrate how Python wrangles attributes"

"""
cls already has baked-in method cls.__setattr__(), a class method-wrapper.

cls.__set_atttr__() by dint of being a method-wrapper has its own methods to include:
   __call__(self, *args, *kwargs) which calls self as a function
   __getattribute__() - does nothing and can be overridden


Here's how it works:

  - With MyClass defined only with methods set_test_val() and get_test_val it "just works"

  - Add a __getattribute__(self, name, val) method, and that's the method that gets called when
       attempting to set any value.  This happens before the interpreter actually tries to figure
	   out if the name exists.  If it raises an AttributeError, then the method
	   __getattr__(self, name, val) is called.

   - Add a __getattr__(self, name, val) to override the parent object's method.  It is 
        called internally with name already supplied.  Can be used to screen rogue names/values


"""

class MyClass():
	def set_test_val(self, val):
		print ("attempting to set val to", val)
		self.val=val				
	
	def get_test_val(self, val):
		print ("attempting to get val to", val)
		return self.val
	
	def __setattr__(self, name, val):
		print("__setattr__() here!")
		self.__dict__[name]=val

	
	def __getattr__(self, name):
		print("__get_attr__() here!")
		self.__dict__[name]="not an aardvark"
		return 	"not an aardvark"
	


cls = MyClass()
x=cls.aardvark

val='xxx'
cls.set_test_val(val)
cls.get_test_val(val)
x=cls.aardvark
x=1

