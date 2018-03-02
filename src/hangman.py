import zeep
import tui

def exec_cmd(cmd):
	if cmd is '1':
		print('1')
	elif cmd is '2':
		print('1')
	elif cmd is '3':
		print('1')		
	else:
		print('...')

def main():
	tui.print_startscreen()
	while True:
		tui.print_menu()
		cmd = tui.get_cmd()
		exec_cmd(cmd)

if __name__ == '__main__': main()