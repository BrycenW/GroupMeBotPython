#Brycen Wershing
from flask import Flask
import requests
import os
import ast
import time
from inOut import *

'''
def grab_message_number(dirty_string):
	for x in range (0, len(dirty_string)-6):
		if dirty_string[x:x+5] == "count":
			for y in range (x+5, len(dirty_string)-6):
				if dirty_string[y:y+8] == "messages":
					return int(dirty_string[x+7: y-2])

def cleanup_string(dirty_string):
	for x in range (0, len(dirty_string)-8):
			if dirty_string[x:x+4] == "null":
				dirty_string = dirty_string[:x] + "\"\"" + dirty_string[x+4:]
			if dirty_string[x:x+5] == "false":
				dirty_string = dirty_string[:x] + "\"0\"" + dirty_string[x+5:]
			if dirty_string[x:x+4] == "true":
				dirty_string = dirty_string[:x] + "\"1\"" + dirty_string[x+4:]
	for x in range (0, len(dirty_string)-6):
		if dirty_string[x:x+8] == "messages":
			for y in range (x + 12, len(dirty_string)-6):
				if dirty_string[y:y+4] == "meta":
					return dirty_string[x+11: y-4]

def pull_message(seeking_num):
	payload = {"limit":1, "token":"dbce80c042ef0133562d05f0d49317f6"}
	dirty_packet = requests.get("https://api.groupme.com/v3/groups/16326365/messages", params=payload)
	message_number = grab_message_number(dirty_packet.content)
	if message_number < seeking_num:
		return {'count':str(message_number)}
	clean_string = cleanup_string(dirty_packet.content)
	out_dict = eval(clean_string)
	out_dict['count'] = str(message_number)
	return out_dict

def seek(seeking_num):
	return pull_message(seeking_num)


def post(text):
	payload = {"text":text, "bot_id":"7e819111ff8f330b299db0679f"}
	requests.post("https://api.groupme.com/v3/bots/post", params=payload)
'''

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


