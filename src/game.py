import rest
import tui

user = None

def start(current_user):
	global user
	user = current_user
	username = user['brugernavn']
	tui.clear()
	rest.reset_game(username)
	rest.reset_score(username)
	print_hangman()
	while True:
		do_guess()

		if rest.is_game_won(username):
			tui.clear()
			print_hangman()
			tui.print_win()
			if play_again():
				rest.reset_game(username)
				tui.clear()
				print_hangman()
				continue
			break

		if rest.is_game_lost(username):
			tui.clear()
			print_hangman()
			tui.print_loss()
			if play_again():
				rest.reset_score(username)
				rest.reset_game(username)
				tui.clear()
				print_hangman()
				continue
			break

def do_guess():
	global user
	username = user['brugernavn']

	while True:
		guess = tui.get_user_guess()
		is_guessed = rest.is_char_guessed(username, guess)
		if is_guessed:
			tui.clear()
			print_hangman()
			tui.print_already_guessed(guess)
			continue
		else:
			break

	if rest.guess(username, guess):
		tui.clear()
		print_hangman()
		tui.print_correct_guess(guess)
		if rest.is_highscore(username, user['adgangskode']):
			current_score = str(rest.get_score(username))
			rest.set_user_highscore(username, current_score)
			tui.print_new_highscore(current_score)
	else:
		tui.clear()
		print_hangman()
		tui.print_wrong_guess(guess)

def print_hangman():
	tui.print_hangman(user['fornavn'],
		rest.get_life(user['brugernavn']),
		rest.get_score(user['brugernavn']),
		rest.get_word(user['brugernavn']), 
		rest.get_guessed_chars(user['brugernavn']))

def play_again() -> bool:
	tui.print_play_again()
	
	answer = None

	while answer == None or len(answer) > 1:
		answer = tui.get_user_input('y/N')

	if answer == 'y' or answer == 'Y':
		return True
	else:
		return False