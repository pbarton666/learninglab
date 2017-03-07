#py_function_1.py
def section(title):
    """center in a string 60 wide padded with ="""
    title_length=len(title)
    return "\n{:=^60}\n".format(title.title())

print(section("<<<< local, nonlocal, global variables >>>>"))

# globals
STAR = "Sirius"   # Polaris
Favorites = [ ]
X = 100

def setStar(name):
    global STAR
    STAR = name
    Favorites.append(name)

print("STAR: ", STAR)
setStar("Polaris")
print("STAR: ", STAR)