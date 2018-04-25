#solution_python1_chapter02_operations.py
"""A solution to Chapter 2"""


#help on the modulo operator (help() already prints
help(int.__mod__)

#how many fires?
buckets_per_fire=3
buckets_available=50

#use modulo operator to scrap remainder, then convert to an int type
whole_fires =  buckets_available - buckets_available % buckets_per_fire
fires_snuffed =int(whole_fires / buckets_per_fire)
print("fires snuffed: {}\n".format(fires_snuffed))


#which operators work, and what's the result?

#"+" operator
print("calculating 'hi' + 'hi' = ", "hi" + "hi")
print("calculating 3.0 + 3.0 = ", 3.0+3.0)
print("calculating (1+2j) + (2+3j) = ", (1+2j) + (2+3j))
print()

print("calculating 3.0 - 3.0 = ", 3.0-3.0)
print("calculating (1-2j) - (2-3j) = ", (1-2j) - (2-3j))
print()

print("calculating 3.0 / 3.0 = ", 3.0/3.0)
print("calculating (1/2j) / (2/3j) = ", (1/2j) / (2/3j))
print()

print("calculating 3.0 - 3.0 = ", 3.0-3.0)
print("calculating (1-2j) - (2-3j) = ", (1-2j) - (2-3j))
print()
print("calculating 'hi' * 2 = ", "hi" * 2)
print("calculating 3.0 * 3.0 = ", 3.0*3.0)
print("calculating (1*2j) * (2*3j) = ", (1*2j) * (2*3j))


#Dialogue
name =   input("Hi, what's your name?...")
sign =   input("And what's your sign?...")
fav_bev= input("What do you like to drink?...")
summary= "So your name is " + name + ", " \
			   "you are a " + sign + ", " \
			   "and you like to drink " + fav_bev+ ". " \
			   "Right?  "
answer=   input(summary)
print("You said " + answer + ".  Awesome!")
