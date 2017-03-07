#py_string_manipulation.py
seven_deadly="   avarice envy wrath sloth gluttony lust hubris   "
#exists?
sin='eNvY'   #this is weirdly formed (common "in the wild")
print("{} in there?  {}\n".format(sin.lower(), sin.lower() in seven_deadly))

#doesn't exist?
print("try the key word not")
print("{} NOT in there?  {}\n".format(sin.lower(), sin.lower() not in seven_deadly))

#replace
print("strings are immutable - compare these")
seven_deadly.replace('avarice', 'greed')
print("no replacement:  ", seven_deadly)
seven_deadly=seven_deadly.replace('avarice', 'greed')
print("replaced at last:  ", seven_deadly + '\n')

#locate
for sin in ('envy', 'texting while driving'):
	sin_position=seven_deadly.find(sin.lower())
	if sin_position >=0:
		print("Yup.  We found '{}' starting in position {}\n".format(sin.lower(), sin_position))
	else:
		print("Nope.  Since find() returned {}, '{}' wasn't there\n".format( sin_position, sin.lower()))

print("using the keyword len, figure out how long our string is")
#note how we've got one method "swallowing another"
print("original sin list is {} characters long".format(len(seven_deadly)))


print("with the white spaces removed it's {} long".format(len(seven_deadly.strip())))
