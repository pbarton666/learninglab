#solution_python1_chapter04.py

"""A solution to Chapter 4"""

def sorter(key):
	"simply returns the value"
	return players[key]

players={225:('Jake', 'Arrieta'),
         234:('Jake', 'Buchanan'),
         240:('Trevor', 'Cahill')}

key_list=list(players.keys())
key_list.sort(key=sorter)

fmt= "{last:<15} {first:<15} {weight:<10}"
print(fmt.format(last="last", first="first", weight="weight"))
dashes="-"*8
print(fmt.format(first=dashes, last=dashes, weight=dashes))
      
for key in key_list:
	first, last = players[key]
	print(fmt.format(first=first, last=last, weight=key))

##################################

players={"Arrieta": ("Jake", 225),
         "arriETTA": ("Jake", 225),
         "arrieta": ("Jake", 225) }


clean_keys=set()
clean_dict=dict()

#dedup by taking advantage that sets only allow unique values
for key, value in players.items():
	element_ct=len(clean_keys)        #"before"
	first, weight = players[key]
	clean_keys.add(key.lower())
	if len(clean_keys) > element_ct:  # compare "before" length to "after"
		clean_dict[key.lower()]=(first, weight)   # if the set grew, add (k,v) pair to new dict

# print it out to see what we've got
print()
print(fmt.format(last="last", first="first", weight="weight"))
print(fmt.format(first=dashes, last=dashes, weight=dashes))

for key in clean_dict.keys():
	first, weight = clean_dict[key]
	print(fmt.format(first=first, last=key, weight=weight))
	a=1