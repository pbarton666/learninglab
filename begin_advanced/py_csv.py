#py_csv.py

"""how to use the csv library to read a file"""

import csv

fn="py_baseball_data.csv"
with open(fn, 'r') as myfile:
    rows=csv.reader(myfile)
    for row in rows:
        print(row)