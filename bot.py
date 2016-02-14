#Brycen Wershing
import requests
import os
import ast
import time
from inOut import *
from weather import *


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
		weath = pywapi.get_weather_from_weather_com(['Pittsburgh'])[0]
		post("Today it is " + weath['temp'], bot_id)
		post("It is " + weath['temp'] + "F", bot_id )
		count = count + 2
	return count


last_num = 0
token = raw_input("Input token: ")
bot_id = raw_input("Input bot_id: ")
group_id = raw_input("Input group_id: ")
while 1:
	message = pull_message(last_num, token, group_id)
	print message['count']
	if int(message['count']) > last_num:
		print message
		last_num = analyse_and_output(message, bot_id, token, group_id) + int(message['count'])
	else:
		test()
		time.sleep(1)
		last_num = int(message['count'])
