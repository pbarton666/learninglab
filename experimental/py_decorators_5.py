#py_decorators_5.py

"""Demonstrates 'dog-piling' of multiple decorators.   Here,
   we'll screen to ensure the user is a dog, whether it's an authorized
   user, and whether an object provided supports the '+ operator."""

from functools import wraps

auth_users = ("Fang d'Poodle", "Quinn Husky", "Joe Cool")

def species_ok( func):
    "is the user a dog?"
    @wraps(func)
    def screened( **kwargs):
        if kwargs['species'] != 'dog':
            kwargs['ok'] = False
        return func( **kwargs)
    return screened

def user_ok( func):
    "is this an authorized user?"
    @wraps(func)
    def screened( **kwargs):	
        if kwargs['user'] not in auth_users:
            kwargs['ok'] = False
        return func( **kwargs)
    return screened

def ops_ok( func):
    "does the method provided support '+' operation?"
    @wraps(func)
    def screened( **kwargs):	
        if not '__add__' in dir(kwargs['obj']):
            kwargs['ok'] = False
        return func( **kwargs)
    return screened			

@species_ok
@user_ok
@ops_ok
def process_tests(**kwargs):
    if not kwargs['ok']:
        print('FAIL', '(', kwargs['user'], kwargs['species'], kwargs['obj'], ')')
    else:
        print("Yea!  Success", '(', kwargs['user'], kwargs['species'], kwargs['obj'], ')')
    return kwargs

tests = ({'ok': True,'user': "Fang d'Poodle", 'species': 'dog', 'obj': print},
         {'ok': True,'user': "Fang d'Poodle", 'species': 'dog', 'obj': int},)

for test in tests:
    process_tests( **test)



