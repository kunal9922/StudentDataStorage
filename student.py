from tkinter import *
from tkinter import ttk
import mysql.connector

class StudentRecord:
	def __init__(self, root):
		self.root = root
		title = Label(self.root, text="Student Management System", bd=5, relief="groove", font=("Cambria", 32, "bold"), bg="yellow", fg="red")
		title.pack(side=TOP, fill=X)
		self.root.title("Student Management System")
		# take the user monitor width and Height
		self.screenWidth = self.root.winfo_screenwidth()
		self.screenHeight = self.root.winfo_screenheight()

		self.root.geometry(f'{self.screenWidth}x{self.screenHeight}+0+0')

		# =============== Manage Frame =================
				# This frame contain txt box where  values will insert
		manageFrame = LabelFrame(self.root, text="Manage Data", font=("Time Roman",20,"bold"), bd=4, fg='Black', bg="#ff9933")
		manageFrame.place(x=30, y=70, width=460, height=600)

		lbl_roll = Label(manageFrame, text="Roll No : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_roll.grid(row=0, column=0, padx=10, pady=10, sticky="w")
		txt_roll = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_roll.grid(row=0, column=1, padx=10, pady=10, sticky="w")

		lbl_Name = Label(manageFrame, text="Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
		txt_Name = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_Name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

		lbl_Sem = Label(manageFrame, text="Semester : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Sem.grid(row=2, column=0, padx=10, pady=10, sticky="w")
		txt_Sem = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_Sem.grid(row=2, column=1, padx=10, pady=10, sticky="w")

		lbl_Email = Label(manageFrame, text="Email : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Email.grid(row=3, column=0, padx=10, pady=10, sticky="w")
		txt_Email = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_Email.grid(row=3, column=1, padx=10, pady=10, sticky="w")

		lbl_gender = Label(manageFrame, text="Gender : ", font=("Consolas", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_gender.grid(row=4, column=0, padx=10, pady=10, sticky="w")
		com_gen = ttk.Combobox(manageFrame, font=("Consolas", 18, "bold"),state="readonly")
		com_gen["values"] = ("Male", "Female", "Other")
		com_gen.grid(row=4, column=1, padx=10, pady=10)

		lbl_dob = Label(manageFrame, text="D.O.B :", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_dob.grid(row=5, column=0, padx=10, pady=10, sticky="w")
		txt_dob = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_dob.grid(row=5, column=1, padx=10, pady=10, sticky="w")

		lbl_address = Label(manageFrame, text="Address : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_address.grid(row=6, column=0, padx=10, pady=10, sticky="w")
		txt_address = Text(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, height=5)
		txt_address.grid(row=6, column=1, padx=10, pady=10, sticky="w")

		#========== button frame ==========
		btnFrame = LabelFrame(manageFrame, bd=6, relief ="solid", fg='Black', bg="#7bfc03")
		btnFrame.place(x=10, y=500, width=430)

		addbtn = Button(btnFrame, text="Add", width=10, font=("Consolas", 10, "bold")).grid(row=0,column=0, padx=10,pady=10)
		deletebtn = Button(btnFrame, text="Delete", width=10, font=("Consolas", 10, "bold")).grid(row=0, column=1, padx=10, pady=10)
		updatebtn = Button(btnFrame, text="Update", width=10, font=("Consolas", 10, "bold")).grid(row=0, column=2, padx=10, pady=10)
		clearbtn = Button(btnFrame, text="Clear", width=10, font=("Consolas", 10, "bold")).grid(row=0, column=3, padx=10, pady=10)


		# ============== Record Showing Frame ================
				# This frame contain list box where  values will shows.
		recordFrame = LabelFrame(self.root, text="Showing Records", font=("Time Roman", 20, "bold"), bd=4 ,fg='Black', bg="#ff9933")
		recordFrame.place(x=500, y=70, width=830, height=600)

		searchLabel = Label(recordFrame, text="Search : ", font=("Consolas", 18, "bold"), fg="#adfc03", bg="#ff9933")
		searchLabel.grid(row=0, column=0, padx=10, pady=10)

		com_gen = ttk.Combobox(recordFrame, font=("Consolas", 18, "bold"), width=10, state="readonly")
		com_gen["values"] = ("Roll Num", "Name", "Semester", "Email", "Gender", "DateOfBirth", "Address")
		com_gen.grid(row=0, column=1, padx=5, pady=10)

		txt_Search = Entry(recordFrame, font=("Consolas", 15, "bold"), bd=5, relief="ridge", width=25)
		txt_Search.grid(row=0, column=2, padx=5, pady=10, sticky="w")

		searchBtn = Button(recordFrame, text="Search ", width=8, font=("Consolas", 14, "bold")).grid(row=0, column=3, padx=10, pady=10)
		showBtn = Button(recordFrame, text="ShowAll ", width=8, font=("Consolas", 14, "bold")).grid(row=0, column=4, padx=10, pady=10)

		#=========== Table Data Frame ============
		tableFrame = Frame(recordFrame, bd=2, relief="ridge", bg="Crimson" )
		tableFrame.place(x=10, y=70, width=780, height=480)

		# ========== showing stored record on this frame ==========
		scroll_X = Scrollbar(tableFrame, orient=HORIZONTAL)
		scroll_Y = Scrollbar(tableFrame, orient=VERTICAL)
		studentRecordTable = ttk.Treeview(tableFrame, columns=("roll", "name", "sem", "email", "gender", "dob", "address"), xscrollcommand=scroll_X.set, yscrollcommand=scroll_Y.set)
		scroll_X.pack(side=BOTTOM, fill=X)
		scroll_Y.pack(side=RIGHT, fill=Y)
		scroll_X.config(command=studentRecordTable.xview)
		scroll_Y.config(command=studentRecordTable.yview)
		studentRecordTable.heading("roll", text="Roll Num")
		studentRecordTable.heading("name", text="Name")
		studentRecordTable.heading("sem", text="Semester")
		studentRecordTable.heading("email", text="Email")
		studentRecordTable.heading("gender", text="Gender")
		studentRecordTable.heading("dob", text="DateOFBirth")
		studentRecordTable.heading("address", text="Address")
		studentRecordTable["show"] = "headings"
		studentRecordTable.pack(expand=True,fill=BOTH)

if __name__ == "__main__":
	win = Tk()
	root = StudentRecord(win)
	win.mainloop()