# py_pascal.py

"""
Another example of a Python generator.

Starting with any row, say [1, 1]
    
Put [0] on the left : [0, 1, 1]
 ...and on the right: [1, 1, 0] +
                      ---------
Add vertically        [1, 2, 1]

... and repeat.

"""

def pascal():
    row = [1]
    while True:
        yield row
        # zipping to give "vertical" pairs, then added
        row = [i+j for i, j in zip(row + [0], [0] + row)]
    
def main():    
    p = pascal()
    for _ in range(10):
        print(next(p))
        
if __name__ == "__main__":
    main()
    