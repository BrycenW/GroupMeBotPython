import requests
import os
import ast
import time
#Brycen

null = ""
false = "false"
true = "true"

# ------------------------------------------------
# These are the functions available in inOut
# test() prints "you good"
# pull_message(last_number, token, group_id), pulls the newest message,
# 	but only if the message number is more than last_number
# post(text, bot_id)	posts to this bot

# The message is a dictionary which includes the following elements:
# id: the unique indentifier of the message
# count: the index of the number in this group
# group_id: the id number of the group
# text: the text of the message
# favorited_by: a list of the users that favorited the message
# sender_type: the type of sender, should be user for following options
# user_id: the unique id of whoever sent the message
# name: the name of the sender
# -----------------------------------------------

def test():
	print "you good"

def grab_message_number(dirty_string):
	try:
		clean_string = eval(dirty_string)["response"]["count"]
		return int(clean_string)
	except (KeyError, TypeError):
		return 0

def pull_message(seeking_num, token, group_id):
	payload = {"limit":1, "token":token}
	try :
		dirty_packet = requests.get("https://api.groupme.com/v3/groups/" +
			group_id + "/messages", params=payload)
	except requests.exceptions.ConnectionError:
		time.sleep(.5)
		return {'count':str(int(seeking_num))}
	message_number = grab_message_number(dirty_packet.content)
	if message_number < seeking_num:
		return {'count':str(message_number)}
	clean_string = eval(dirty_packet.content)["response"]["messages"]
	out_dict = eval(str(clean_string[0]))
	out_dict['count'] = str(int(message_number))
	return out_dict

def get_group_info(group_id, token):
	payload = {"token":token}
	try :
		dirty_packet = requests.get("https://api.groupme.com/v3/groups/" +
			str(group_id), params=payload)
	except requests.exceptions.ConnectionError:
		time.sleep(1)
		return get_group_info(group_id)
	out_dict = eval(dirty_packet.content)
	return out_dict['response']

def pull_next_message(previous_id, token, group_id):
	payload = {"limit":1, "after_id":previous_id, "token":token}
	try:
		dirty_packet = requests.get("https://api.groupme.com/v3/groups/" +
			group_id + "/messages", params=payload)
	except requests.exceptions.ConnectionError:
		time.sleep(.5)
		return 1
	if "200" not in str(dirty_packet):
		return 1
	out_dict = eval(dirty_packet.content)["response"]["messages"]
	if len(out_dict) == 0:
		return 1
	out_dict = out_dict[0]
	out_dict['count'] = str(grab_message_number(dirty_packet.content))
	return out_dict

def post(text, bot_id):
	payload = {"text":text, "bot_id":bot_id}
	try:
		requests.post("https://api.groupme.com/v3/bots/post", params=payload)
	except requests.exceptions.ConnectionError:
		time.sleep(1)
		post(text)

def get_likes(previous_id, token, group_id):
	message = pull_next_message(previous_id, token, group_id)
	return message["favorited_by"]

def analyse_and_output(message):
	text = message['text']
	text = text.lower()
	if text[0:4] == "echo":
		post(text[4:])
	return 0
