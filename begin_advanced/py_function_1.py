#py_function_1.py

# Globals namespace 
STAR = "Sirius"   # Polaris
Favorites = [ ]
X = 100

def setStar(name):
    "Local namespace"
    #remove comment to map to global namespace
    #global STAR    
    STAR = name
    Favorites.append(name)

print("STAR: ", STAR)
setStar("Polaris")
print("STAR: ", STAR)