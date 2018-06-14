#py_dict.py
the_dict = {"key":"value", "A":2, "B":3}
same_dict = dict(key="value", A=2, B=3)

print("Dict compare    :", the_dict == same_dict)
print("And here's the dict:", the_dict)

the_dict['C']=3
print("... and again:", the_dict)

my_value=the_dict.get('D', "some default value")
print("... and yet again:", the_dict)
print("... (and my_value is: {})".format(my_value))




