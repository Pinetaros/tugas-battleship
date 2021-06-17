import json

class Config:

	def __init__(self):

		self.app_title = "Battleship"

		self.row = 4
		self.column = 4

		base = 170
		ratio = 4
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+500"

		self.init_img_btn = "img/init_img.png"
		self.final_img_btn = "img/final_img.png"
		self.win_img_btn = "img/win_img.png"

		self.intro_path = "img/intro.png"
		self.main_menu_logo_path = "img/menu.png"

		self.users_path = "json/users.json"
		self.gameData_path = "json/gameData.json"
		self.gameData_counter_path = "json/gameData_counter.json"

		self.gameData = self.load_gameData(self.gameData_path)


	def load_userData(self, users_path):
		with open(users_path, "r") as json_data:
			userData = json.load(json_data)
		return userData

	def load_gameData(self, gameData_path):
		with open(self.gameData_path, "r") as json_data:
			gameData = json.load(json_data)
		return gameData

	def save_gameData(self, gameData_path):
		with open(self.gameData_path, "w") as json_data:
			json.dump(self.gameData, json_data)
