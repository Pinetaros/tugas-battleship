import tkinter as tk

class InfoPage(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="dodger blue")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="dodger blue")
		self.main_frame.pack(expand=True)

		self.frame_howToPlay = tk.Frame(self.main_frame, width=self.config.side, height=3*self.config.side//8, bg="dodger blue")
		self.frame_howToPlay.pack(side="top", fill="x")

		self.label_howToPlay = tk.Label(self.frame_howToPlay, text="How to Play", font=("Elephant", 20, "bold"), bg="gray1", fg="slate gray")
		self.label_howToPlay.pack(side="top", anchor="nw", pady=5)

		self.scroll_howToPlay = tk.Scrollbar(self.frame_howToPlay)
		self.scroll_howToPlay.pack(side="right", fill="y")

		self.text_howToPlay = tk.Text(self.frame_howToPlay, width=100, height=8, font=("Elephant", 18))
		self.howToPlay = """Press button, use luck, monke win."""
		self.text_howToPlay.insert(tk.END, self.howToPlay)
		self.text_howToPlay.pack(pady=5)

		self.text_howToPlay.configure(yscrollcommand=self.scroll_howToPlay.set)
		self.scroll_howToPlay.configure(command=self.text_howToPlay.yview)

		self.frame_aboutGame = tk.Frame(self.main_frame, width=self.config.side, height=3*self.config.side//8, bg="dodger blue")
		self.frame_aboutGame.pack(side="top", fill="x")

		self.label_aboutGame = tk.Label(self.frame_aboutGame, text="About Game", font=("Elephant", 20, "bold"), bg="gray1", fg="slate gray")
		self.label_aboutGame.pack(side="top", anchor="nw", pady=5)

		self.scroll_aboutGame = tk.Scrollbar(self.frame_aboutGame)
		self.scroll_aboutGame.pack(side="right", fill="y")

		self.text_aboutGame = tk.Text(self.frame_aboutGame, width=100, height=8, font=("Elephant", 18))
		self.aboutGame = """This project was made by Rafif Adelio, i don't know what to put here except that."""
		self.text_aboutGame.insert(tk.END, self.aboutGame)
		self.text_aboutGame.pack(pady=5)

		self.text_aboutGame.configure(yscrollcommand=self.scroll_aboutGame.set)
		self.scroll_aboutGame.configure(command=self.text_aboutGame.yview)

		self.btn_mainMenu = tk.Button(self.main_frame, text="Main Menu", font=("Elephant", 18, "bold"), command=lambda:self.game.change_page('mainMenu'))
		self.btn_mainMenu.pack(side="bottom", pady=5)