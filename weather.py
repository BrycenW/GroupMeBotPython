#!/usr/bin/env python
# encoding: utf-8

import sys
from argparse import ArgumentParser
from xml.dom import minidom
try:
	from urllib.request import urlopen
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlopen, urlencode


API_URL = "http://www.google.com/ig/api?"

# Gets the current weather from the array of cities (given as strings)
# from the Google Weather API.  Returns an array of dictionaries, one
# for each city, of current conditions.
def get_weather_for_cities(cities):
	weathers = []
	for location in cities:
		url = API_URL + urlencode({"weather": location})
		xml = urlopen(url).read()
		doc = minidom.parseString(xml)

		forecast_information = doc.documentElement.getElementsByTagName("forecast_information")[0]
		city = forecast_information.getElementsByTagName("city")[0].getAttribute("data")

		current_conditions = doc.documentElement.getElementsByTagName("current_conditions")[0]
		temp = current_conditions.getElementsByTagName("temp_f" if args.unit == "F" else "temp_c")[0].getAttribute("data")
		condition = current_conditions.getElementsByTagName("condition")[0].getAttribute("data")
		wind_condition = current_conditions.getElementsByTagName("wind_condition")[0].getAttribute("data")
		humidity = current_conditions.getElementsByTagName("humidity")[0].getAttribute("data")
		conds = { "forecast_information": forecast_information, 
				"city": city, 
				"temp": temp,
				"current_conditions": current_conditions,
				"condition": condition,
				"wind_condition": wind_condition,
				"humidity": humidity
				}
		weathers.append(conds)
	return weathers
