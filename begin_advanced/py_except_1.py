#py_except_1.py

def bad_int():
    int('a')
def bad_not_defined():
    int(a)
def bad_div():
    1/0
def good():
    print("Hi!")

for func in (bad_int, bad_not_defined, bad_div, good):
    try:
        func()
    except ValueError:
        print("you have no values")
    except TypeError:
        print("Learn how to type")
    except NameError:
        print("You have a horse with no name")
    except ZeroDivisionError:
        pass
    finally:
        print("I'm done.\n")