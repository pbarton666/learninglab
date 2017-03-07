#!/usr/bin/env python3

#/cgi-bin/solution_python2_chapter05_pizza_script.py


import cgi
fields = cgi.FieldStorage()

STAIRMASTER_CALS_PER_HOUR=800

html=\
    """
    <HTML>
        
        <BODY>
            <h3><center>PAYBACKS!</center></h3>
            <center>
            <form METHOD="post" ACTION="/index.cgi">
                <!--report what was ordered-->
                {}
                <br><br>
                <!--and gym time-->
                And it'll cost you {} hours at the gym.
            </form>
        </BODY>
    </HTML>
    """
#for ease of maintenance, make a dict of ingredients and calories
cal_dict={"crust":   {'Whole wheat':300,
                     'Traditional': 250,
                     'Deep-dish':   400},
          'cheese':  {'mozzarella': 200,
                      'cheddar':    210,
                      'soy':        150},
          'meat':    {'no meat':    100,
                      'pepperoni':  200,
                      'ham':        220},
          'beverage':{'beer':       225,
                      'cola':       180,
                      'orange':     190}
          
          }

#gather all incredients - count calories and make a report
#  as we go.

report="You ordered a pizza with:<br>"
calories=0

for group in ('crust', 'cheese','meat', 'beverage'):
    choices=fields.getlist(group)           #reads the value(s)
    for choice in choices:
        report+="<br>&nbsp{}<br>".format(choice)
        calories+=cal_dict[group][choice]   #drills into dict

gym_hours=round(calories/STAIRMASTER_CALS_PER_HOUR, 1)

print(html.format(report, gym_hours))
