#py_fuzzy_lookup.py

"""This demonstrates how one might do a 'fuzzy lookup' to find approximate matches"""

from fuzzywuzzy import process

def do_fuzzy_lookup(item_to_find = None, using_this = None, threshhold = 75):
    "tries to find a fuzzy match with fuzzywuzzy library"
    from fuzzywuzzy import process
    finding =  process.extractOne(item_to_find, using_this)
    matcher = finding[0]
    score = finding[1]
    if score > threshhold:
        return matcher

player = 'HeNDricks'    
possible_matchers = ['Chatwood', 'Farrell', 'Hendricks', 'Lester']
threshold = 75      

do_fuzzy_lookup(item_to_find = player, using_this=possible_matchers, threshhold=threshhold)