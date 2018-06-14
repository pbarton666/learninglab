#py_strings.py
some_string="$R5a "
for s in some_string:
	print(">{}< is alphanumeric?  {}".format(s, s.isalnum()))
	print(">{}< is alpha?  {}".format(s, s.isalpha()))
	print(">{}< is numeric?  {}".format(s, s.isnumeric()))
	print(">{}< is upper?  {}".format(s, s.isupper()))
	print()
	
	