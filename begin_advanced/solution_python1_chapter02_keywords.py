#solution_python1_chapter02_keywords.py
"""Solutions to Chapter 2 keyword problem"""

import keyword

#get all the keywords
all_kw=keyword.kwlist

####### String methods  #######

#figure out how many there are
kw_count=len(all_kw)

#one approach might be to use string methods to keep track of guessed and unguessed words   
guessed=''    #not required (we don't need to initialize)

#a counter for correct guesses
counter=0

#what the user types when giving up
cry_uncle="Uncle1"

#for demo purposes, we'll loop through some simulated responses
for guess in ('if', 'else', 'else', 'in', cry_uncle):

	list_of_guessed=guessed.split(",")  
	
	#keep track of correct guesses
	if guess in all_kw and not guess in list_of_guessed:
		#if the string is empty, add the keyword
		if len(guessed)==0:
			guessed=guess
		#if there's already a correct guess, add a comma and the new one
		else:
			guessed += "," + guess
		#either way, increment the counter
		counter+=1	

	print(guessed)	
		
	#if user gives up or has guessed them all, print it out
	if guess==cry_uncle or counter==kw_count:    
		format_string = "{:^10} {:^10}"
		print(format_string.format("guessed", "missed"))
		print(format_string.format(counter, kw_count-counter))
		
		
####### List methods  #######

import keyword

#get all the keywords
all_kw=keyword.kwlist

#figure out how many there are
kw_count=len(all_kw)

#we could use a list to track correct guesses directly
list_of_guessed=[]

#what the user types when giving up
cry_uncle="Uncle1"

#for demo purposes, we'll loop through some simulated responses
for guess in ('if', 'else', 'else', 'in', cry_uncle):
	
	if guess and not guess in list_of_guessed:
		list_of_guessed.append(guess)
		
	if len(list_of_guessed)==len(all_kw) or guess == cry_uncle:
		#we're done, but now it's easy to report all guessed/unguessed
		unguessed = []
		for kw in all_kw:
			if not kw in list_of_guessed:
				unguessed.append(kw)
		
		#print the table
		print("\n\n")
		format_string = "{:^10} {:^10}"
		print(format_string.format("guessed", "missed"))
		print(format_string.format(len(list_of_guessed), len(unguessed)))
		print("\n"*3)
		
		
		#if we want more detail
		format_string = format_string = "{:^10} {:^10}  {:^10}"
		print(format_string.format("keyword", "guessed", "missed"))
		print(format_string.format("-"*10, "-"*10, "-"*10))
		for kw in all_kw:
			if kw in list_of_guessed:
				print(format_string.format(kw, "X", ""))
			else:
				print(format_string.format(kw, "", "X"))
				
		
