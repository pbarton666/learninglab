#py_nested_dict.py

"how to use nested dicts"
names=['Snarky', 'Fang', 'Sara']
toys=['bone', 'squrrel', 'squeaker']
weights=[23,30,40]

mydict={}
index=0  
for name, toy, weight in zip(names, toys, weights):
	mydict["dog_"+str(index)] = {'name': name,
	                             'toy': toy,
	                             'weight': weight}
	
	index+=1
	
for key, value in mydict.items():	
	print("{} :   {}".format(key, value))

fav_toy=mydict['dog_1']['toy']	
print("\nThe first dog's fav toy is: {}".format(fav_toy))		




