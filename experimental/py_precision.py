#py_precision.py

"""A brief foray into the precision available with different numeric
   data types and some Python libraries you can use to wrangle them."""

#floats controlled by hardware; accurate to nearest binary value
print("simple addition: {} + {} + {} = {}".\
      format(.1, .1, .1,
             .1 + .1 + .1))
print()

#another example - these two are the same in binary
a = .1
b =  0.10000000000000001
print("does {} = {:.23f}?   {}".\
      format(a, b, a == b))
print()

#one solution:  store as a fraction
print("as fraction: {} + {} + {} = {}".\
      format(a, a, a,  (a + a + a).as_integer_ratio()))

print()
#better yet, use fractions library
import fractions
a = fractions.Fraction(1, 10)
print("using fractions.Fraction: {} + {} + {} = {}".\
      format(a, a, a,  (a + a + a)))

print()
#or use the decimal library
import decimal

#Accuracy is baked in when the (immutable) number is defined.

#   The accuracy is implied by the number of decimal places provided.
a = decimal.Decimal(".111111111111111111111111111111111111111111111111111111111111111111111"
                    "11111111111111111111111111111111111111111111111111111111111111111111"
                    "11111111111111111111111111111111111111111111111111111111111111111111"
                    "11111111111111111111111111111111111111111111111111111111111111111111"
                    "11111111111111111111111111111111111111111111111111111111111111111111"
                    "11111111111111111111111111111111111111111111111111111111111111111111")

#the 'context' is used to specify how much precision will be used in operations
decimal.getcontext().prec = 600
print("using decimal.Decimal:\n{}\n+\n{}\n+\n{}\n=\n{}".\
      format(a, a, a,
             a + a + a))

#and you can always 'sqeeze it down' into a fixed precision
print()
quant_num =  a.quantize(decimal.Decimal('0.001'))
print("quantized:  a = {}".format(quant_num))

print()

#Integers are inherently accurate.  There is no theoretical size limit
# except practical (system constrained).  How big?
import sys

print("maximum Python integer supported on this box: {}".format(sys.maxsize))

print()
#In numpy (scipy) different object types have different limitations
import numpy
print("numpy integers available on this box:")
for dtype in numpy.sctypes['int']:
	info =  numpy.iinfo(dtype)
	print("dtype: {}  max: {}".format(info.dtype, info.max))
