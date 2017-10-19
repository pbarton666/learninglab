import pickle

fn='my_lda_model.pkl'
#reconstitute the Python object
with open(fn, 'rb') as f:
	model=pickle.load(f)
	
print(model)
z=1