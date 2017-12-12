# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:23:45 2017

@author: Kirby Urner

Example of the "Where's Waldo" genre:
https://i.ytimg.com/vi/SiYrSYd7mlc/maxresdefault.jpg

Extract "Waldo" from each data structure

"""

data = {"id:":["Joe", "Smith"],
        "mother": ["Judy", "Smith"],
        "father": ["Waldo", "Smith"]}
       
print(data['father'][0]) # output "Waldo"

data = {"Waldo": {"scores":[34,56,23,98,89]}}

print(list(data.keys())[0]) # output "Waldo" hint: dict.keys()

data = {(1,2):{"Name":["Waldeen", "Smith"]},
        (4,5):{"Name":["Waldorf", "Smith"]},
        (9,0):{"Name":["Waldo", "Smith"]}}

print(data[(9,0)]["Name"][0]) # output "Waldo" hint: tuples may be keys
first, last = data[ (9,0) ] ["Name"]
print(first)
data = ["Joe", 3, 7, ["dog", ("cat", "Waldo")], 27, {}]

print(data[3][1][1]) # output "Waldo'

# Exercises

##data = {[], [], ()}
data = [[], [], ()]
data[1].append("Wendy")
data[1].append("Waldo")
data[1].append("Willow")
# where's Waldo?
waldo = None # <your answer>