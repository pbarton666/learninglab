
#py_animal_class_v2.py

class Animal:
    
    tricks = ["jumping", "playing dead", 
              "rolling over", "walking backwards"]
    
    def __init__(self, name, species, age, fav_food):
        self.name = name
        self.species = species
        self.__dict__["age"] = age # alternative to self.age = age
        self.fav_food = fav_food
        self.stomach = [ ]

    def __str__(self):
        fstr="Hi, I'm {}, a {} who loves {}!\n"\
             "And I know how to all these things: {}!\n"
        return fstr.format(self.name, self.species,  
                           self.fav_food,
                           " and ".join(self.tricks))

        
    def __repr__(self):
        return "Animal(name={}, species={})".format(self.name, self.species)

#make us a dawg and create an introduction
mypet=Animal("Fang",  "dog", 10, "steak")
print(mypet)

#create a cat
neighbor_cat=Animal("Fluffy",  "cat", 1, "mice")
print(neighbor_cat)

#override an inherited attribute
neighbor_cat.tricks=['tangling yarn', 'throwing kitty litter']

#Change parent then make new child
Animal.tricks=["barf on floor", "shed on your clothes"]
another_cat=Animal("Snarly",  "cat", 100, "rats")
print(another_cat)

print("*****")
#check in on a child with overridden attributes
print(neighbor_cat)
#check in on child with no overrides
print(mypet)