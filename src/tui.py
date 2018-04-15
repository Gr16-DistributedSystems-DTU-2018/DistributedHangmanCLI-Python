import os
import json

PROMPT_SYMBOL = '» '

clear = lambda: os.system('cls')

def print_startscreen():
	menu_text = """
┌─────────────────────────────────────────────────────────────────────────────┐  
│    ____  ___  ____  _____  ____   ___  ____   _   _  _____  _____  ____     │
│   |  _ \|_ _|/ ___||_   _||  _ \ |_ _|| __ ) | | | ||_   _|| ____||  _ \    │
│   | | | || | \___ \  | |  | |_) | | | |  _ \ | | | |  | |  |  _|  | | | |   │
│   | |_| || |  ___) | | |  |  _ <  | | | |_) || |_| |  | |  | |___ | |_| |   │
│   |____/|___||____/  |_|  |_| \_\|___||____/  \___/   |_|  |_____||____/    │
│             _   _     _     _   _   ____  __  __     _     _   _            │
│            | | | |   / \   | \ | | / ___||  \/  |   / \   | \ | |           │
│            | |_| |  / _ \  |  \| || |  _ | |\/| |  / _ \  |  \| |           │
│            |  _  | / ___ \ | |\  || |_| || |  | | / ___ \ | |\  |           │
│            |_| |_|/_/   \_\|_| \_| \____||_|  |_|/_/   \_\|_| \_|           │
└─────────────────────────────────────────────────────────────────────────────┘
                """
	print(menu_text)

def print_menu(users_online, user):
	user_str = '│ User: Not Logged In                │'

	if user != None:
		user_str = '│ User: {} {}'.format(user['fornavn'], user['efternavn'])

	user_str = trim_str(user_str, 36, True)

	print('┌────────────────────────────────────┐')
	print('│   Welcome to Distributed Hangman!  │')
	print('├────────────────────────────────────┤')
	print('│ Users online: {}                    │'.format(users_online))
	print(user_str) 
	print('├────────────────────────────────────┤')
	print('│             Main Menu              │') # 36 chars in length
	print('├────────────────────────────────────┤')

	if user == None:
		print('│ (q) Log In                         │')
		print('│                                    │')

	if user != None:
		print('│ (w) Log Out                        │')


	if user == None:
		print('│ (d) Forgot Password                │')

	if user != None:
		print('│ (e) User Information               │')
		print('│                                    │')
		print('│ (r) Play                           │')
		print('│ (t) Lobby                          │')
		print('│ (a) High Scores                    │')
		print('│                                    │')
		print('│ (s) Send Email                     │')
		print('│ (f) Change Password                │')
	
	print('│                                    │')
	print('│ (g) About                          │')
	print('│ (x) Exit                           │')
	print('└────────────────────────────────────┘')

def print_hangman(name, life, score, word, used_chars):
	hangman_list = ['0', '/', '|', '\\', '/', '\\']

	hangman_show_list = []

	life_lost = 6 - life

	for i in range(0, 6):
		if i < life_lost:
			hangman_show_list.append(hangman_list[i])
		else:
			hangman_show_list.append(' ')
	
	name_str = trim_str(name, 10, False)
	life_str = trim_str(str(life), 1, False)
	score_str = trim_str(str(score), 7, False)

	word_str = trim_str(word, 28, False)
	used_chars_str = trim_str(used_chars, 28, False)

	print('┌──────────────────────────────┐')
	print('│      Distributed Hangman     │')
	print('├──────────────────────────────┤')
	print('│ Name:  {}  ┌────┐    │'.format(name_str))
	print('│ Life:  {}           │    {}    │'.format(life_str, hangman_show_list[0]))
	print('│ Score: {}     │   {}{}{}   │'.format(score_str, hangman_show_list[1], hangman_show_list[2], hangman_show_list[3]))
	print('│                    │   {} {}   │'.format(hangman_show_list[4], hangman_show_list[5]))
	print('│                    ┴         │')
	print('│                              │')
	print('│ {} │'.format(word_str))
	print('│ {} │'.format(used_chars_str))
	print('└──────────────────────────────┘')

def print_unknown_cmd():
	print('┌──────────────────────────────┐')
	print('│        Unknown Command       │')
	print('├──────────────────────────────┤')
	print('│ The entered command was not  │')
	print('│ recognized! Please use one   │')
	print('│ of the valid commands seen   │')
	print('│ on the menu.                 │')
	print('└──────────────────────────────┘')

def print_login_prompt():
	print('┌──────────────────────────────┐')
	print('│            Log In            │')
	print('├──────────────────────────────┤')
	print('│ Please enter your username   │')
	print('│ and password to log in.      │')
	print('└──────────────────────────────┘')

