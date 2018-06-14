#py_list_copy.py

def test_lists(first, second):
	test_result= (first==second)
	print("same list, right?  {}".format(test_result))
	if test_result==False:
		print("first id is {}    second id is {}".format(id(first), id(second)))
	

print('make a list, then create a copy')
a_list=["Tony", "Sally", "George"]
b_list=a_list
print(a_list, b_list)
test_lists(a_list, b_list)

#update the first list, but not the second.
print("\nadd someone to the a_list, leaving the b_list alone")
a_list.append("Sam")
test_lists(a_list, b_list)
print("Uh, what happened here?")




