import os

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

	user_str = trim_str(user_str, 36)

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
		print('│ (f) New Password                   │')
	
	print('│                                    │')
	print('│ (g) About                          │')
	print('│ (x) Exit                           │')
	print('└────────────────────────────────────┘')

def print_hangman(name, life, score, guessed_characters, used_characters):
	print('┌──────────────────────────────┐')
	print('│      Distributed Hangman     │')
	print('├──────────────────────────────┤')
	print('│ Name: {}           ┌────┐    │'.format(name))
	print('│ Life: {}           │    0    │'.format(life))
	print('│ Score: {}          │   /|\   │'.format(score))
	print('│                    │   / \   │')
	print('│                    ┴         │')
	print('│                              │')
	print('│      {}                      │'.format(guessed_characters))
	print('│    - {} -                    │'.format(used_characters))
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

def print_user_information(current_user):
	campusnetid_str = '│ CampusNetID : {}'.format(current_user['campusnetId'])
	username_str =    '│ Username    : {}'.format(current_user['brugernavn'])
	first_name_str =  '│ First Name  : {}'.format(current_user['fornavn'])
	last_name_str =   '│ Last Name   : {}'.format(current_user['efternavn'])
	email_str =       '│ E-mail      : {}'.format(current_user['email'])
	study_str =       '│ Study       : {}'.format(current_user['studeretning'])
	last_active_str = '│ Last Active : {}'.format(current_user['sidstAktiv'])

	campusnetid_str = trim_str(campusnetid_str, 41)
	username_str = trim_str(username_str, 41)
	first_name_str = trim_str(first_name_str, 41)
	last_name_str = trim_str(last_name_str, 41)
	email_str = trim_str(email_str, 41)
	study_str = trim_str(study_str, 41)
	last_active_str = trim_str(last_active_str, 41)

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
	print('┌──────────────────────────────┐')
	print('│          Send Email          │')
	print('├──────────────────────────────┤')
	print('│ Successfully send email to   │')
	print('│ {}!                    │'.format(username))
	print('└──────────────────────────────┘')

def print_send_email_failed(username):
	print('┌──────────────────────────────┐')
	print('│          Send Email          │')
	print('├──────────────────────────────┤')
	print('│ Failed to send email to      │')
	print('│ {}!                    │'.format(username))
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
	print('│         New Password         │')
	print('├──────────────────────────────┤')
	print('│ Please enter your username,  │')
	print('│ current password and a new   │')
	print('│ password.                    │')
	print('└──────────────────────────────┘')

def print_new_password_success():
	print('┌──────────────────────────────┐')
	print('│         New Password         │')
	print('├──────────────────────────────┤')
	print('│ Successfully changed         │')
	print('│ password!                    │')
	print('└──────────────────────────────┘')

def print_new_password_failed():
	print('┌──────────────────────────────┐')
	print('│         New Password         │')
	print('├──────────────────────────────┤')
	print('│ Failed to change password!   │')
	print('└──────────────────────────────┘')

def trim_str(string, max_len) -> str:
	delta_len = max_len - len(string)
	for i in range(0, delta_len):
		string += ' '
		if i == delta_len - 1:
			string += ' │'
			break
	return string;

def get_cmd() -> str:
	return input(PROMPT_SYMBOL)

def get_user_input(prefix) -> str:
	return input('[{}] {}'.format(prefix, PROMPT_SYMBOL))