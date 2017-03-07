#py_compound_conditionals.py
for numerator, denominator in (  (1, 0), (9, 3) ):
	if denominator and numerator/denominator ==3:
		print("yay!  We have a {}!".format(numerator/denominator))

	