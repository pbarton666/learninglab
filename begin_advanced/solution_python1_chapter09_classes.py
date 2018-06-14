#solution_python1_chapter09_classes.py

"A module to support Vehicle classes"

import inspect

class Vehicle:
    def __init__(self):
        self.__name__ = "Vehicle"
        self.has_wheels = True

    def __str__(self):
        return "I'm a {}".format(self.__name__)


class MotorVehicle(Vehicle):
    def __init__(self):
        self.__name__ = "MotorVehicle"
        self.has_motor = True

    def __str__(self):
        return "I'm a {}".format(self.__name__)

class Car(MotorVehicle):
    def __init__(self):
        super().__init__()
        self.__name__ = "MotorVehicle"	
        self.wheels = 4
        self.has_AC  =  True

    def __str__(self):
        return "I'm a {}".format(self.__name__)


class MotorCycle(MotorVehicle):

    def __init__(self, fairing_color):
        super().__init__()
        self.__name__ = "MotorCycle"	
        self.wheels = 2
        self.has_fairing = True
        self.fairing_color = fairing_color

    def __str__(self):
        return "I'm a {}".format(self.__name__)

    @property
    def fairing_color(self):
        print("getting fairing color")
        return self.__fairing_color

    @fairing_color.setter
    def fairing_color(self, fairing_color):
        if isinstance(fairing_color, str):
            print("settign fairing color to {}".format(fairing_color))
            self.__fairing_color = fairing_color
        else:
            print("I can't set the fairing color to a {}".format(type(fairing_color)))


def print_class_tree(tree, indent=-1):
    "introspectively look at the class structure"
    if type(tree) == list:
        for branch in tree:
            print_class_tree(branch, indent+1)
    else:
        print ('  ' * indent, tree[0].__name__)
    return

def print_method_resolution_order(this_cls):
    for cls in inspect.getmro(this_cls):
        print(cls)

print("Here's the object hierarchy:")
tree=inspect.getclasstree([MotorCycle, MotorVehicle, Car, Vehicle])
print_class_tree(tree)


mc=MotorCycle(fairing_color="blue")
mc1=MotorCycle(fairing_color=123)
a=1
#print("\n\nHere's the Method Order Resolution (MRO) for {}:".format(mc.__name__))
#print_method_resolution_order(mc)
