import re
import requests

# Sending Message to bot users

with open("users.txt", "r", encoding="utf-8") as file:
	lines = file.readlines()
	url = "https://api.telegram.org/bot<Token>/"
	count = 0
	for line in lines:
		result = re.search(r'[0-9]+', line) # Searching for chat_id
		message = """ <Message> """ # The message that will send to the users
		params = {"chat_id": result[0], "text": message}
		response = requests.post(url + "sendMessage", data=params)
		print("\n")
		print(response)
		print(f"The message has been send to id={result}")
		count += 1
	print(count)
