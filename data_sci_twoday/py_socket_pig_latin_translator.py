#py_socket_pig_latin_translator.py

"""Pig latin translator:
    - words beginning with a vowel get '-ay' appended and
       returned
    - otherwise initial constanent/dipthong is split from the end
        of the word and returned as <end> <initial> '-ay'
"""
vowels='aeiouy'

def pig(sentence):
	
	translated=[]
	for word in sentence.split():
		if isinstance(word, bytes):   #bytes -> str if needed
			word=word.decode('utf-8')
		for index, ch in enumerate(word):
			if ch in vowels:
				if not index:
					#first letter a vowel ex: eat -> eat-ay
					translated.append(word + '-ay')
				else:
					#otherwise ex: store -> ore-stay
					translated.append(word[index:] + '-' + word[:index] + 'ay')
				break
	return " ".join	(translated)

if __name__=='__main__':
	#these should work
	translate_me=(('eat', 'eat-ay'),
	            ('sing', 'ing-say'),
	            ('store', 'ore-stay'),
	            ('straw', 'aw-stray'),	
	            ('singing in the rain', 'inging-say in-ay e-thay ain-ray'),
	)
	for raw, expected in translate_me:
		print(raw, '|',pig(raw))
		assert pig(raw)==expected
		
	

