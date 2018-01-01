#py_multiproc_1.py

"""Demonstrates basic usage of multiprocessing -
   tracking of parent, child processes via process IDs
"""

import multiprocessing as mp
import sys
import os

def worker():
    "some important work here, in real life"
    pass

if __name__ == '__main__':
    
    print("parent process: {}".format(os.getpid()))
    
    for i in range(5):
        p = mp.Process(target = worker,          #an (optional) worker method
                       name = 'Worker_' + str(i) #an (optional) name
                       )
        p.start()                                #start it up
        stg = "Hi, I'm {},   process number {}"
        print(stg.format(p.name, p.pid))         #processes are self-aware
        p.join()                                 # "wait for process to finish"
