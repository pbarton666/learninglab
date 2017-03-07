#py_while_for.py	
counter=0
for i in range(10):
	if i %2:   #grab odd numbers
		while True:
			if counter==1:
				print("One is the loneliest number that there ever was.")
				counter +=1
				continue
			print("The counter is now: {} and i is now {}.".format(counter,i))
			if counter>1:
				break #only breaks out of the inner (while) loop
			counter +=1
	if i>5:
		print("I'm done - about to go on a break")
		break  #breaks out of the for loop
	