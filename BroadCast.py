import re
import requests

# Sending Message to bot users

with open("users.txt", "r", encoding="utf-8") as file:
	lines = file.readlines()
	url = "https://api.telegram.org/bot<Token>/"
	count = 0
	Error = 0
	for line in lines:
		result = re.search(r'[0-9]+', line)  # Searching for chat_id
		message = """ <Message> """  # The message that will send to the users
		params = {"chat_id": result[0], "text": message}
		response = requests.post(url + "sendMessage", data=params)
		if response.status_code == 200:
			print(response.status_code)
			print(f"The message has been send to id={result}")
			count += 1
		else:
			print(response.status_code)
			print(f"Error to send message to id={result}")
			Error += 1
	print("\n")
	print(f"Success={count}")
	print("\n")
	print(f"Error={Error}")
	print("\n")
