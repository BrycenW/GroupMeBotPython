#Brycen Wershing
from flask import Flask
import requests
import os
import ast
import time
from inOut import *
import pywapi


def analyse_and_output(message, bot_id, token, group_id):
	text = message['text']
	text = text.lower()
	count = 0
	if text[0:4] == "echo":
		post(text[4:], bot_id)
		count = count + 1
	if "underground" in text or "under ground" in text:
		post("FUCK THE POLICE", bot_id)
		post("coming straight from the underground", bot_id)
		count = count + 2
	if "weather" in text:
		weath = pywapi.get_weather_from_weather_com('15213', 'imperial')
		if weath['current_conditions']['temperature'] != weath['current_conditions']['feels_like']:
			post("but it feels like" + weath['current_conditions']['feels_like'], bot_id)
			count = count + 1
		if "today" in text:
			post("The high today is " + weath['forecasts'][0]['high'] +
				" and the low is " + weath['forecasts'][0]['low'], bot_id)
			count = count + 1
		elif "tomo" in text:
			post("Tomorrow will be " + weath['forecasts'][1]['day']['text'], bot_id)
			post("The high tomorrow is " + weath['forecasts'][1]['high'] +
				" and the low is " + weath['forecasts'][1]['low'], bot_id)
			count = count + 2
		else:
			post("Today it is " + weath['current_conditions']['text'], bot_id)
			post("It is " + weath['current_conditions']['temperature'] + "F", bot_id )
			count = count + 2
	return count


last_num = 0
token = "dbce80c042ef0133562d05f0d49317f6"
bot_id = "7e819111ff8f330b299db0679f"
group_id = "16326365"
while(1):
	message = pull_message(last_num, token, group_id)
	print message['count']
	if int(message['count']) > last_num:
		print message
		last_num = analyse_and_output(message, bot_id, token, group_id) + int(message['count'])
	else:
		test()
		time.sleep(1)
		last_num = int(message['count'])