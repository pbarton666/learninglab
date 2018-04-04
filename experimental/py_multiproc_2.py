#py_multiproc_2.py

"Add and remove items from a process queue"

from multiprocessing import Process, Queue
import time

def add_element(q, activity):
	"loads an object (could be anything) into the queue"
	q.put(activity)
	
def load_queue(q, iterable, priority = None):
	"loads up a queue with elements of an iterable"
	for thing in iterable:
		p = Process(target=add_element, args=(q, thing))
		p.start()
		p.join()		
		
def unload_queue(q):
	"systematically remove and prints elements"
	while q.qsize():
		print(q.get(), "CHECK!")
		time.sleep(1)

if __name__ == '__main__':
	q = Queue()                    #FIFO queue
	#elements can be (picklable) objects
	todo = ['work out', 'program', 'eat dinner']
	load_queue(q, todo)
	unload_queue(q)

	print("Done!")

