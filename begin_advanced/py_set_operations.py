#py_set_operations.py

the_set = {"monkey", "gorilla", "dog", "cat"}
print("Set:             :", the_set)
the_set.add("parrot")
print("Set:             :", the_set)

other_set = {"gorilla", "elephant", "pig", "chicken"}

print("Set intersection  :", the_set & other_set) # intersection
print("Set union        :", the_set | other_set) # union
