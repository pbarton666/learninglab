#py_dict_3.py

def sorter(key):
	"simply returns the value"
	return my_dict[key]

my_dict={'team': "Cubs", "town": "Chicago", "rival": "Cards"}	

key_list=list(my_dict.keys())
key_list.sort(key=sorter)
for key in key_list:
	print(key, my_dict[key])

	




