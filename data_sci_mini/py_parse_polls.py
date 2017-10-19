#py_parse_polls.py

"""Parse a raw table from RCP.  A few sample lines (tab delimited):
[Rasmussen Reports	'3/19 - 3/21'	'1500 LV'	46	54	-8]
[Economist/YouGov	'3/19 - 3/21'	'1296 RV'	44	49	-5]
[Reuters/Ipsos	    '3/17 - 3/21'	'1606 A'	47	47	Tie]
"""

import csv
from datetime import datetime

#file specs
raw_file_name='py_polls_raw.txt'
header_lines=7
data_year=2017

#output specs
header_in_out=True
out_file_name='py_polls_clean.csv'
fields=('name', 'start', 'end', 'n', 'sample', 'approve', 'disapprove', 'spread')
ix_dict= {name:ix for ix, name in enumerate(fields)}  #lets us use names for indices


def clean_row_rcp(row):
	"the guts of the data cleaning"
	#placeholder list for clean data
	clean_row=['' for i in range(len(fields))]      
	#incoming raw data here
	row_elem=row[0].split('\t')   

	#poll names are 1-3 words long. First element w/ number is the start date

	if row_elem[1][0].isdigit():
		start=1
		clean_row[ix_dict['name']]=row_elem[0]

	elif row_elem[2][0].isdigit():
		start=2
		clean_row[ix_dict['name']]='_'.join((row_elem[0], row_elem[1]))		

	elif row_elem[3][0].isdigit():
		start=3
		clean_row[ix_dict['name']]='_'.join( (row_elem[0], row_elem[1], 
		                                      row_elem[2], row_elem[3] ))

	else:
		start=4
		clean_row[ix_dict['name']]='_'.join( (row_elem[0], row_elem[1], 
		                                      row_elem[2], row_elem[3] ))			

	#convert the start and end dates (like 3/21) to datetime objects		
	month, day=row_elem[start].split('-')[0].strip().split('/')
	clean_row[ix_dict['start']]=datetime(data_year, int(month), int(day))

	month, day=row_elem[start].split('-')[1].strip().split('/')
	clean_row[ix_dict['end']]=datetime(data_year, int(month), int(day))			

	#get integer versions of the actual sample data, where appropriate.
	#  Failed operations typically indicate a missing field e.g. N

	try:
		sample_n, sample_type = row_elem[start+1].split()
		clean_row[ix_dict['n']]          = int(sample_n )
		clean_row[ix_dict['sample']]     = sample_type 
		clean_row[ix_dict['approve']]    = int(row_elem[start+2] )
		clean_row[ix_dict['disapprove']] = int(row_elem[start+3] )
		if not row_elem[start+4].lstrip('-').isdigit():
			clean_row[ix_dict['spread']] = 0  #might be a 'Tie'
		else:
			clean_row[ix_dict['spread']] = int(row_elem[start+4] )
	except ValueError:
		print("So sorry, I couldn't parse this row:\n{}".format(row_elem))
	
	return clean_row

def write_output_file(data):
	'''write the clean list to the output file'''
	with open(out_file_name, 'w') as fh:
		writer=csv.writer(fh)
		for row in data:
			writer.writerow(row)

def process_input_file(raw_file_name=raw_file_name):
	"processes each row of input file"
	
	#start with an empty list to hold our cleaned-up lines of data
	clean=[]
	if header_in_out: clean.append(list(fields))	
	#create a file handle (produces an iterator for csv)
	with open(raw_file_name, 'r') as fh:
		
		#create a reader
		reader=csv.reader(fh)
		
		#pick off the headers
		for _ in range(header_lines):
			next(reader)
			
		#preen each row of raw data and add to a clean list	
		for row in reader:  
			clean.append(clean_row_rcp(row))	
			
	return clean

if __name__=='__main__':
		#a couple o' quick tests
		test   = ['Gallup\t8/1 - 8/3\t1500 A\t36\t58\t-22']		
		expected = ['Gallup',
						datetime(2017, 8, 1, 0, 0),
						datetime(2017, 8, 3, 0, 0),
						1500, 'A',36,58, -22]
		result=clean_row_rcp(test)
		assert result==expected
				
		test   = ['Gallup\t8/1 - 8/3\t1500 A\t36\t36\tTie']		
		expected = ['Gallup',
		                datetime(2017, 8, 1, 0, 0),
		                datetime(2017, 8, 3, 0, 0),
		                1500, 'A',36,36, 0]
		result=clean_row_rcp(test)
		assert result==expected				
		x=1

    #this processes our file
		data=process_input_file(raw_file_name)
		write_output_file(data)
		#print it out, if desired
				
		with open(out_file_name, 'r') as fh:
			#create a reader
			reader=csv.reader(fh)
			for row in reader:
				print(row)
		
				