#py_plotting_utils.py

"""General utilities for interactive display and plotting.  Demonstrates
   multiple data series on single line chart, bar charts and tools
   available for formatting time-related axes."""

#Essential matplotlib docs here:
#https://matplotlib.org/api/axes_api.html
#http://matplotlib.org/api/pyplot_api.html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as dates


def printme(*args):
	"print objects with line feed between each"
	arg_count=len(args)
	fmt_string="\n{}"*len(args)
	if arg_count==0:
		print()
	elif arg_count==1:
		print(fmt_string.format(args[0]))
	elif arg_count==2:
		print(fmt_string.format(args[0], args[1]))
	elif arg_count==3:
		print(fmt_string.format(args[0], args[1], args[2]))
	elif arg_count==4:
		print(fmt_string.format(args[0], args[1], args[2], args[3]))
	else: 
		print("sorry, this function takes at most 4 arguments")


def formatPlot2(start=None, end=None, s=None, t=None):
	"Create a line chart with a snazzy x-axis from a Series"
	
	#if not called with a Series make one up
	if not isinstance(s, pd.Series):  
		idx = pd.date_range('2017-03-01', '2017-05-01')
		s = pd.Series(np.random.randn(len(idx)), index=idx)
	#if start and end points are provided use them ...	
	else:
		if start and end:
			idx = pd.date_range(start, end)	
		#... otherwise plot the whole series
		else:
			idx=pd.date_range(s.index.min(), s.index.max())

	#formats for axes and plots.  Many more options available.  Docs: 
	#  https://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D
	minor_format='%d\n%a'
	major_format='\n\n\n%b\n%Y'	
	symbol_format='v-'

	#Shortcut way to create a plot
	fig, ax = plt.subplots()
	
	#add the data
	ax.plot_date(x=idx.to_pydatetime(), y=s, fmt=symbol_format)
	
	#Set axis label tick marks with a Locator, formatted with a Formatter
	ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=(1),
		                                            interval=1))
	ax.xaxis.set_minor_formatter(dates.DateFormatter(minor_format))

	ax.xaxis.set_major_locator(dates.MonthLocator())
	ax.xaxis.set_major_formatter(dates.DateFormatter(major_format))
	
	#make a grid
	ax.xaxis.grid(True, which="minor")
	ax.yaxis.grid()	

	#add a title and some padding 
	plt.title(t)
	plt.tight_layout()
	fig.autofmt_xdate()
	
	#et voila!
	plt.show()


def formatPlotBar(**kwargs):
	"""create a respectable bar chart for two data series.  
	
	   Inputs (all optional):
	   start, end, s1, s1_label, s1_color, s2, s2_label, s2_color
	   x_label, y_alabel, title, bar_width, opacity, freq (x-axis freq 'min', 'A', etc.)

	   Placeholders are provided
	"""

	#if start date not provided, assume placeholder values for data, index
	try:  
		#idx = pd.date_range(kwargs['start'], kwargs['end'])#use dummy data for testing
		s1=kwargs['s1']
		s2=kwargs['s2']
		freq=kwargs.get('freq', 'd')
		idx=pd.date_range(min(s1.index), max(s1.index), freq=freq)
		idx=idx.to_pydatetime()		
		
	except KeyError:
		#give 'em a dummy chart no matter what
		idx = pd.date_range('2017-03-01', '2017-05-01')
		s1 = pd.Series(np.random.randn(len(idx)), index=idx)
		s2 = pd.Series(np.random.randn(len(idx)), index=idx)
	
	#http://stackoverflow.com/questions/13703720/
	# converting-between-datetime-timestamp-and-datetime64/13753918#13753918

	
	#if labels/titles not provided, assume placeholder values
	title = kwargs.get('title', 'Placeholder Title')
	bar_width=kwargs.get('bar_width', .4)
	opacity=kwargs.get('opacity', .7)
	

	s1_label=kwargs.get('s1_label', 'Series 1')
	s1_color=kwargs.get('s1_color', 'b')

	s2_label=kwargs.get('s2_label', 'Series 2')
	s2_color=kwargs.get('s2_color', 'g')

	y_axis_label=kwargs.get('y_label', 'y-axis')
	x_axis_label=kwargs.get('x_label', 'x-axis')

	#general formatting	
	minor_format=kwargs.get('minor_format','%d\n%a')
	major_format='\n\n\n%b\n%Y'	

	#instance the plot and axes objects - they're fine with a shared y-axis
	fig, ax = plt.subplots(sharey=True)

	#this sets up the y-axis spacing using a numeric version of datatime
	y_locations=dates.date2num(idx)
	
	#spec out each series of bars
	bars1=plt.bar(y_locations, s1, bar_width, alpha=opacity, 
		          color=s1_color, label=s1_label, tick_label=idx)
	
	barsy2=plt.bar(y_locations-bar_width, s2, bar_width, alpha=opacity, 
			color=s2_color, label=s2_label,tick_label=idx)	


	#tell the x-axis to be dates (makes formatting a snap)
	ax.xaxis_date()
	
	#tell the minor tick labels weekdays, then format
	ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=(1),
		                                            interval=1))
	if minor_format:
		ax.xaxis.set_minor_formatter(dates.DateFormatter(minor_format))
	
	#tell major tick labels to be months, then format
	ax.xaxis.set_major_locator(dates.MonthLocator())
	ax.xaxis.set_major_formatter(dates.DateFormatter(major_format))

	#set some gridlines
	ax.xaxis.grid(True, which="minor")
	ax.yaxis.grid()

	#general beautification
	plt.title(title)     
	
	#grab a figure object, set its title and save it to disk
	fig=plt.gcf()
	fig.canvas.set_window_title(title)
	plt.tight_layout()
	plt.savefig(title+'.png')
	#fig.autofmt_xdate()
	plt.show()


if __name__=='__main__'	:
	test_printme=False 
	test_formatPlot2=True
	test_formatPlotBar=True

	if test_formatPlotBar:
		formatPlotBar()	

	if test_formatPlot2:
		formatPlot2()	

	if test_printme:
		printme('one_arg')
		printme('two', 'args')
		printme('three', 'args', 'now')
		printme('four', 'args', 'here', 'now')
