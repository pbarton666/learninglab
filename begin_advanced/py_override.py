#py_override.py

"how to subclass a built-in object and override behavior"
class myint(int):
    def __init__(self, val):
        super().__init__()
        self.val=val

    def __add__(self, other):
        return str(self.val + other) + " Yowza!"

if __name__=='__main__':
    one=myint(1)
    print(one+3)