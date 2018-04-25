#py_files_1.py

f = open('afile', 'w')

f.write("Hello afile!")

print("What's up with {}?\n".format(f.name))

print("readable?", f.readable())
print("writable?", f.writable())
print("encoding?", f.encoding)
print("closed?", f.closed)

print("Closing now!")
print("closed?", f.closed)
	  