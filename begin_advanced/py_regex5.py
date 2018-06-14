
#py_regex_5.py
import re
re.sub
regex = 'cubs'
change_to = "CUBS"
target = 'If the cubs actually win, will they still be the cubs?'
result = re.sub(regex, change_to, target)

if result:
    print(result)

