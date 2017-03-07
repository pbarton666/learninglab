#py_decorators.py

def big_fish(input_function):
    print ("Yum.  I just ate a {}".format(input_function()))

@big_fish			  
def little_fish():
    user_input=input("Please type something:  ") 
    return user_input



	
