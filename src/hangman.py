import tui
import rest
import sys
import game

current_user = None

def exec_cmd(cmd):
	if cmd is 'q':
		if current_user == None:
			do_login()
		else:
			tui.print_unknown_cmd()
	elif cmd is 'w':
		if current_user != None:
			do_logout()
		else:
			tui.print_unknown_cmd()
	elif cmd is 'e':
		if current_user != None:
			do_user_information()
		else:
			tui.print_unknown_cmd()
	elif cmd is 'd':
		if current_user == None:
			do_forgot_password()
		else:
			tui.print_unknown_cmd()
	elif cmd is 'r':
		if current_user != None:
			do_play()
		else:
			tui.print_unknown_cmd()
	elif cmd is 't':
		if current_user != None:
			do_lobby()
		else:
			tui.print_unknown_cmd()
	elif cmd is 'a':
		if current_user != None:
			do_high_scores()
		else:
			tui.print_unknown_cmd()
	elif cmd is 's':
		if current_user != None:
			do_send_email()
		else:
			tui.print_unknown_cmd()
	elif cmd is 'f':
		if current_user != None:
			do_new_password()
		else:
			tui.print_unknown_cmd()
	elif cmd is 'g':
		do_about()
	elif cmd is 'x':
		do_exit()
	else:
		tui.print_unknown_cmd()

def main():
	tui.clear()
	tui.print_startscreen()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	while True:
		cmd = tui.get_cmd()
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		exec_cmd(cmd)

def do_login():
	global current_user

	tui.print_login_prompt()
	username = tui.get_user_input('Username')
	password = tui.get_user_input('Password')

	if rest.login(username, password):
		current_user = rest.get_logged_in_user(username)
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_login_success()
	else:
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_login_failed()

def do_logout():
	global current_user

	if current_user == None:
		tui.print_logout_not_logged_in()
		return

	if rest.logout(current_user['brugernavn']):
		current_user = None
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_logout_success()
	else:
		current_user = None
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_logout_failed()

def do_user_information():
	global current_user
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_user_information(current_user)

def do_send_email():
	global current_user
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_send_email_prompt()
	username = tui.get_user_input('Username')
	password = tui.get_user_input('Password')
	subject = tui.get_user_input('Subject')
	message = tui.get_user_input('Message')

	if rest.send_email(username, password, subject, message):
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_send_email_success(username)
	else:
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_send_email_failed(username)

def do_new_password():
	global current_user
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_new_password()

	username = tui.get_user_input('Username')
	old_password = tui.get_user_input('Old Password')
	new_password = tui.get_user_input('New Password')

	if rest.change_user_password(username, old_password, new_password):
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_new_password_success()
	else:
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_new_password_failed()

def do_forgot_password():
	global current_user
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_forgot_password()

	username = tui.get_user_input('Username')

	if rest.send_forgot_password_email(username, ''):
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_forgot_password_success()
	else:
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		tui.print_forgot_password_failed()

def do_about():
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_about()

def do_exit():
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_exit()
	sys.exit()

def do_play():
	global current_user
	game.start(current_user)
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)

def do_lobby():
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_lobby(rest.get_all_logged_in_users_score())

def do_high_scores():
	tui.clear()
	tui.print_menu(rest.get_current_user_amount(), current_user)
	tui.print_high_scores(rest.get_all_users_highscore())
	
if __name__ == '__main__': main()