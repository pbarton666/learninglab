#py_getters_and_setters.py

class SomeClass():
	def __init__(self, some_value):
		self.some_value=some_value
		
cls=SomeClass(41)
print("value is: {}  ".format( cls.some_value))
cls.some_value=666
print("value is: {}  ".format( cls.some_value))