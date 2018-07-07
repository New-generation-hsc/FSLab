from settings import Singleton, System
from command import app
import surface
import router

manager = Singleton.getInstance().manager
manager.login('guest', '')

surface.clear_screen()

while True:
	surface.print_prompt()
	input_cmd = input()
	if input_cmd == "quit":
		break
	app.run(input_cmd)