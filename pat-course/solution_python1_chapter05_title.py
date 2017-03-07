"""A solution to Chapter 2"""

lst=["shot in the dark", "guido van rossum", "monty python's life of brian"]
lst.extend(["pat's thing", "von RYAN's express", "Life of Brian", "trials of o'malley"])

new_titles=[]
for title in lst:
	fixed="" #an empty string to hold the fixed title
	for word in title.split():
		#knock it to lower case for eash of handling
		word=word.lower()  
		#if it's a long word, cap the first character if it's not "noble"
		if len(word) > 3:
			if not word.startswith('von')  and not word.startswith('van'):
				word=word[0].upper()+word[1:]
		#if there's an apostrophe, cap the next letter if it's not an "s"
		position=word.find("'")
		if position >= 0:  #apostrophe found
			if word[position+1]!='s':
				#up to and including ' + next letter + rest of word
				word=word[:position+1]+word[position+1].upper()+word[position+2:]
		
		fixed+=word + " "
	#trim trailing space
	fixed = fixed.strip()
	
	new_titles.append(fixed)
	
fmt="{:<30}  {:<30}"
print(fmt.format("old", "new"))
print(fmt.format("="*20, "="*20))
for old, new in zip(lst, new_titles):
	print(fmt.format(old, new))
