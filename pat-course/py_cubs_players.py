#py_cubs_players.py
players={225:('Jake', 'Arrieta'),
         234:('Jake', 'Buchanan'),
         240:('Trevor', 'Cahill')
         }
print(players)

players={"Arrieta": ("Jake", 225),
         "arriETTA": ("Jake", 225),
         "arrieta": ("Jake", 225),
         }

"""

I just hired a new admin and it did not work so well.  I asked her ot organize
my Cubs player database in Python dictionaries.  It turned out to be a disaster.  
After she quit, I found two versions of the database both in terrible shape.

One version uese the player's weights as the key.  I'll spare the details but it 
looked like this.

Can you find a way, working only wiht the code and this dict, to produce a nicely
formatted table that's sorted by the players' last name?

The other version was slightly better.   It was organized by last name - sort of.
There were lots of duplications caused by bad typing.  Here's a bit of it:

Can you find a way to print a nice table of de-duplicated player information 
using the set object?

"""