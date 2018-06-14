#py_numpy_1.py

"""a snake-charming application"""

from PIL import Image
import numpy as np
import os
idir =os.getcwd() 

iname= 'im3.png'# 'white_snake.PNG'
saveas='new_snake.PNG'

#sets up an array for pixel processing
white=np.array([255,255,255,0]) #r, g, b, a
transparent = np.array([0, 0, 0, 0])
background = white

#open the image and convert it
raw_image = Image.open(iname)
converted_image = raw_image.convert('RGBA')
raw_image.close()
h, w = converted_image.size
converted_histo=converted_image.histogram()
converted_colors=converted_image.getcolors(w*h)

#dump the data into a numpy array and split the channels "bands"
data = np.array(converted_image) # h * w * 4 array (rgba)
r, g, b, a = data.T

#this sets the masking condition and replaces the background color
replace = (r == background[0]) & (b == background[1]) & (g == background[2])
data[replace.T] = (0,0,0,0)

#generate a new image, grab some stats, and save it.
new_image = Image.fromarray(data, 'RGBA')
h, w = new_image.size
new_histo=new_image.histogram()
new_colors=new_image.getcolors(w*h) #a list of tuples [count (rgba), ...]
new_image.save(saveas)
recovered_image = Image.open(saveas)
h, w = recovered_image.size
recovered_histo=recovered_image.histogram()
recovered_colors=recovered_image.getcolors(w*h) #a list of tuples [count (rgba), ...]

#strategy: make a list of color bins we expect to find. These will have pixel ranges
# that are human-friendly e.g., 'brownish', 'gold'. Each spec within the bin can be
# additively applied to a mask - functionally reducing the color palette.

reduced_image = recovered_image.convert('P', palette=Image.ADAPTIVE, colors=10)
reduc1 = reduced_image = recovered_image.convert('P', palette=Image.ADAPTIVE, colors=10)

reduc2 = reduc1.convert('RGB') #turns it to rgb

#save the image in a couple formats
reduc_fn = 'scratch.BMP'
reduc2.save(reduc_fn)

reduced_histo=reduced_image.histogram()
reduced_colors=reduced_image.getcolors(w*h) #a list of tuples [count (rgba), ...]
reduced_image.save(saveas+'reduced.BMP')

#now show them
recovered_image.show()
reduced_image.show()
recovered_image.close()