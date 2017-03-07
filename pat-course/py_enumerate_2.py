#py_enumerate_2.py

fruits=('apple', 'banana', 'kiwi')
start_at=1
for snack, index in enumerate(fruits, start_at):
    print('fruit #{} is a(n) {}'.format(snack, index))



