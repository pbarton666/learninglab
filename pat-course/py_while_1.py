#py_while_1.py	
counter=0
while True:
	if counter==1:
		print("One is the loneliest number that there ever was.")
		counter +=1
		continue
	print("The counter is now: {}.".format(counter))
	if counter>1:
		break
	counter +=1
else:
	print("Yo.  I'm done!")
		
	