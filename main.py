from settings import Singleton, System
from command import app
import surface
import router
import load
import settings

manager = Singleton.getInstance().manager
manager.login('admin', 'admin')

load.load_user()
load.trans_to_tree(settings.BASE_PATH)
surface.clear_screen()

manager.login('guest', '')

while True:
	surface.print_prompt()
	input_cmd = input()
	if input_cmd == "quit":
		load.store_user()
		break
	app.run(input_cmd)