def print_login_success():
	print('┌──────────────────────────────┐')
	print('│            Log In            │')
	print('├──────────────────────────────┤')
	print('│    Successfully logged in!   │')
	print('└──────────────────────────────┘')

def print_login_failed():
	print('┌──────────────────────────────┐')
	print('│            Log In            │')
	print('├──────────────────────────────┤')
	print('│     Invalid credentials!     │')
	print('└──────────────────────────────┘')

def print_logout_success():
	print('┌──────────────────────────────┐')
	print('│            Log Out           │')
	print('├──────────────────────────────┤')
	print('│   Successfully logged out!   │')
	print('└──────────────────────────────┘')

def print_logout_failed():
	print('┌──────────────────────────────┐')
	print('│            Log Out           │')
	print('├──────────────────────────────┤')
	print('│      Failed to log out!      │')
	print('└──────────────────────────────┘')

def print_logout_not_logged_in():
	print('┌──────────────────────────────┐')
	print('│            Log Out           │')
	print('├──────────────────────────────┤')
	print('│   No logged in user found!   │')
	print('└──────────────────────────────┘')

def print_exit():
	print('┌──────────────────────────────┐')
	print('│             Exit             │')
	print('├──────────────────────────────┤')
	print('│             Bye!             │')
	print('└──────────────────────────────┘')

def print_correct_guess(char):
	print('┌──────────────────────────────┐')
	print('│             Guess            │')
	print('├──────────────────────────────┤')
	print('│ Good job! You guessed {}!     │'.format(char))
	print('└──────────────────────────────┘')

def print_wrong_guess(char):
	print('┌──────────────────────────────┐')
	print('│             Guess            │')
	print('├──────────────────────────────┤')
	print('│ Sorry!                       │')
	print('│ {} was not in the word!       │'.format(char)) 
	print('└──────────────────────────────┘')

def print_win():
	print('┌──────────────────────────────┐')
	print('│              Win             │')
	print('├──────────────────────────────┤')
	print('│ Congratulations! You won!    │')
	print('└──────────────────────────────┘')

def print_loss():
	print('┌──────────────────────────────┐')
	print('│             Loss             │')
	print('├──────────────────────────────┤')
	print('│ Sorry, you lost.             │')
	print('│ Better luck next time!       │')
	print('└──────────────────────────────┘')

def print_play_again():
	print('┌──────────────────────────────┐')
	print('│         Play again?          │')
	print('├──────────────────────────────┤')
	print('│ Would you like to play       │')
	print('│ another round?               │')
	print('└──────────────────────────────┘')

def print_already_guessed(char):
	print('┌──────────────────────────────┐')
	print('│             Guess            │')
	print('├──────────────────────────────┤')
	print('│ {} is already guessed!        │'.format(char))
	print('└──────────────────────────────┘')

def print_user_information(current_user):
	campusnetid_str = '│ CampusNetID : {}'.format(current_user['campusnetId'])
	username_str =    '│ Username    : {}'.format(current_user['brugernavn'])
	first_name_str =  '│ First Name  : {}'.format(current_user['fornavn'])
	last_name_str =   '│ Last Name   : {}'.format(current_user['efternavn'])
	email_str =       '│ E-mail      : {}'.format(current_user['email'])
	study_str =       '│ Study       : {}'.format(current_user['studeretning'])
	last_active_str = '│ Last Active : {}'.format(current_user['sidstAktiv'])

	campusnetid_str = trim_str(campusnetid_str, 41, True)
	username_str = trim_str(username_str, 41, True)
	first_name_str = trim_str(first_name_str, 41, True)
	last_name_str = trim_str(last_name_str, 41, True)
	email_str = trim_str(email_str, 41, True)
	study_str = trim_str(study_str, 41, True)
	last_active_str = trim_str(last_active_str, 41, True)

	print('┌─────────────────────────────────────────┐')
	print('│             User Information            │')
	print('├─────────────────────────────────────────┤') # 15 length from : to space before |
	print(campusnetid_str)
	print('│                                         │')
	print(username_str)
	print(first_name_str)
	print(last_name_str)
	print('│                                         │')
	print(email_str)
	print(study_str)
	print(last_active_str)
	print('└─────────────────────────────────────────┘')

def print_send_email_prompt():
	print('┌──────────────────────────────┐')
	print('│          Send Email          │')
	print('├──────────────────────────────┤')
	print('│ Please enter the username    │')
	print('│ and password of the user who │')
	print('│ you want to send an email to.│')
	print('│ Then enter the subject and   │')
	print('│ message to send.             │')
	print('└──────────────────────────────┘')

