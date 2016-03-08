#Brycen Wershing
import requests
import os
import ast
import time
from inOut import *

token = raw_input("Input token: ")
bot_id = raw_input("Input bot_id: ")
group_id = raw_input("Input group_id: ")

def check_mess(text):
	print text
	if "kick me" in text.lower():
		print "true"
		return True
	print "false"
	return False

def moderate():
	last_num = 0
	while 1:
		message = pull_message(last_num, token, group_id)
		print message['count']
		if int(message['count']) > last_num:
			print message
			print message['text']
			if check_mess(message['text']):
				kick_member(group_id, message['user_id'], token, group_id)
			last_num = message['count']
		else:
			test()
			time.sleep(1)
			last_num = int(message['count'])

def rerename(user_id, nickname):
	rename_member(bot_id, user_id, token, group_id, nickname)
	last_num = 0
	while 1:
		message = pull_message(last_num, token, group_id)
		print message['count']
		if int(message['count']) > last_num:
			print message
			print message['user_id'] + message['name']
			if str(message['user_id']) == str(user_id) and nickname != message['name']:
				rename_member(bot_id, user_id, token, group_id, nickname)
			last_num = message['count']
		else:
			test()
			time.sleep(1)
			last_num = int(message['count'])