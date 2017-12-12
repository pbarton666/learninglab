#py_numpy.py
import numpy as np

#auto creation possible
b=np.ones(3)   
print(b)

#instantiate from a list
b = np.array([ 1.,  1.,  1.])
print(type(b[1]))
print(type(b))
print(b.shape)
print()

a=np.array([1,2,3])
print(a)
print(type(a))

#create an array from a container; these all work
d=np.array([(0,1,2,3), (10,11,12,13),(20,21,22,23)])
d=np.array([[0,1,2,3], [10,11,12,13],[20,21,22,23]])
d=np.array(((0,1,2,3), (10,11,12,13),(20,21,22,23)))
print(d.__repr__())
print()

#introspect
shape=d.shape
print('shape is: {}'.format(shape))
dims=d.ndim
print('dimension(s):  {}'.format(dims))


#get the second row, then an element from that row
row=d[1]
print(row.__repr__())

element=d[1][1]
print(element.__repr__())
print(type(element))
print()

#get a column then 2-D selections
col=d[:,1]
print(col.__repr__())
print()

#pick off the top, left corner
top_left_chunk=d[:2,0:3]
print(top_left_chunk.__repr__())
print()

#bottom element
bottom_corner=d[-1, -1]
print(bottom_corner.__repr__())
print()

#skip columns
skip_cols=d[:,::2]
print(skip_cols)
print()

#slice objects work
row_slice=slice(0,2)
col_slice=slice(0,3)
top_left_chunk=d[row_slice, col_slice]
print(top_left_chunk.__repr__())
print()

#deep versus shallow copies
e=d
print('I did:  e=d   Did I fail to copy it? {}'.format(id(d)==id(e)))
e=d[:]
print('I did:  e=d[:]   Did I fail to copy it? {}'.format(id(d)==id(e)))
print()

print(col.__repr__())
col[1]=777
print(col.__repr__())
print()
print(d)

#scalar / element-wise operations
d=np.array(((0,1,2,3), (10,11,12,13),(20,21,22,23)))
print()
print(d+100)
print()
print(d)
print()

#need to reassign name to make it stick
print('reassigining')
d=d+100
print(d)
print()

#making a mask
print("select odd values")
mask= d % 2
print(mask)
print()
print( d * mask)
print()

#vectorizing an array
print("turn into vector")
e = d.ravel()
print(e)
print()
iter_version = d.flat
print('first element:', next(iter_version))
print()

#reshaping operations
print("reshape")
new_rows=4
new_cols= len(e) // new_rows
e = e.reshape(new_rows, new_cols)
print(e)
print()

#resizing operations
print("resize to reduce")
e=np.resize(e, (2,2))
print(e)
print()

print("resize to expand using numpy.resize()")
e=np.resize(e, (4,4))
print(e)
print()

print("resize to expand using array method")
k=np.array([(1,2,3)])
print(k)
print()
k.resize((3,3))
print(k)
print()

#references can block resizing
k.resize((1,2))
print(k)
zebra=k
try: k.resize(2,2)
except ValueError:
	print('failed resize due to reference')
	k.resize(2,2, refcheck=False)
print(k)
print()

#descriptive stats
d=np.array([(6, 3, 8), (20,1,80), (4, 3, 34)])
print('min {:10}'.format(d.min()))
print('max {:10}'.format(d.max()))
print('sum {:10}'.format(d.sum()))
print('std {:10}'.format(d.std()))
print('mean {:10}'.format(d.mean()))
print('diagonal {:10}'.format(str(d.diagonal())))
print('trace {:10}'.format(str(d.trace())))
print()

#sorting arrays
d=np.array([(6, 3, 8), (20,1,80), (4, 3, 34)])
print(d)
print("\nsorted on axis 0")
d.sort(0)
print("\nsorted on axis ")
d.sort(1)
print(d)
print()

#build a stack of 2-D arrays; element: top 3.xx, mid 2.xx, btm 1.xx
top=np.empty( (3,3));mid=np.empty( (3,3));btm=np.empty( (3,3))
for arr, valbase in zip( (top, mid, btm), (3,2,1)):
	for row in range(arr.shape[0]):
		for col in range(arr.shape[1]):
			arr[row, col]=np.random.random()+valbase
box=np.array( (top, mid, btm))
print(box)
print()
print(box[1, :, :])  #the middle layer
print()
print(box[1, 1, :])  #the middle row from the middle layer
print(box[1, :, 1])  #the middle col from the middle layer
print(box[1, 1, 1])  #the middle element, middle row, middle layer
print()

#alternative ways to create an array

#identity matrix, 3x3, 32-byte wide integer elements
c=np.eye(3, dtype=np.int32)  
print(c)
print(c.shape)
print()

#these all work (review)
y = np.empty ( (2,2) )  #tuple
y.fill(4)
print(y)
print()

y =np.ones( (1, 2))     #tuple
print(y)
print()

y = np.zeros ((1,2))
print(y)
print()

y = np.random.rand (1,2) #*not* a tuple
print(y)
print()

#building arrays with file system objects
dtype=np.dtype( 'int, int, int')
d=np.array([(6, 3, 8), (20,1,80), (4, 3, 34)], dtype=dtype)
fn='junk.npy'
d.tofile(fn)
new_d=np.fromfile(fn, dtype=dtype)
print(new_d)
print()

#using binary (pickle) storage
np.save(fn, d)
d = None    #just to prove it works
d = np.load(fn)
print(d)
print()

#create an array from an iterable object
print(np.fromiter([i for i in range(10000)], dtype=np.int))
count=10000
print(np.fromiter([i for i in range(count)], dtype=np.int, count=count))
print()

#array arithmetic
a=np.array([ [1,2], [3,4]])
b=np.array([ [10,20], [30,40]])
print(a+b)
print()
print(a-b)
print()
print(a*b)
print()
print(np.sin(a)*abs(np.sin(b)))

#"real" multiplication with dot()
c=np.array((10,10))
print(a); print()
print(c); print()
print(a.dot(c))
print()
print(c.dot(a))

#transposition
print(a)
print(a.T)
print(a.T.T.T.T)


#==================
dtype='|S4, c8, f16, int32'
data=("hello", complex(1,2), 4.3, 6)
g=np.array(data, dtype=dtype)
print(g)

h=np.array( [ ("hello", 23), ('goodby', 45) ], dtype='object, int32')
print(h.__repr__())
h=np.array( ("hello", 23), dtype='object, int32')
x=1
