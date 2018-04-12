import requests
import json

url = 'http://ubuntu4.saluton.dk:8080/web/rest/game'

def login(username, password) -> bool:
	local_url = url + "/login?username={}&password={}".format(username, password)
	result = requests.post(local_url)
	if is_ok_status(result):
		if result.text == username + " logged in successfully.":
			return True
		else:
			return False
	else:
		return False

def logout(username) -> bool:
	local_url = url + "/logout?username={}".format(username)
	result = requests.post(local_url)
	if is_ok_status(result):
		if result.text == username + " logged out successfully.":
			return True
		else:
			return False
	else:
		return False

def get_all_current_usernames() -> list:
	pass

def get_current_user_amount() -> int:
	pass

#def get_logged_in_user() -> 
#	pass

def is_logged_in(username) -> bool:
	pass

#def get_user_with_highest_highscore() -> :
#	pass

def set_user_highscore(username, highscore) -> bool:
	pass

def get_user_highscore(username) -> int:
	pass

#def get_all_logged_in_users_score() -> 
#	pass

#def get_all_users_highscore() -> :
#	pass

def send_email(username, password, subject, msg) -> bool:
	pass

def send_forgot_password_email(username, msg) -> bool:
	pass

def change_user_password(username, oldPassword, newPassword):
	pass

def guess(char) -> bool:
	pass

def reset_score(username) -> bool:
	pass

def reset_game(username) -> bool:
	pass

def get_guessed_chars(username) -> str:
	pass

def get_word(username) -> str:
	pass

def get_life(username) -> int:
	pass

def get_score(username) -> int:
	pass

def is_char_guessed() -> bool:
	pass

def is_game_won() -> bool:
	pass

def is_game_lost() -> bool:
	pass

def is_highscore(username, password) -> bool:
	pass

# TEST
def test() -> str:
	local_url = url + "/test"
	result = requests.get(local_url)
	if is_ok_status(result):
		return result.text
	else:
		return "ERROR: /test"

def is_ok_status(result) -> bool:
	status_code = result.status_code
	if status_code == 200:   # OK
		return True
	elif status_code == 400: # Bad request
		print("ERROR: 400 Bad Request")
		return False
	elif status_code == 401: # Unauthorized
		print("ERROR: 401 Unauthorized")
		return False
	elif status_code == 403: # Forbidden
		print("ERROR: 403 Forbidden")
		return False
	elif status_code == 404: # Not found
		print("ERROR: 404 Not Found")
		return False
	elif status_code == 405: # Method Not Allowed
		print("ERROR: 405 Method Not Allowed")
		return False
	elif status_code == 500: # Internal Server Error
		print("ERROR: 500 Internal Server Error")
		return False
	else:
		return False

print(login("jacno", "xxx"))
