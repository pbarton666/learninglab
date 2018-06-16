import pickle
import csv

#list comprehension
my_tuple = tuple([  i for i in range(1, 9 *10 +1) if not i % 9 ])
print("the tuple:  {}".format(my_tuple))
print()

#create a pickle file, dump then retrieve the tuple
pickle_fn = 'pickle_fn.pkl'
with open(pickle_fn, 'wb') as pf:
	pickle.dump(my_tuple, pf)	
with open(pickle_fn, 'rb') as pf:
	recovered = pickle.load(pf)
	
print("recovered:  {}".format(recovered))
print()
	
#write a csv file, two elements per line
text_file_name = 'text_file.csv'
with open (text_file_name, 'w', newline = '') as tf:
	writer = csv.writer(tf)
	for i in range(0,10,2):
		writer.writerow( [ recovered[i], recovered[i + 1] ] )

#print it out to ensure that we got it right	
print("the text file a row at a time:")
with open(text_file_name, 'r') as tf:
	for i in range(0,10,2):
		print(tf.readline(), end = '')
print()	


class Dog():
	def __init__(self, name):
		self.name=name

class Pack(Dog):
	def __init__(self):
		self.members=[]
	def __add__(self, new):
		self.members.append(new.name)
		      
pack=Pack()

for name in ('lassie', 'spicey', 'kelly'):
	pack + Dog(name)
	
print("Yay! There are now {} dog(s):\n{}\n"\
          .format(len(pack.members), ', '.join(pack.members)))	


		


x=1