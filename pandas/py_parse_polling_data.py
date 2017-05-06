#parse_polling_data.py

"""each line copied from an RCP html page is tab-delimited and looks like:
['Rasmussen Reports\t4/20 - 4/24\t1500 LV\t47\t53\t-6']

This is one-off for Real Clear Politics.  Grab all rows after the "RPC average".
http://www.realclearpolitics.com/epolls/other/president_trump_job_approval-6179.html#polls

NB the year is 'hardwired' for 2017 below
"""
import csv
from collections import namedtuple
from datetime import datetime

#We'll export these columns (not all match original)
cols=['date','poll','size', 'stype', 'approve', 'disapprove' ,'spread']
year=2017

#infile is a text file produced from a screen grab
infile='raw_polling_data.txt'
outfile='clean_polling_data.csv'

#this is what process_row() returns
Row=namedtuple("Row",' '.join(cols) )

def process_row(row):
	"parse out and process each row of survey data"
	#it's tab-delimited
	raw=row[0].split('\t')
	
	#these items are good to go
	poll=raw[0]
	approve=raw[3]
	disapprove=raw[4]
	
	#spread might be a 'Tie'
	if raw[5].strip()=='Tie':
		spread=0
	else:
		spread=raw[5]
	
	#dates are a range, something like '4/20 - 4/24'; use the last
	last=raw[1].split('-')[1]
	mon_day=last.split('/')
	date=datetime(year, int(mon_day[0]), int(mon_day[1]))
	
	#pole sample is a type and a size, something like '1500 LV'
	sample=raw[2].split()
	size=int(sample[0])
	stype=sample[1].strip()
	
	#return the namedtuple object
	return Row(date, poll, size, stype, approve, disapprove, spread )

#read, process, and write each row of input data
with open(outfile, 'w') as outf:
	writer=csv.writer(outf)
	writer.writerow(cols)
	
	with open(infile, 'r') as inf:
		inrows=csv.reader(inf)
		for row in inrows:	
			writer.writerow(process_row(row))

if __name__=='__main__':
	with open(outfile, 'r') as inf:
		inrows=csv.reader(inf)
		for row in inrows:
			print(row)			
			