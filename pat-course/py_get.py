#py_get.py

"use the dict method get()"
plant_dict={'raspberry': 'rubus',
            'elm'      : 'ulmus',
            'maple'    : 'acer'
            }

#create a format string
fmt_str="The {} is more properly called a {}."

#get() with no argument 
look_for='raspberry'
found=plant_dict.get(look_for)
print(fmt_str.format(look_for, found))

#get() with a default value
look_for='alder'
default='SOMETHING.  I dunno'
found=plant_dict.get(look_for, default)
print(fmt_str.format(look_for, found))

#get() with a default None
look_for='sumak'
default=None
found=plant_dict.get(look_for, default)
if found:
	print(fmt_str.format(look_for, found))
else:
	print("Dude, I give up ;-)")