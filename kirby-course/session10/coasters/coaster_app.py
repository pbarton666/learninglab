# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:05:10 2017

@author: kurner
"""

from make_coasters_db import DB
from flask import Flask, Response, request
from jinja2 import Environment, PackageLoader
import sys
import json


import os
#sys.path.append("/Users/kurner/Downloads/session10/")
#sys.path.append("/home/pat/workspace/learninglab/kirby-course/session10/")

#fixes "hard path problem" by grabing parent dir and adding a slash
path_elements=os.path.split(os.getcwd())
parent_dir=os.path.sep.join(path_elements[:-1]) + os.path.sep
sys.path.append(parent_dir)

print (os.getcwd())
print(parent_dir)

app = Flask(__name__)

env = Environment(
    loader=PackageLoader('coasters', 'templates'),
)

@app.route("/")
def index():
    template = env.get_template('home.html')
    return template.render()

@app.route("/coasters")
def coasters():
    the_data = all_coasters()
    template = env.get_template('coaster_listing.html')
    return template.render(coasters= the_data)

@app.route("/coaster/<coaster>", methods=["POST", "GET"])
def coaster(coaster):
    if request.method == "POST":
        data = {}
        data['Name'] = coaster # disabled in form, so doesn't come through
        data.update(request.form.to_dict(flat=True))
        try:
            with DB() as db:
                db.update_coaster(data)
        except:
            print("NO CHANGES POSTED")

    # get Coaster, either just modified or coming in from the list
    the_data = list(one_coaster(coaster)[0])
    if "'" in the_data[0]:
        the_data.append(the_data[0].replace("'","*"))
    else:
        the_data.append(the_data[0])
    template = env.get_template('coaster.html')
    return template.render(the_data = the_data)

@app.route("/api/coaster/<coaster>")
def json_coaster(coaster):
    the_data = one_coaster(coaster)
    json_string = json.dumps(the_data[0])
    return Response(response=json_string, status=200, mimetype = "application/json")

@app.route("/update/<coaster>")
def edit_coaster(coaster):
    print("Update: ", coaster)
    the_data = one_coaster(coaster)
    template = env.get_template('update_coaster.html')
    return template.render(the_data = the_data[0])

@app.route("/delete/<coaster>")
def delete_coaster(coaster):
    with DB() as db:
        db.delete_coaster(coaster)
    return coasters()
    
def all_coasters():
    with DB() as db:
        query = ("SELECT name, park, yr_opened FROM Coasters "
                 "ORDER BY name")
        db.get_coasters(query)
        return tuple(db.cursor.fetchall())

def one_coaster(coaster):
    with DB() as db:
        if "'" in coaster:
            coaster = coaster.replace("'", "''")
        if "*" in coaster:
            coaster = coaster.replace("*", "''")
        if "," in coaster:
            coaster = coaster.replace(",", "%")
            coaster=coaster[:coaster.index('%')+1]
        if "%" not in coaster:
            query = ("SELECT * FROM Coasters "
                     "WHERE name = '{}'".format(coaster))
        else:
            query = ("SELECT * FROM Coasters "
                     "WHERE name LIKE '{}'".format(coaster))            
        print("Seeking: ", query)
        db.get_coasters(query)
        return db.cursor.fetchall()


        
if __name__ == "__main__":
    app.run()
    