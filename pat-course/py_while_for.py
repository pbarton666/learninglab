#py_while_for.py	
stop_me=False
counter=0
for i in range(10):
	if i%2: #odd numbers:
		while True:
			if counter==1:
				print("One is the lonliest number that there ever was.")
				counter +=1
				continue
			print("the counter is now: {} and i is now {}.".format(counter, i))
			if counter>1:
				break #only breaks out of the inner(while) loop
			counter+=1
	if i > 5:
		print("I'm done - about to go on a break.")
		break  #this breaks out of the outer (for) loop