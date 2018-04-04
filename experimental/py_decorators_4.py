#py_decorators_4.py

"""A tongue-in-cheek use case for decorators using a color selection
     screening tool"""

from matplotlib import colors

#most ladies know zillions of colors
distaff_colors = colors.get_named_colors_mapping().keys()
#males, not so much
male_colors = ['red', 'blue', 'yellow']

#a few gender choices
genders = ('m', 'f', 'x')

from functools import wraps

def color_screener(func):
	"""Make sure males don't get over their heads by straying from
	     primary colors:-)   Make sure everyone else chooses a valid
		 color."""
	
	#here, we'll add warnings to the kwargs if needed.
	@wraps(func)
	def decorated_func( *args, **kwargs):
		gender = kwargs['gender']
		color = kwargs['color']
		
		#is geneder valid?
		if gender not in genders:
			kwargs['warning'] = \
			    "sorry " + gender + " is not yet supported"
			
		if gender == 'm':
			#males are only allowed primary colors
			if color in male_colors:
				pass
			
			elif color in distaff_colors:
				kwargs['warning'] = \
				    'as a male you are unqualified to '\
				    'choose' + color
			else:
				kwargs['warning'] = 'sorry, invalid color: ' + color
				
		elif gender == 'f' or gender == 'x':
			#non-males can pick anything valid
			if not color in distaff_colors:
				kwargs['warning'] = 'sorry, invalid color: ' + color 
				    
		return func( *args, **kwargs)
	
	return decorated_func
	
@color_screener
def process_color_choice( **kwargs):
	"delegates mundane screening to decorator"
	#more processing could happen here, of course
	
	print("You're a '{}' and chose {}.".\
	      format(kwargs['gender'], kwargs['color']))
	if 'warning' in kwargs:		
		print(kwargs['warning'])
	else:		
		print("Congrats! {} totally works.".format(kwargs['color']))
	print()

	
#some test data
testers = ( {'color':'mauve', 'gender':'m'},            #non-existant color
            {'color':'darkgoldenrod', 'gender':'m'},    #mis-matched color
            {'color':'darkgoldenrod', 'gender':'f'},    #good
            {'color':'deeppink', 'gender':'x'},         #good
            {'color':'deeppink', 'gender':'unknown_gender'})   #unsupported gender

for test in testers:
	process_color_choice( **test)
		
x = 1	