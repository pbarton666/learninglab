#py_binary_operations.py	

base_10_number = 12

fmt = "{:<20} {:<30}"

print("Base 2 operations: left shift increases by powers of 2")
for i in range(3):
    print(fmt.format("mybin_1000: ", bin(base_10_number << i)))

print()

print("Base 2 operations: right shift reduces by powers of 2")
for i in range(3):
    print(fmt.format("mybin_1000: ", bin(base_10_number >> i)))

#This is like the base 10 operation of increasing the power of 10
print()
base = 12
print("Base 10 operations:")
fmt = "base number raised to 10**:{:<20} {}"
for i in range(-3,3):
    print(fmt.format(i, round(base * 10**i, 3)))


