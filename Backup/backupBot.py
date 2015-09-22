#Brycen Wershing
from flask import Flask
import requests
import os
import ast
import time
from inOut import *


def analyse_and_output(message):
	text = message['text']
	text = text.lower()
	if text[0:4] == "echo":
		post(text[4:])
	return 0


last_num = 0
while(1):
	message = pull_message(last_num)
	print message['count']
	if int(message['count']) > last_num:
		print message
		analyse_and_output(message)
		last_num = int(message['count']) + 1
	else:
		test()
		time.sleep(.1)
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


