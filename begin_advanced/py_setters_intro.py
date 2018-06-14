"A quick introduction to getters and setters"

class A:
    def __init__(self, color="blue"):
        self.__name__="I am class A"
class B:
    def __init__(self, color='white'):
        super().__init__()
        print("Class B here." )
        self.color=color
        print("Class B here.  My color is {}".format(self.color))

    @property
    def color(self):
        print("returning a color")
        return self.__some_color

    @color.setter
    def color(self, color):
        print("setting a color")
        self.__some_color=color

b=B('orange')
