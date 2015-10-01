from inOut import *

#[[text, previous message, [sender_id... ]]... ]
token = raw_input("Input token: ")
bot_id = raw_input("Input bot_id: ")
group_id = raw_input("Input group_id: ")

def grab_next_message_checkbot(id):
	waiting = 1
	i = 0
	while waiting == 1:
		print("pulling")
		time.sleep(1)
		next_message = pull_next_message(id, token, group_id)
		if (next_message != 1):
			waiting = 0
		i = i + 1
	if next_message['sender_type'] == "bot":
		print "bot"
		return {"sender_type":"bot", "id":next_message["id"]}
	print "acheive"
	return next_message

def combine_items(array, first, second):
	which_name = raw_input("Between " + array[first][0] + " and " +
		array[second][0] + " would you like (f)ormer, (l)atter, or (d)on't combine? Reply f, l, or d?")
	if which_name == "d":
		return array
	elif which_name == "f":
		for i in range (0, len(array[second][2]) - 1):
			array[first][2].append(array[second][2][i])
		del array[second]
	elif which_name == "l":
		for i in range (0, len(array[first][2]) - 1):
			array[second][2].append(array[first][2][i])
		del array[first]
	else:
		print("Fuck your input")
		return combine_items(array, first, second)
	return array

def poll_open_end(name, question):
	working_id = pull_message(0, token, group_id)['id']
	post("Hello eveyone, I am the poll bot, and " + name +
		" wants me ask everyone a question. Only your first reply after this " +
		"message will count, so don't be shitty", bot_id)
	post(question, bot_id)
	full_member_info = get_group_info(group_id, token)["members"]
	print full_member_info
	not_voted_id = []
	print not_voted_id
	print len(full_member_info)
	for i in range (0, len(full_member_info)):
		print "check"
		print i
		not_voted_id.append(full_member_info[i]["user_id"])
	print not_voted_id
	user_responses = []
	for i in range (0, 1000):
		for j in range(0, 1000):
			working_message = grab_next_message_checkbot(working_id)
			if working_message["sender_type"] == "bot":
				working_id = working_message["id"]
			else:
				break
		if "fuck you bot" in working_message["text"]:
			post("I'm fucking off", bot_id)
			return user_responses
		if working_message["sender_id"] in not_voted_id:
			not_voted_id.remove(working_message["sender_id"])
			print working_message["name"] + " said " + working_message["text"]
			user_responses.append([working_message["text"], working_id,
				[working_message["sender_id"]]])
			print str(len(user_responses)) + " people have responded"
			if len(not_voted_id) == 0:
				print "Everyone has voted!"
				return user_responses
			if "n" in raw_input("Would you like to continue getting responses? "):
				return user_responses
		print working_message["sender_id"] + " not in " + str(not_voted_id)
		working_id = working_message["id"]
	return user_responses

def generate_string_from_responses(options):
	string_options = ""
	for i in range (0, len(options)):
		string_options = string_options + " " + str(i) + ": " + str(options[i][0])
	return string_options

def combine_responses(options):
	i, j = 0, 0
	while i < len(options) - 1:
		a_text = options[last_index - i][0]
		b_text = options[last_index - j][0]
		a_text = a_text.lower.replace(" ", "")
		b_text = b_text.lower.replace(" ", "")
		if a_text in b_text or b_text in a_text:
			options = combine_items(options, last_index - i, last_index - j)
			j = j - 1
		if j < len(options):
			j += 1
		else:
			i += 1
			j = i + 1
	print "The responses are " + generate_string_from_responses(options)
	while "y" in raw_input("Would you like to combine any options? "):
			first = int(raw_input("What is the index of one? "))
			second = int(raw_input("What is the index of the other? "))
			combine_items(options, first, second)
	return options

def assure_no_double(array):
	for i in range(0, len(array)):
		to_be_deleted = []
		for j in range(0, len(array[i][2]) - 1):
			for k in range (j + 1, len(array[i][2])):
				if array[i][2][j] == array[i][2][k]:
					to_be_deleted.append(k)
		for l in range(0, len(to_be_deleted)):
			del array[i][2][l]


	return array

def sort_by_votes(dirty_results):
	results = assure_no_double(dirty_results)
	for i in range(0, len(results) - 1):
		for j in range(i, len(results) - 1):
			if len(results[i][2]) < len(results[i][2]):
				temp = results [i]
				results[i] = results [j]
				results[j] = temp
	return results

def consider_likes(results):
	for i in range(0, len(results)):
		results[i][2] = results[i][2] + get_likes(results[i][1], token, group_id)
	return results

def poll():
	name = raw_input("What is your name? ")
	question = raw_input("What question would you like to pose? ")
	if "y" in raw_input("Is this an open ended question? "):
		responses = poll_open_end(name, question)
	else:
		print "more shit to be added later"
		return 0
	if "n" in raw_input("Would you like to consider likes? "):
		return sort_by_votes(combine_responses(responses))
	post("Likes will be considered, so make sure to like your favorites!", bot_id)
	raw_input("Input anything to count likes: ")
	return sort_by_votes(combine_responses(consider_likes(responses)))

def pretty_display(results):
	for i in range(0, len(results)):
		print str(i + 1) + ". " + results[i][0] + " with " + str(len(results[i][2])) + " votes"
	post("The top answer is " + results[0][0] + " with " +
		str(len(results[0][2])) + " votes", bot_id)

pretty_display(poll())
