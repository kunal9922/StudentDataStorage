import tkinter as tk
import DBconnect
from tkinter import messagebox
class ShowDBFrame():
	def __init__(self, rootWin):
		self.rootWin = rootWin

	def getfoucs(self, event):

		try:
			cs = self.listDBs.curselection()  # list of items we were selected that store inside it variable called cs
			print(cs)
			self.dbvartxt.set(self.listDBs.get(cs[0])[0])
			print(self.listDBs.get(cs[0])[0])
		except IndexError:
			pass

	def createdb(self):
		print(self.dbvartxt.get())
		self.DB.createDB(self.dbvartxt.get())
		listofDBs = self.DB.showDBs()

		# fill rows of Available databases
		for dbName in listofDBs:
			self.listDBs.insert(tk.END, dbName)

	def useExistsDB(self):
		self.DB.database = self.dbvartxt.get()
		print(self.dbvartxt.get())
		self.DB.useOtherDB()
		self.tableFrame()

	def DBFrame(self):
		self.lableDBframe = tk.LabelFrame(self.rootWin, text="DataBase Entry", font=("Time Roman", 20, "bold"), bd=3, relief="ridge", bg="#73ebe1")

		# place where all available DB will show
		self.lableDBframe.grid(row=3, column=0, padx=10, pady=10)
		listFrame = tk.Frame(self.lableDBframe)
		listFrame.grid(row=1, column=0, columnspan=2, pady=10)
		avaiDBs = tk.Label(self.lableDBframe, text="Available DataBases  ", font=("Time Roman", 20, "bold"), fg="#6764fa")
		avaiDBs.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
		xscroll = tk.Scrollbar(listFrame, orient=tk.HORIZONTAL)
		yscroll = tk.Scrollbar(listFrame, orient=tk.VERTICAL)
		self.listDBs= tk.Listbox(listFrame, fg="#000000", bd=0, relief="flat", font=("Time Roman", 15, "bold"))

		self.listDBs.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		xscroll.pack(fill=tk.X, side=tk.BOTTOM)
		xscroll.config(command=self.listDBs.xview)
		yscroll.config(command=self.listDBs.yview)
		yscroll.pack(fill=tk.Y, side=tk.RIGHT)
		self.listDBs.pack(fill=tk.BOTH, side=tk.LEFT)

		self.dbvartxt = tk.StringVar()
		dbNameEntry = tk.Entry(self.lableDBframe, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, bg="red", fg="#ffffff", textvariable=self.dbvartxt)
		dbNameEntry.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
		useDBbtn = tk.Button(self.lableDBframe, font=("Consolas", 15, "bold"), text="Use DB", command=self.useExistsDB).grid(row=3, column=0, padx=5, pady=5)
		createDBbtn = tk.Button(self.lableDBframe, font=("Consolas", 15, "bold"), text="Create DB",  command=self.createdb).grid(row=3, column=1, padx=5, pady=5)

		# insert result to it's list boxes
		self.DB = DBconnect.DB_connect("localhost", "root", "kunal9922soni")
		self.DB.database = self.dbvartxt.get()
		listofDBs = self.DB.shows("DATABASES")
		# fill rows of Available databases
		for dbName in listofDBs:
			self.listDBs.insert(tk.END, dbName)

		self.listDBs.bind("<<ListboxSelect>>", self.getfoucs)

		#self.tableFrame()

	def getfoucstable(self, event):
		try:
			cs = self.listTables.curselection()
			self.tablevar.set(self.listTables.get(cs[0])[0])
			print(self.listTables.get(cs[0])[0])
		except IndexError:
			pass

	def useExistsTable(self):
		print("Tables is selecteed = ", self.tablevar.get())
		self.DB.table = self.tablevar.get()

	def createTable(self):
		print(self.tablevar.get())
		self.DB.createtable(self.tablevar.get())
		self.listTables.delete(0, tk.END)
		listTables = self.DB.shows("TABLES")

		# fill rows of Available databases
		for table in listTables:
			self.listTables.insert(tk.END, table)

	def tableFrame(self):
		self.lableTableframe = tk.LabelFrame(self.rootWin, text="Tables Entry", font=("Time Roman", 20, "bold"), bd=3,
		                                  relief="ridge", bg="#73ebe1")

		# place where all available DB will show
		self.lableTableframe.grid(row=3, column=1, padx=10, pady=10)
		listFrame = tk.Frame(self.lableTableframe)
		listFrame.grid(row=1, column=0, columnspan=2, pady=10)
		avaiTables = tk.Label(self.lableTableframe, text="Available Tables  ", font=("Time Roman", 20, "bold"),
		                   fg="#6764fa")
		avaiTables.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
		xscroll = tk.Scrollbar(listFrame, orient=tk.HORIZONTAL)
		yscroll = tk.Scrollbar(listFrame, orient=tk.VERTICAL)
		self.listTables = tk.Listbox(listFrame, fg="#000000", bd=0, relief="flat", font=("Time Roman", 15, "bold"))

		self.listTables.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		xscroll.pack(fill=tk.X, side=tk.BOTTOM)
		xscroll.config(command=self.listTables.xview)
		yscroll.config(command=self.listTables.yview)
		yscroll.pack(fill=tk.Y, side=tk.RIGHT)
		self.listTables.pack(fill=tk.BOTH, side=tk.LEFT)

		self.tablevar = tk.StringVar()
		tableNameEntry = tk.Entry(self.lableTableframe, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25,
		                       bg="red", textvariable=self.tablevar)
		tableNameEntry.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
		usetablebtn = tk.Button(self.lableTableframe, font=("Consolas", 15, "bold"), text="Use Table", command=self.useExistsTable).grid(row=3,
		                                                                                                 column=0,
		                                                                                                 padx=5, pady=5)
		createtablebtn = tk.Button(self.lableTableframe, font=("Consolas", 15, "bold"), text="Create Table", command=self.createTable).grid(row=3,
		                                                                                                       column=1,
		                                                                                                       padx=5,
		                                                                                                       pady=5)

		# insert result to it's list boxes
		Tables = self.DB.showTables()
		# fill rows of Available databases
		for table in Tables:
			self.listTables.insert(tk.END, table)

		self.listTables.bind("<<ListboxSelect>>", self.getfoucstable)


class GUI_project(ShowDBFrame):
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
		hostLabel.grid(row=0, column=0, padx=20, pady=5)
		hostEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.hostNameVar)
		hostEntry.grid(row=0, column=1, padx=5, pady=5)

		userNameLabel = tk.Label(topWin, text=" User Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		userNameLabel.grid(row=1, column=0, padx=20, pady=5)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.userNameVar)
		userEntry.grid(row=1, column=1, padx=5, pady=5)

		passwdLabel = tk.Label(topWin, text=" PassWord : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		passwdLabel.grid(row=2, column=0, padx=20, pady=5)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.passwordVar, show="*")
		userEntry.grid(row=2, column=1, padx=5, pady=5)

		#	hostName = tk.Label(topWin, text=" DB Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		#hostName.grid(row=3, column=0, padx=20, pady=10)

		dbFrame = ShowDBFrame(rootWin=topWin)
		dbFrame.DBFrame()




