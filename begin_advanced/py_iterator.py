#py_iteraror1.py
class FibonacciNumbers:
    '''iterator that creates the Fibonacci sequence
       (starting with 0 and 1, adds them up to get the next: 1
            then adds 1     1  to get 2
            then adds 1     2         3
            then adds 2     3  to get 5    and so on)
    '''

    def __init__(self, max=6):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib_num = self.a
        if fib_num > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib_num


myfib=FibonacciNumbers()
for number in myfib:
    print(number, end=" ")

    