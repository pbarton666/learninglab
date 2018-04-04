"""A solution to Chapter 5 string-wrangling function"""

ROYALTY = ('von', 'van')

def process_list(lst):
	"process a list of titles; return a list of fixed titles"
	new_titles=[]
	for title in lst:
		new_titles.append(process_title(title))
	return new_titles

def process_title(title):
	"process an individual title; return fixed title"
	new_title = []
	for word in title.split():
		new_title.append(process_word(word))
	return " ".join(new_title)

def process_word(word):
	"process an individual word; return fixed version"    
	word = word.lower()
	if word in ROYALTY:
		word = process_royalty(word)
	elif len(word) > 3:
		word = word.capitalize()
	word = fix_apost(word)        
	return word

def fix_apost(word):
	"deal with words that have apostropies"
	split_word = word.split("'")
	if len(split_word) > 1 and split_word[0].lower() == 'o':
		split_word[1]=split_word[1].capitalize()
		return "'".join(split_word)
	return word

def process_royalty(word):
	#doesn't do much now, but placeholder for later changes
	return word

#provide some titles to test out - note the extend() method
lst=["shot in the dark", "guido van rossum", "monty python's life of brian"]
lst.extend(["pat's thing", "von RYAN's express", "Life of Brian", "trials of o'malley"])		

new_titles = process_list(lst)

#provide some fancy formatting for a clean list of titles
fmt="{:<30}  {:<30}"
print(fmt.format("old", "new"))
print(fmt.format("="*20, "="*20))

#have a look at the 'before' and 'after' - note the zip() function
#new_titles=fixer_upper(lst)
for old, new in zip(lst, new_titles):
	print(fmt.format(old, new))

x=1    
import unittest
class tester(unittest.TestCase):
	def test_word(self):
		self.assertEqual(process_word("THE"), 'the')
	def test_title(self):
		self.assertEqual(process_title("pat's thing"), "Pat's Thing")
		self.assertEqual(process_title("Guido Van Rossum"), "Guido van Rossum")

unittest.main()        

