#py_function_6.py

def add_numbers(things_to_add):
    "adds two numbers"
    first, second=things_to_add
    
    return first+second

def find_evens(thing_to_evaluate):
    "returns True if even"
    return not thing_to_evaluate % 2  #True if 0, False otherwise


integers=[ (2,2), (4,4), (5,6), (7,8)  ]
mapped_data=map(add_numbers, integers)

filtered_results=filter(find_evens, mapped_data)
print("The even sums are {}".format(list(filtered_results)))
