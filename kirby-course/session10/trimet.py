# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:34:19 2017

@author: kurner
"""

import os
import os.path
import requests
import xml.etree.ElementTree as ET

PROJECT = "/Users/kurner/Downloads/session10"

if not os.path.abspath(".") != PROJECT:
    os.chdir(PROJECT)
    
#get_url = ("https://developer.trimet.org/ws/V1/trips/tripplanner/"
#           "fromplace/pdx/toplace/zoo/appId/8....")

#r = requests.get(get_url)
#print(dir(r))
#print(r.status_code)
#print(r.text)

ns = {"model":"http://maps.trimet.org/maps/model/xml"}

# root =  ET.fromstring(r.text)

tree = ET.parse("trimet_trip_plan.xml")
root = tree.getroot()

itineraries = root.findall("model:itineraries", ns)

for itinerary in itineraries[0].findall("model:itinerary", ns):
    td = itinerary.find("model:time-distance", ns)
    date  = td.find("model:date", ns).text
    start = td.find("model:startTime", ns).text
    end = td.find("model:endTime", ns).text
    duration = td.find("model:duration", ns).text
    distance = td.find("model:distance", ns).text
    print("----")
    print("Date:", date)
    print("Start Time:", start)
    print("End Time:", end)
    print("Duration:", duration)
    print("Distance:", distance)

    for idx, leg in enumerate(itinerary.findall("model:leg", ns)):
        print("Leg ", idx)
        mode = leg.attrib['mode']
        leg_start, leg_end = "", ""

        td = False
        td = leg.find("model:time-distance", ns)        
        if td and mode !="Walk":
            leg_start = td.find("model:startTime", ns).text
            leg_end   = td.find("model:endTime", ns).text
            
        start_from = leg.find("model:from", ns)
        start_stopId = start_from.find("model:stopId", ns).text
        start_dest = start_from.find("model:description", ns).text

        end_at = leg.find("model:to", ns)
        if mode != "Walk":
            end_stopId = end_at.find("model:stopId", ns).text
            route = leg.find("model:route", ns).find("model:name", ns).text
        else:
            end_stopId = "N/A"
            route = "On foot"
        end_dest = end_at.find("model:description", ns).text


        print("Mode : {}".format(route))
        print("Start: {:8} {:>8} {}".format(leg_start, start_stopId, start_dest))
        print("End  : {:8} {:>8} {}".format(leg_end, end_stopId, end_dest))


        