def print_send_email_success(username):
	username_str =    '│ {}!'.format(username)
	username_str = trim_str(username_str, 30, True)
	print('┌──────────────────────────────┐')
	print('│          Send Email          │')
	print('├──────────────────────────────┤')
	print('│ Successfully send email to   │')
	print(username_str)
	print('└──────────────────────────────┘')

def print_send_email_failed(username):
	username_str =    '│ {}!'.format(username)
	username_str = trim_str(username_str, 30, True)
	print('┌──────────────────────────────┐')
	print('│          Send Email          │')
	print('├──────────────────────────────┤')
	print('│ Failed to send email to      │')
	print(username_str)
	print('└──────────────────────────────┘')

def print_forgot_password():
	print('┌──────────────────────────────┐')
	print('│        Forgot Password       │')
	print('├──────────────────────────────┤')
	print('│ Please enter your username.  │')
	print('└──────────────────────────────┘')

def print_forgot_password_success():
	print('┌──────────────────────────────┐')
	print('│        Forgot Password       │')
	print('├──────────────────────────────┤')
	print('│ Success. Please check your   │')
	print('│ email for your password.     │')
	print('└──────────────────────────────┘')

def print_forgot_password_failed():
	print('┌──────────────────────────────┐')
	print('│        Forgot Password       │')
	print('├──────────────────────────────┤')
	print('│ Failed to sent forgot        │')
	print('│ password email!              │')
	print('└──────────────────────────────┘')

def print_about():
	print('┌──────────────────────────────┐')
	print('│             About            │')
	print('├──────────────────────────────┤')
	print('│         Developed at         │')
	print('│    DTU Distributed Systems   │')
	print('└──────────────────────────────┘')

def print_new_password():
	print('┌──────────────────────────────┐')
	print('│        Change Password       │')
	print('├──────────────────────────────┤')
	print('│ Please enter your username,  │')
	print('│ current password and a new   │')
	print('│ password.                    │')
	print('└──────────────────────────────┘')

def print_new_password_success():
	print('┌──────────────────────────────┐')
	print('│        Change Password       │')
	print('├──────────────────────────────┤')
	print('│ Successfully changed         │')
	print('│ password!                    │')
	print('└──────────────────────────────┘')

def print_new_password_failed():
	print('┌──────────────────────────────┐')
	print('│        Change Password       │')
	print('├──────────────────────────────┤')
	print('│ Failed to change password!   │')
	print('└──────────────────────────────┘')

def print_new_highscore(highscore):
	high_score_str = trim_str(str(highscore), 28, False)
	print('┌──────────────────────────────┐')
	print('│          High Score          │')
	print('├──────────────────────────────┤')
	print('│ Reached new high score!      │')
	print('│ {} │'.format(high_score_str))
	print('└──────────────────────────────┘')

def print_lobby(user_map):
	print('┌──────────────────────────────┐')
	print('│             Lobby            │') # length 32
	print('├──────────────────────────────┤') # s151641 length 7 so thats 7 max for the username # Score 6 is max
	print('│ User        Score     Battle │')
	print('├──────────────────────────────┤')

	char = 'a'
	for username, score in user_map.items():
		username = add_leading_zeroes(username, 7)
		score = add_leading_zeroes(score, 6)
		print('│ {}     {}    ({})    │'.format(username, score, char))
		char = chr(ord(char) + 1)
	print('└──────────────────────────────┘')

def print_high_scores(user_map):
	print('┌──────────────────────────────┐')
	print('│          High Scores         │') # length 32
	print('├──────────────────────────────┤') # s151641 length 7 so thats 7 max for the username # Score 6 is max
	print('│ User              High Score │')
	print('├──────────────────────────────┤')

	for username, score in user_map.items():
		username = add_leading_zeroes(username, 7)
		score = add_leading_zeroes(score, 6)
		print('│ {}           {}     │'.format(username, score))

	print('└──────────────────────────────┘')

def trim_str(string, max_len, is_with_end_pipe) -> str:
	delta_len = max_len - len(string)
	for i in range(0, delta_len):
		string += ' '
		if i == delta_len - 1:
			if is_with_end_pipe:
				string += ' │'
			break
	return string

def add_leading_zeroes(string, length) -> str:
	string = str(string)
	if len(string) > length:
		return

	if len(string) < length:
		delta_len = length - len(string)
		string += (' ' * delta_len)

	return string 

def get_user_guess():
	while True:
		guess = get_user_input('Guess')
		if (len(str(guess)) > 1):
			continue
		else:
			return guess

def get_cmd() -> str:
	return input(PROMPT_SYMBOL)

def get_user_input(prefix) -> str:
	return input('[{}] {}'.format(prefix, PROMPT_SYMBOL))