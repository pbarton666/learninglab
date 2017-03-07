#py_getters_and_setters_2.py


class SomeClass():
	def __init__(self, some_value):
		self.some_value=some_value
		
	@property
	def some_value(self):
		return self.__some_value
	
	@some_value.setter
	def some_value(self, some_value):
			if isinstance(some_value, int) and \
			   some_value > 0 and \
			   some_value <= 100:
								
			   self.__some_value=some_value
						   
			else:
				msg = "Sorry, Charlie, this needs to be between 1 and 10."
				print(msg)
		
		
cls=SomeClass(41)
print("value is: {}  ".format( cls.some_value))
cls.some_value=666
print("value is: {}  ".format( cls.some_value))