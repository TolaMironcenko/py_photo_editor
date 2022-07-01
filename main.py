from photo_editor import PyPhotoEditor
from termcolor import cprint


def main():
	PyPhotoEditor().run()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit('exited')
	except Exception as e:
		cprint('Error: '+str(e), 'red')