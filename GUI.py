import tkinter as tk
from tkinter import messagebox
class ShowDBFrame():
	def DBFrame(self, rootWin):
		pass

class GUI_project():
	def __init__(self, RootWin):
		# toplevel window for connectivity to database
		self.RootWin = RootWin

	def gui_db_connect(self):

		self.hostNameVar = tk.StringVar()
		self.userNameVar = tk.StringVar()
		self.passwordVar = tk.StringVar()

		topWin = tk.Toplevel(self.RootWin, bg="#73ebe1", bd=5)
		topWin.title("DataBase connectivity")

		hostLabel = tk.Label(topWin, text=" Host Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		hostLabel.grid(row=0, column=0, padx=20, pady=10)
		hostEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.hostNameVar)
		hostEntry.grid(row=0, column=1, padx=5, pady=10)

		userNameLabel = tk.Label(topWin, text=" User Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		userNameLabel.grid(row=1, column=0, padx=20, pady=10)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.userNameVar)
		userEntry.grid(row=1, column=1, padx=5, pady=10)

		passwdLabel = tk.Label(topWin, text=" PassWord : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		passwdLabel.grid(row=2, column=0, padx=20, pady=10)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.passwordVar, show="*")
		userEntry.grid(row=2, column=1, padx=5, pady=10)

		#	hostName = tk.Label(topWin, text=" DB Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		#hostName.grid(row=3, column=0, padx=20, pady=10)


