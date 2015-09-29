from flask import Flask
import requests
import os
import ast
import time

null = ""
false = "false"
true = "true"

def test():
	print "you good"

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
	try :
		dirty_packet = requests.get("https://api.groupme.com/v3/groups/16326365/messages", params=payload)
	except requests.exceptions.ConnectionError:
		time.sleep(.5)
		return {'count':str(seeking_num)}
	message_number = grab_message_number(dirty_packet.content)
	if message_number < seeking_num:
		return {'count':str(message_number)}
	clean_string = cleanup_string(dirty_packet.content)
	out_dict = eval(clean_string)
	out_dict['count'] = str(message_number)
	return out_dict

def get_group_info(group_id):
	payload = {"token":"dbce80c042ef0133562d05f0d49317f6"}
	try :
		dirty_packet = requests.get("https://api.groupme.com/v3/groups/" + str(group_id), params=payload)
	except requests.exceptions.ConnectionError:
		time.sleep(1)
		return get_group_info(group_id)
	out_dict = eval(dirty_packet.content)
	return out_dict['response']

def pull_next_message(previous_id):
	payload = {"limit":1, "after_id":previous_id, "token":"dbce80c042ef0133562d05f0d49317f6"}
	try:
		dirty_packet = requests.get("https://api.groupme.com/v3/groups/16326365/messages", params=payload)
	except requests.exceptions.ConnectionError:
		time.sleep(.5)
		return 1
	if "200" not in str(dirty_packet):
		return 1
	#clean_string = cleanup_string(dirty_packet.content)
	out_dict = eval(dirty_packet.content)["response"]["messages"]
	if len(out_dict) == 0:
		return 1
	out_dict = out_dict[0]
	out_dict['count'] = str(grab_message_number(dirty_packet.content))
	return out_dict

def seek(seeking_num):
	return pull_message(seeking_num)

def post(text):
	payload = {"text":text, "bot_id":"7e819111ff8f330b299db0679f"}
	try:
		requests.post("https://api.groupme.com/v3/bots/post", params=payload)
	except requests.exception.ConnectionError:
		time.sleep(1)
		post(text)

def get_likes(previous_id):
	message = pull_next_message(previous_id)
	return message["favorited_by"]


def analyse_and_output(message):
	text = message['text']
	text = text.lower()
	if text[0:4] == "echo":
		post(text[4:])
	return 0