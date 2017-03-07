#py_while.py	
stop_me=False
counter=0
while not stop_me:
	print("The counter is now: {}.".format(counter))
	if counter>1:
		stop_me=True
	counter=counter+1  #counter +=1
else:
	print("Yo.  I'm done!")
		
	