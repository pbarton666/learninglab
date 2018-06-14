"""
thread.py: Use threading.Thread subclass to specify thread logic in run() method
. """
import threading
import time

class MyThread(threading.Thread):
	def __init__(self, sleep_seconds, *args, **kw):
		threading.Thread.__init__(self, *args, **kw)
		self.sleep_seconds = sleep_seconds
		
	def run(self):
		print("{} started".format(self.name))
		time.sleep(self.sleep_seconds)
		for i in range(self.sleep_seconds):
			for j in range(100000):
				k = j+5  #some arbitrary calculation
			print("{} working ... done with pass {}".format(self.name, i))
		print("{} finished - only took {} seconds".format(self.name, self.sleep_seconds))
			
			
running_threads = threading.active_count()
#a list of thread object instances
thread_list = [MyThread(i+1) for i in range(6)]

for thread in thread_list:
	thread.start()
	print("{} thread(s) are running".format(threading.active_count()))
	s=1

while threading.active_count() :
	time.sleep(1)
	print("z"*50)
	a=1
