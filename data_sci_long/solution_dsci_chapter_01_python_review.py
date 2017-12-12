solution_dsci_chapter_01_python_review.py

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
	pack+Dog(name)
	
print("Yay! There are now {} dog(s):\n{}\n"\
          .format(len(pack.members), ', '.join(pack.members)))	


		


x=1