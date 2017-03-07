# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:34:19 2017

@author: kurner
"""

import requests
import xml.etree.ElementTree as ET

get_url = "https://developer.trimet.org/ws/V1/trips/tripplanner/fromplace/pdx/toplace/zoo/appId/8008437301659A246AC8D08A5"

r = requests.get(get_url)
print(r.status)
print(r.text)

tree =  ET.parse(r.text)

root = tree.getroot()