#py_csv.py

import csv
fn="py_test_data.csv"

data=[\
      'In the moonlight,',
      'The color and scent of the wisteria',
      'Seems far away.']

with open(fn, 'w') as myfile:
    writer=csv.writer(myfile)
    for line in data:
        writer.writerow([line])
        writer.writerow(line)
    writer.writerow('')
    writer.writerows([data])
    
    
with open(fn, 'r') as myfile:
    rows=csv.reader(myfile)
    for row in rows:
        print(row)
        
x=1        