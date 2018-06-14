#py_dict_2.py
my_dict = {'team': "Cubs", "town": "Chicago", "rival": "Cards"}
print("dict is: {}\n".format(my_dict))
default = None

#use popitem() to get some (unknown) item.  Will crash if dict is empty.
if my_dict:
    key, value = my_dict.popitem()
    print("we've removed: {}\n".format(value))
    print("dict is now: {}\n".format(my_dict))

#with pop() we can pick a key and use a default, just in case
for looking_for in ("house beer", 'team'):
    key_value_tuple = my_dict.pop(looking_for, default)
    if key_value_tuple:
        print("{} is {}\n".format(looking_for, key_value_tuple))
    else:
        print("sorry, no {} here".format(looking_for))







