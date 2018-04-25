#!/usr/local/bin/python3

#py_format_0.py
"""Some formatting exotics"""

#numbered fields ('all or none' here)
stg = "{2} {1} {0}"\
	 .format("George", "Paul", "John")
print(stg)
print()

#named fields ('all or none'; note no quotes around names)
stg = "{who} is a smart {what}"\
    .format(what = 'cookie', who = 'Silvia')
print(stg)
print()

#dig out bits of a list using format string
stg = "The 5th element of the 1st argument is {0[5]}"\
    .format( ["Dallas", "Zorg", "Cornelius", "Ruby",
              "Billy", "Leelo"])
print(stg)
print()

#refer to dict keys using format string (note no quotes)
d = {'Cher':'Sarkisian', 'Sonny':'Bono'}
stg = "Sonny's surname is {0[Sonny]}".format(d)
print(stg)
print()

#on-the fly formatting - {0:>6} means first element, 6 wide, left justified
stg = "Cher's surname is {lookup[Cher]}".format(lookup = d)
print(stg)
print()

#10 wide, accept default justification
stg = "{0:10} {1:10}"
for first, last in d.items():
	print(stg.format(first, last))

print()	
#example of numeric base "casting"; 
stg = "{0:>6} = {0:#16b} = {0:#06x}"  #note the  '#..b'  and '#0..x' 
for i in (1, 23, 456, 7890):
	print(stg.format(i))
