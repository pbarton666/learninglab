import pstats
try:	
	import cProfile as profiler
except:
	import profile as profiler
from py_profile_1 import fib, fib_seq

#interesting gui stats visualizer (KCacheGring) described here:  
#https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara

fib_count=20
fn='profile_stats'
#run profiler, dump output to  a file
profiler.run("fib_seq({})".format(fib_count), fn)

#ransack it for stats
stats=pstats.Stats(fn)

#strip extended dir names and print
stats.strip_dirs().sort_stats(-1).print_stats()
stats.sort_stats('time').print_stats()



