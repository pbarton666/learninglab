
#py_text_debug_4.py
"rounds resource consumption for billing"
import math
from pprint import pprint

DEBUG_MODE = True

def evaluate(seconds, minimum=30, incr=15):
	"minimum time charged, then even increments"
	if seconds:  
		if seconds <= minimum:	#minimum billing is <minimum> seconds	
			return minimum
		#bill in <incr> second intervals, rounding up
		time_billed=math.ceil(seconds/incr) * incr 
		if DEBUG_MODE: print("\n\nlocals:"); pprint(locals())
		return time_billed 
	
	else: 
		return 0

if __name__=='__main__':
	#expected individual results with test data
	secs=    [0,    15, 30, 35, 50, 75, 90, None]
	targets= [0,    30, 30, 45, 60, 75, 90, 0]
	
	total=0
	
	#this checks each test value against expected
	for sec, target in zip(secs, targets):
		answer=evaluate(sec)
		assert(target== answer)
		total+=answer
		if DEBUG_MODE and sec >50: print("\n\nglobals:"); pprint(globals())
		
	#this makes sure we got the total right
	assert(total==sum(targets))
	