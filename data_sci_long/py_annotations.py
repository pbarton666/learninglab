#python 
def foo(a, b: 'annotating b', c: int) -> float: 
	help(b)
	print(a + b + c)

a=foo(1,2,3)
print(type(foo))