#py_except_3.py
import traceback

def another_bad_int():
    try:
        int('b')
    except:
        raise

for func in (another_bad_int, ):
    try:
        func()
    except ValueError as ve:
        print("you have no values\n\n", ve, "\n")
        traceback.print_stack()
        raise
