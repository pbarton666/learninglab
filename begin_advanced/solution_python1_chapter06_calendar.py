#solution_python1_chapter06.py
"""A solution to Chapter 6 ... gaining comfort with calendar utilities"""

import datetime
import calendar
from pprint import pprint as pp

#not for production code, but good for debugging
debug=False

bday_text="May 5, 1970"

#parse out the contents
bday_parts=bday_text.replace(',','').split()

#convert month to integer
month_dict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,
            'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10,'Nov':11, 'Dec':12}

#create a datetime object from the parsed birthday
mon, day, yr = bday_parts
bday_datetime=datetime.datetime(int(yr), month_dict[mon], int(day))

#figure out how long ago that was, using datetime objects
now=datetime.datetime.now()
delta=now - bday_datetime

#parse out the days and roughly figure out age in years
days_ago = delta.days 
age = delta.days / 365   #doesn't count leap year, but oh, well

#figure out the day of week using calendar.weekday; returns an integer (Mon=0)
bday_day_of_week=calendar.weekday(int(yr), month_dict[mon], int(day))

#for the calendar, we need to know what day the 1st falls on
first_day_of_week=calendar.weekday(int(yr), month_dict[mon], 1)

#.. and how many days that month has 
_, last_day_of_bday_month=calendar.monthrange(int(yr), month_dict[mon])

#Now, all we need is to populate a calendar to print out.  Strategy:
#  make a list for the month, comprised of lists for each week.  We can
#  use calendar.weekday to get the day code for each day.  If the code is
#  0, it's a Monday and we need to append a new list for a new week.

cmonth=[]  #the whole month

#First, let's make a "magic decoder ring" for the weekday and create a header list
weekday_dict={0:'Mon', 1:'Tue', 2:'Wed', 3:'Thr', 4:'Fri', 5:'Sat', 6:'Sun'}

#load up the header
header_list=[]
for day_index in range(7):
	header_list.append(weekday_dict[day_index])
cmonth.append(header_list)

#load up a list for each week and append it to the calendar

for a_day in range(1, last_day_of_bday_month+1):
	day_of_week=calendar.weekday(int(yr), month_dict[mon], a_day)
	
	#make a fresh list if this either Monday or the 1st
	if day_of_week == 0 or a_day==1:
		week_list=[]
		
	#if it's the 1st, we may need to "pad out" null elements for previous days
	if a_day==1:
		for index in range(day_of_week):
			week_list.append("")
	
	week_list.append(a_day)
	
	if debug: pp(week_list)
	
	#if it's Saturday, append the list to the monthly calendar
	if day_of_week==6:
		cmonth.append(week_list)
		
	if debug: pp(cmonth)

#print out our birthday details
	
print("I was born on {}".format(bday_text))
print()
print("That was {} days ago ... and it makes me {}.".format(days_ago, int(age)))
print()
print("Here's a calendar for that month:")
print("\n{:^28}".format(mon + ", " + str(yr)))

cal_fmt="{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4} "
for week in cmonth:
	print(cal_fmt.format(week[0],week[1],week[2],week[3],week[4],week[5],week[6]))

