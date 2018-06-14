#py_iterator_2.py
import time
COLORS=('red', 'blue', 'green', 'orange', 'puce', 'off-mauve', 'silver', 
        'white', 'black', 'pavement pizza orange')
def random_choice():
	while True:
		index=int(str(time.time())[-1])
		yield COLORS[index]

while True:
	print (time.time())
	time.sleep(.1)

my_colors=random_choice()
for _ in range(10):
	print( next (my_colors) , sep = '|')
	time.sleep(.1)