#py_dangerous_globals.py

"""Demonstrates potential pitfalls of using (mutable) global-to-module
      objects in your code."""
import random

ls = []

def joe():
	if ls:
		ls.pop()
	ls.append("{} says Tag!, you're it!".format(joe.__name__))

def mary():
	if ls:
		ls.pop()
	ls.append("{} says Tag!, you're it!".format(mary.__name__))
	
for _ in range(10):
	fun = random.choice([joe, mary])
	fun()
	print(ls)
	
