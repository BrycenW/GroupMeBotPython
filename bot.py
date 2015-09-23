#Brycen Wershing
from flask import Flask
import requests
import os
import ast
import time
from inOut import *
import pywapi


def analyse_and_output(message):
	text = message['text']
	text = text.lower()
	count = 0
	if text[0:4] == "echo":
		post(text[4:])
		count = count + 1
	if "underground" in text or "under ground" in text:
		post("FUCK THE POLICE")
		post("coming straight from the underground")
		count = count + 2
	if "weather" in text:
		weath = pywapi.get_weather_from_weather_com('15213', 'imperial')
		if weath['current_conditions']['temperature'] != weath['current_conditions']['feels_like']:
			post("but it feels like" + weath['current_conditions']['feels_like'])
			count = count + 1
		if "today" in text:
			post("The high today is " + weath['forecasts'][0]['high'] + " and the low is " + weath['forecasts'][0]['low'])
			count = count + 1
		elif "tomo" in text:
			post("Tomorrow will be " + weath['forecasts'][1]['day']['text'])
			post("The high tomorrow is " + weath['forecasts'][1]['high'] + " and the low is " + weath['forecasts'][1]['low'])
			count = count + 2
		else:
			post("Today it is " + weath['current_conditions']['text'])
			post("It is " + weath['current_conditions']['temperature'] + "F" )
			count = count + 2
	return count


last_num = 0
while(1):
	message = pull_message(last_num)
	print message['count']
	if int(message['count']) > last_num:
		print message
		last_num = analyse_and_output(message) + int(message['count'])
	else:
		test()
		time.sleep(1)
		last_num = int(message['count'])


def antiquated():
	payload = {"limit":1, "token":"dbce80c042ef0133562d05f0d49317f6"}
	r = requests.get("https://api.groupme.com/v3/groups/16326365/messages", params=payload)
	temp = r.content
	for x in range (0, len(temp)-6):
		if temp[x:x+5] == "count":
			for y in range (x+5, len(temp)-6):
				if temp[y:y+8] == "messages":
					mes_id = temp[x+7: y-2]
					print mes_id
	if last_num != int(mes_id):
		for x in range (0, len(temp)-6):
			if temp[x:x+4] == "null":
				temp = temp[:x] + "\"\"" + temp[x+4:]
			if temp[x:x+5] == "false":
				temp = temp[:x] + "\"0\"" + temp[x+5:]
		for x in range (0, len(temp)-6):
			if temp[x:x+8] == "messages":
				for y in range (x + 12, len(temp)-6):
					if temp[y:y+4] == "meta":
						temp = temp[x+11: y-4]
		message = eval(temp)
		print message['text']
		
		payload = {"text":message['text'], "bot_id":"7e819111ff8f330b299db0679f"}
		r = requests.post("https://api.groupme.com/v3/bots/post", params=payload)
		last_num = int(mes_id) + 1