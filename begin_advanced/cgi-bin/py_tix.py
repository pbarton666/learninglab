#!/usr/bin/env python3
import cgi
fields = cgi.FieldStorage()

html=\
"""
<HTML>        
<BODY>
<h3><center>Let's make sure I've got it right</center></h3>
<center>
<form METHOD="post" ACTION="/index.cgi">
	And you are: 
	<br>{} 
	<br>{} 
	<br>... and you like the {}
	<br>
</BODY>
</HTML>
"""
if "firstname" in fields: firstname = fields['firstname'].value
if "lastname" in fields:  lastname = fields['lastname'].value
if "team" in fields:  team = fields['team'].value

print(html.format(firstname, lastname, team))