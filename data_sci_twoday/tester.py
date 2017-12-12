#CN11T-9MEM8-WAJGE-33XJT

#py_multiproc_2.py

#do you need a queue?
#when to use popen

import multiprocessing as mp
import time
import sys

def worker(number):
	"here's where the actual work is done"
	print('Worker {} here!'.format(number))
	time.sleep(.1)

if __name__ == '__main__':
	#code is "hidden" here to avoid recursion (this module
	# is imported for each new process)

	for i in range(5):
		p = mp.Process(target = worker,          #an (optional) worker method
				       args = [i],               #an (optional) iterable
				       #name = 'worker_' + str(i) #an (optional) name
				       )
		p.start()                                #start it up
		time.sleep(.1)                           #just so we can see some output
		#sys.stdout.flush()