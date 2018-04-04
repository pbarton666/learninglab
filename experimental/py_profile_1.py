try:	
    import cProfile as profiler
except:

    import profile as profiler

def fib(n):
    # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq

if __name__=='__main__':
    print ('fib_seq')
    print ( '=' * 80)
    profiler.run('print (fib_seq(20)); print()')
  