#py_getters_and_setters_1.py
class SomeClass():
	def __init__(self, some_value):
		self.some_value=some_value
		
	@property
	def some_value(self):
		print("returning a value")
		return self.__some_value
	
	@some_value.setter
	def some_value(self, some_value):
		print('checking for a valid value here')
		self.__some_value=some_value
		
cls=SomeClass(41)
print("value is: {}  ".format( cls.some_value))
cls.some_value=666
print("value is: {}  ".format( cls.some_value))
