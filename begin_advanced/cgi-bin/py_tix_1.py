#!/usr/bin/env python3

#/cgi-bin/py_tix_1.py

import cgi
fields = cgi.FieldStorage()

html=\
    """
    <HTML>
        
        <BODY>
            <h3><center>OK, You're going to have fun!</center></h3>
            <center>
            <form METHOD="post" ACTION="/index.cgi">
                Your name is {} {}.
                <br>
                You're going to pay by {}.
                <br>
                And you're going to see the {} play in {} seats.
                <br>
                You plan to consume {}.
                <br><br>
                Enjoy the game!
            </form>
        </BODY>
    </HTML>
    """

if "payment" in fields:
    payment = fields['payment'].value
if "foodbev" in fields:
    foodbev =" and ".join(fields.getlist('foodbev'))
    
if "firstname" in fields:
    firstname = fields['firstname'].value   
if "lastname" in fields:
    lastname = fields['lastname'].value  
if "team" in fields:
    team = fields['team'].value  
if "seating" in fields:
    seating = fields['seating'].value     

print(html.format(firstname, lastname, payment, team, seating, foodbev, payment))
