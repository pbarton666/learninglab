
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
        return "Hi!  My name is {}".format(self.name)
        
    def __repr__(self):
        return "Animal(name={}, species={})".format(self.name, self.species)

#make us a dawg and create an introduction
mypet=Animal("Fang",  "dog", 10, "steak")

fstr="Hi, I'm {}, a {} who loves {}!"
print(fstr.format(mypet.name, mypet.species,  mypet.fav_food))

print("And I know how to all these things: {}!".format(" and ".join(mypet.tricks)))
print()



#create a cat
neighbor_cat=Animal("Fluffy",  "cat", 1, "mice")
print(fstr.format(neighbor_cat.name, neighbor_cat.species,  neighbor_cat.fav_food))
print("And I know how to all these things: {}!\n".\
      format(" and ".join(neighbor_cat.tricks)))

#override an inherited attribute
neighbor_cat.tricks=['tangling yarn', 'throwing kitty litter']
#...and we can make a change to this instance
print(fstr.format(neighbor_cat.name, neighbor_cat.species,  neighbor_cat.fav_food))
print("And I know how to all these things: {}!".\
      format(" and ".join(neighbor_cat.tricks)))


#To illustrate class versus objects, we can change the parent
Animal.tricks=["barf on floor", "shed on your clothes"]
#... create new instance
another_cat=Animal("Snarly",  "cat", 100, "rats")
