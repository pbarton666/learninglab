#solution_python1_chapter07_handler_practice.py
"""Demonstrates how to 'pass the buck' while handling exceptions. """
import sys

class SomeException(Exception):
	def __init__(self, origin):
		print("exception raised from {}".format( origin))

# bottom calls middle, which calls top; all generate exceptions						
def bottom():
	try: middle()
	except: raise SomeException(bottom.__name__)   #handle
def middle():
	try: top()
	except:  raise SomeException(middle.__name__)  #handle
def top():
	try: 1/0
	except: raise SomeException(top.__name__)      #handle



# bottom_1 calls middle_1, which calls top_1; only bottom_1 generates exception
def bottom_1():
	try: middle_1()
	except: raise SomeException(bottom_1.__name__)    #handle
def middle_1():
	try: top_1()
	except:  raise   #pass the buck
def top_1():
	try: 1/0
	except: raise    #pass the buck

#print("running the first stack\n")
#bottom()	
print("\nrunning the second stack\n")
bottom_1()	