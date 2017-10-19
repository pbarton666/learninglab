#py_utilities_parse_signature.py
"grab a complicate method signature and turn it into a table"
"   for inclusion in teaching materials"
sig=\
"""
filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=False, error_bad_lines=True, warn_bad_lines=True, skipfooter=0, skip_footer=0, doublequote=True, delim_whitespace=False, as_recarray=False, compact_ints=False, use_unsigned=False, low_memory=True, buffer_lines=None, memory_map=False, float_precision=None
"""
#we'll print out 'cols' columns of arguments
cols=3
skip_positionals=1
args=sig.split(',')
ls=[]
for a in args:
	ls.append(a.strip())
cix=-1   #columns index
stg=''
for e in ls[skip_positionals:]:
	if cix == 2:
		stg+= e+'\n'
		cix=0
	else:
		stg+=  e+'\t'
		cix+=1
print(stg)		
	