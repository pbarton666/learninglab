#py_named_tuples.py
from collections import namedtuple

print("\n{:=^40}".format("< NAMED TUPLES >"))

Piece = namedtuple('Piece', 'type color position symbol')

grid = []
for r in range(8):
    grid.append([None, None, None, None, 
                      None, None, None, None])

grid[7] = [  
            Piece("Rook"   , "black", [7,0], "R"),
            Piece("Knight" , "black", [7,1], "K"),
            Piece("Bishop" , "black", [7,2], "B"),
            Piece("Queen"  , "black", [7,3], "Q"),
            Piece("King"   , "black", [7,4], "K"),
            Piece("Bishop" , "black", [7,5], "B"),
            Piece("Knight" , "black", [7,6], "K"),
            Piece("Rook"   , "black", [7,7], "R") ]

grid[6] = [ ]
for c in range(8):
    p=Piece("Pawn", "black", [6,c], "P")
    grid[6].append(Piece("Pawn", "black", [6,c], "P"))
    
for p in grid[7]:
    print(p.symbol, end="")
print()
for p in grid[6]:
    print(p.symbol, end="")
print()    

