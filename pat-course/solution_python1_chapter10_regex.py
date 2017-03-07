#solution_python1_chapter10_regex.py

import re

cc="1234-5678-1234-5678"
regex = re.compile(r'''(
(\d{4})   #match 4 digits
(\s*|\-*) #matches either a white space \s or a dash
(\d{4})
(\s*|\-*)
(\d{4})

)''',re.VERBOSE)


#validation:  does it even look like a credit card?
m = regex.match(cc)
if not m:
    print("Sorry, that's not a credit card number")

#if it is, we'll make a substiturion of the first 12 numbers
fixed=re.sub(m.group(), "****-****-****",cc)

print("Success.  Changed {} \n\tto the much safer {}.".format (cc, fixed))
