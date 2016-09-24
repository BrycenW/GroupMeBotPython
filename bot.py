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
	if "fuck" in text:
		post("potato salad", bot_id)
		count = count + 1
	if "weather" in text:
		weath = weather.get_weather_from_weather_com(['Pittsburgh'])[0]
		post("Today it is " + weath['temp'], bot_id)
		post("It is " + weath['temp'] + "F", bot_id )
		count = count + 2
	return count

def count_all_likes(token,group_id):
	message = pull_message(0, token, group_id)
	like_totals = {}
	count = 0
	user_names = {}
	while message != 1:
		if message["user_id"] not in like_totals:
			like_totals[message["user_id"]] = 0
			user_names[message["user_id"]] = message["name"]
		like_totals[message["user_id"]] += len(message["favorited_by"])
		count += 1
		message = pull_prev_message(message["id"], token, group_id)
	return { "user_likes" : like_totals, "user_name" : user_names, "message_count" : count}






last_num = 0
auth = open("auth.txt", "r")
token = auth.readline()
bot_id = auth.readline()
group_id = auth.readline()
auth.close


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
