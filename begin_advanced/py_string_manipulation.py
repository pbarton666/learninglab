#py_string_manipulation.py
seven_deadly="   avarice envy wrath sloth \
                 gluttony lust hubris   "     #some popular sins

#Do we have this sin?   Note the use of lower() and in.
sin='eNvY'                                     
print("{} in there?  {}\n".format(sin.lower(), 
                                  sin.lower() in seven_deadly.lower()))

#Do we NOT have this sin?  Note the use of keyword not for Boolean negation.
print("try the key word not")
print("{} NOT in there?  {}\n".format(sin.lower(), sin.lower() not in seven_deadly))

#Locate the position,  Note the two-element tuple object.
for sin in ('envy', 'texting while driving'):
	sin_position=seven_deadly.find(sin.lower())
	if sin_position >=0:
		print("Yup.  We found '{}' starting in position {}\n".
		         format(sin.lower(), sin_position))
	else:
		print("Nope.  Since find() returned {}, no '{}'\n".
		         format( sin_position, sin.lower()))
		
#Replace characters
print("strings are immutable - compare these")
seven_deadly.replace('avarice', 'greed')
print("no replacement:  ", seven_deadly)
seven_deadly=seven_deadly.replace('avarice', 'greed')
print("replaced at last:  ", seven_deadly + '\n')		

#Remove leading/trailing spaces.  Note chained methods.
print("original sin list is {} characters long".format(len(seven_deadly)))
print("with the white spaces removed it's {} long".format(len(seven_deadly.strip())))
