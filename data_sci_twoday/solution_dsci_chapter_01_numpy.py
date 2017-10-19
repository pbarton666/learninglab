#solution_dsci_chapter_01_numpy.py

"""
To celeberate completion of this class, you might have
a party for your geek friends.  Let's say you stock up
with three 12-packs of great beer:

Beer 1:  IPA
Beer 2:  Lagar
Beer 3:  Stout

Each 12-pack has three rows of bottles (call them 1, 2, and 3) and
four "columns" of bottles (call them 1, 2, 3) as well

Represent them in a 3-D ndarray comprised of (100 * beer value) + 
(10 * row value) + (1 * column value).   The array would look like:

Layer 1 (IPA Layer):   Layer 2 (Lagar Layer):    Layer 3 (Stour Layer):
111  112   113  114    211   212   213  214      311   312   313   314   
121  122   123  123    221   222   223  224      321   322   323   324
131  132   133  134    231   232   233  234      331   332   333   334

See if you can strip out these chunks of the array:

- Layer 1 (as above)

- The "middle, bottom" bit of Layer 2:
      222   223
	  232   233
	  
- This "middle row" of Layer 3:
      321   322   323  324
	  
- The middle bottles:
      122   123
	  222   233
	  322   323

"""
"""
111  112   113  114    211   212   213  214      311   312   313   314   
121  122   123  123    221   222   223  224      321   322   323   324
131  132   133  134    231   232   233  234      331   332   333   334
"""
import numpy as np
rows=3; cols=4; layers=3
#stake out some memory using zeros()
arr=np.zeros([layers, rows, cols])
#add each element
for el in range(layers):
	for r in range(rows):
		for c in range(cols):
			arr[el, r, c]=(el + 1) * 100 + (r + 1) * 10 + (c + 1)

IPA=arr[0]
print(IPA)
print()

mid_bottom_layer_2=arr[1, 1:3, 1:3]
print(mid_bottom_layer_2)
print()

mid_row_layer_3 = arr[2, 2, :]
print(mid_row_layer_3)
print()

print(arr)

"""- This "middle row" of Layer 3:
      321   322   323  224
- The middle bottles:
      122   123
	  222   233
	  322   323"""

x=1