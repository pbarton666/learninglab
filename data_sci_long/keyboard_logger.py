import keyboard
until='x'
while True:
	capture = keyboard.record(until=until)
	#keyboard.send(until)

	for cap in capture:
		print(cap.name, end='')
	print()
	#print(capture)
z=1