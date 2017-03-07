#py_iterator_1.py

def fib(max=8):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
        
f = fib()        
for i in range(10) :
    try:
        print(next( f), end = " ")
    except StopIteration:
        pass
print("\nDone!")