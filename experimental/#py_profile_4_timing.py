#py_profile_4_timing.py

"How to profile and time code"

#earlier versions of python lacked the faster cProfile
try:
	import cProfile as profiler
except:	
	import profile as profiler

#allows analysis of profiled results	
import pstats

#allows timing of small bits of code
import timeit

#******* some profiling *********

LOOP_COUNT = 100
lst = []
results_file_name = 'results.prf'

def outer_fun():
	for i in range(LOOP_COUNT):
		middle_fun()
		
def middle_fun():
	for i in range(LOOP_COUNT):
		inner_fun()

def inner_fun():
	for i in range(LOOP_COUNT):
		lst.append('x')

#print a report to standard output
profiler.run("outer_fun()")

#alternatively, dump a report to a file then print it
profiler.run("outer_fun()", results_file_name)
stats = pstats.Stats(results_file_name)
stats.print_stats()

#*******using timeit library

#we can experiment with different ways to "skin the cat"

#testing list.append()
t_1 = \
"""
ls = []
for i in range(100):
	ls.append(i)
"""
print("Using append, this takes {} seconds".format(\
    timeit.timeit(t_1, number = 1000)))

#testling a list comprehension		
t_2 = \
"""\
[i for i in range(100)]
"""
print("Using a comprehension, this takes {} seconds".format(\
    timeit.timeit(t_2, number = 1000)))

	
	