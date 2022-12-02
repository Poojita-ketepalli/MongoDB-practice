# _____________@Poojita Ketepalli___________________

from tkinter import *
import pymongo
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection successful")

db = client['Students']
students_data = db['students_list']
marks_data = db['marks']


root = Tk()
root.geometry("850x650")
root.title("CRUD operations with mongoDB")
root.configure(bg='white')

heading = Frame(root,width =850,height=100,relief=RAISED,bd=8)
heading.pack(side="top")
heading_label = Label(heading,font=('Times New Roman',41,'bold'),text="CRUD Operations with MongoDB",fg="black",bd=10,anchor=W,bg = "white")
heading_label.grid(row=0,column=0)

widgets_frame = Frame(root,width =850,height=550,bd=8,bg = "white")
widgets_frame.pack(side="top")

reg_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Reg.No",fg="black",bd=10,anchor=W,bg = "white")
reg_label.grid(row=0, column=0)
reg_no = IntVar()
reg_entry=Entry(widgets_frame,textvariable=reg_no,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
reg_entry.grid(row=0, column=2)

name_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Name",fg="black",bd=10,anchor=W,bg = "white")
name_label.grid(row=1, column=0)
name = StringVar()
name_entry=Entry(widgets_frame,textvariable=name,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
name_entry.grid(row=1, column=2)

section_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Section",fg="black",bd=10,anchor=W,bg = "white")
section_label.grid(row=2, column=0)
section = StringVar()
section_entry=Entry(widgets_frame,textvariable=section,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
section_entry.grid(row=2, column=2)

branch_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Branch",fg="black",bd=10,anchor=W,bg = "white")
branch_label.grid(row=3, column=0)
branch = StringVar()
branch_entry=Entry(widgets_frame,textvariable=branch,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
branch_entry.grid(row=3, column=2)

spl_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Specialization",fg="black",bd=10,anchor=W,bg = "white")
spl_label.grid(row=4, column=0)
spl = StringVar()
spl_entry=Entry(widgets_frame,textvariable=spl,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
spl_entry.grid(row=4, column=2)


sub1_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Subject-1",fg="black",bd=10,anchor=W,bg = "white")
sub1_label.grid(row=0, column=4)
sub1 = IntVar()
sub1_entry=Entry(widgets_frame,textvariable=sub1,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
sub1_entry.grid(row=0, column=6)

sub2_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Subject-2",fg="black",bd=10,anchor=W,bg = "white")
sub2_label.grid(row=1, column=4)
sub2 = IntVar()
sub2_entry=Entry(widgets_frame,textvariable=sub2,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
sub2_entry.grid(row=1, column=6)

sub3_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Subject-3",fg="black",bd=10,anchor=W,bg = "white")
sub3_label.grid(row=2, column=4)
sub3 = IntVar()
sub3_entry=Entry(widgets_frame,textvariable=sub3,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
sub3_entry.grid(row=2, column=6)

sub4_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Subject-4",fg="black",bd=10,anchor=W,bg = "white")
sub4_label.grid(row=3, column=4)
sub4 = IntVar()
sub4_entry=Entry(widgets_frame,textvariable=sub4,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
sub4_entry.grid(row=3, column=6)

sub5_label = Label(widgets_frame,font=('Times New Roman',20,'bold'),text="Subject-5",fg="black",bd=10,anchor=W,bg = "white")
sub5_label.grid(row=4, column=4)
sub5 = IntVar()
sub5_entry=Entry(widgets_frame,textvariable=sub5,font=('Times New Roman',15,'bold'),bd=2,width=14,justify='right')
sub5_entry.grid(row=4, column=6)


def clear():
	reg_no.set("")
	name.set("")
	section.set("")
	branch.set("")
	spl.set("")

	sub1.set("")
	sub2.set("")
	sub3.set("")
	sub4.set("")
	sub5.set("")

def add_students():
	document = ({
		"Reg_No":reg_no.get(),
		"name":name.get(),
		"section":section.get(),
		"branch":branch.get(),
		"spl":spl.get()
		})
	return students_data.insert_one(document)

def add_marks():
	add = add_students()
	document2 = ({
		"s_id": add.inserted_id,
		"Subject-1":sub1.get(),
		"Subject-2":sub2.get(),
		"Subject-3":sub3.get(),
		"Subject-4":sub4.get(),
		"Subject-5":sub5.get()
		})
	result.set("Added Successfully")
	clear()
	return marks_data.insert_one(document2)

def search():
	data = {}
	for i in students_data.find({"Reg_No":reg_no.get()}):
		data = i
	if(data!={}):
		name.set(data["name"])
		section.set(data["section"])
		branch.set(data["branch"])
		spl.set(data["spl"])
		for i in marks_data.find({"s_id":data["_id"]}):
			data2 = i
		sub1.set(data2["Subject-1"])
		sub2.set(data2["Subject-2"])
		sub3.set(data2["Subject-3"])
		sub4.set(data2["Subject-4"])
		sub5.set(data2["Subject-5"])

		result.set("Document Exist")
	else:
		result.set("Document not exist")
def update_document():
	data = {}
	for i in students_data.find({"Reg_No":reg_no.get()}):
		data = i
	for i in marks_data.find({"s_id":data["_id"]}):
		data2 = i
	students_data.update_many(
    {"Reg_No":reg_no.get()},
    {'$set':{"name":name.get(),
		"section":section.get(),
		"branch":branch.get(),
		"spl":spl.get()},
    "$currentDate":{"lastModified":True}}
	)
	marks_data.update_many(
		{"s_id":data["_id"]},
		{'$set':{
			"Subject-1":sub1.get(),
			"Subject-2":sub2.get(),
			"Subject-3":sub3.get(),
			"Subject-4":sub4.get(),
			"Subject-5":sub5.get()},
		"$currentDate":{"lastModified":True}}
	)
	result.set("Updated successfully")

def delete_document():
	marks_data.delete_one({"s_id":students_data.find_one({"Reg_No":reg_no.get()})["_id"]})
	students_data.delete_one({"Reg_No":reg_no.get()})
	result.set("Deleted Successfully")




add_button = Button(widgets_frame, text='Add', fg='black', bg='powder blue', height=1, width=6,font=('Times New Roman',20,'bold'),bd=2,command=add_marks)
add_button.grid(row=5, column=0)

space_label = Label(widgets_frame,font=('Times New Roman',4,'bold'),text="  ",fg="black",bd=10,anchor=W,bg = "white")
space_label.grid(row=5, column=1)

delete_button = Button(widgets_frame, text='Delete', fg='black', bg='powder blue', height=1, width=6,font=('Times New Roman',20,'bold'),bd=2,command = delete_document)
delete_button.grid(row=5, column=2)

space_label = Label(widgets_frame,font=('Times New Roman',4,'bold'),text="     ",fg="black",bd=10,anchor=W,bg = "white")
space_label.grid(row=5, column=3)

update_button = Button(widgets_frame, text='Update', fg='black', bg='powder blue', height=1, width=6,font=('Times New Roman',20,'bold'),bd=2,command = update_document)
update_button.grid(row=5, column=4)

space_label = Label(widgets_frame,font=('Times New Roman',4,'bold'),text="  ",fg="black",bd=10,anchor=W,bg = "white")
space_label.grid(row=5, column=5)

search_button = Button(widgets_frame, text='Search', fg='black', bg='powder blue', height=1, width=6,font=('Times New Roman',20,'bold'),bd=2,command = search)
search_button.grid(row=5, column=6)

clear_button = Button(widgets_frame, text='Clear', fg='black', bg='powder blue', height=1, width=6,font=('Times New Roman',20,'bold'),bd=2,command = clear)
clear_button.grid(row=6, column=3)


result = StringVar()
result_entry=Entry(widgets_frame,textvariable=result,font=('Times New Roman',15,'bold'),bd=2,width=20,justify='right')
result_entry.grid(row=6, column=0)


root.mainloop()