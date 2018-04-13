import tui
import rest
import sys

current_user = None

def exec_cmd(cmd):
	if cmd is 'q':
		do_login()
	elif cmd is 'w':
		do_logout()
	elif cmd is 'e':
		do_user_information()
	elif cmd is 'd':
		do_forgot_password()
	elif cmd is 'r':
		do_play()
	elif cmd is 't':
		do_lobby()
	elif cmd is 'a':
		do_high_scores()
	elif cmd is 's':
		do_send_email()
	elif cmd is 'f':
		do_new_password()
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
		print(tui.print_send_email_success(username))
	else:
		tui.clear()
		tui.print_menu(rest.get_current_user_amount(), current_user)
		print(tui.print_send_email_failed(username))

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
	pass

def do_lobby():
	pass

def do_high_scores():
	pass

if __name__ == '__main__': main()