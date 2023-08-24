import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import openpyxl

filepath = ""

def select_file():
    global filepath
    filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if filepath:
        initialize_workbook(filepath)

def initialize_workbook(filepath):
    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["First Name", "Last Name", "Title", "Age", "Nationality",
                   "#Courses", "#Semesters", "Registration status"]
        sheet.append(heading)
        workbook.save(filepath)

def enter_data():
    global filepath
    if filepath:
        accepted = accept_var.get()
        if accepted == "Accepted":
            # user info
            firstname = first_name_entry.get()
            lastname = last_name_entry.get()
            if firstname and lastname:
                title = title_combobox.get()
                age = age_spinbox.get()
                nationality = nationality_combobox.get()

                # course info
                registration_status = reg_status_var.get()
                numcourses = numcourses_spinbox.get()
                numsemesters = numsemesters_spinbox.get()

                workbook = openpyxl.load_workbook(filepath)
                sheet = workbook.active
                sheet.append([firstname, lastname, title, age, nationality, numcourses, numsemesters, registration_status])
                workbook.save(filepath)

                # Clear the text boxes
                first_name_entry.delete(0, tkinter.END)
                last_name_entry.delete(0, tkinter.END)
                title_combobox.set('')
                age_spinbox.delete(0, tkinter.END)
                nationality_combobox.set('')
                numcourses_spinbox.delete(0, tkinter.END)
                numsemesters_spinbox.delete(0, tkinter.END)

                # Uncheck the checkboxes
                registered_check.deselect()
                terms_check.deselect()

                # Inside the 'enter_data()' function, after saving the data to the Excel file
                data_treeview.insert("", "end", values=(firstname, lastname, title, age, nationality, numcourses, numsemesters, registration_status))

            else:
                tkinter.messagebox.showwarning(title="Error", message="First name and last name required")
        else:
            tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")
    else:
        tkinter.messagebox.showwarning(title="Error", message="Please select a file first")

window = tkinter.Tk()
"""
This is the root window,parent window/widget with other widgets
"""
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

desired_width = int(screen_width * 0.75)
desired_height = int(screen_height * 0.75)
window.geometry(f"{desired_width}x{desired_height}")

window.title("Data Entry Form")
frame=tkinter.Frame(window) #contained inside the window
frame.pack() #geometry managers in tkinter grid,pack,place
#.pack keeps everything nicelooking and responsive

# Button for browsing file
browse_button = tkinter.Button(frame, text="Browse", command=select_file)
browse_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

#saving user info
user_info_frame=tkinter.LabelFrame(frame,text="User information")#parent frame in window so first parameter
user_info_frame.grid(row= 0,column=0,padx=20,pady=10,sticky="news" )#select columns and row and add a padding to see everything in place
# Configure additional rows
user_info_frame.grid_rowconfigure(1, weight=1)  # Additional row
user_info_frame.grid_rowconfigure(2, weight=1)  # Additional row

# Configure columns
user_info_frame.grid_columnconfigure(0, weight=1)
user_info_frame.grid_columnconfigure(1, weight=1)
user_info_frame.grid_columnconfigure(2, weight=1)

first_name_label=tkinter.Label(user_info_frame,text="First Name")#inside window and frame.There is hierarchy 
#adding a widget,create and define it then pack,place or grid
first_name_label.grid(row=0,column=0)
last_name_label=tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)#Input box
last_name_entry=tkinter.Entry(user_info_frame)#input box
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label=tkinter.Label(user_info_frame,text="Title")
title_combobox=ttk.Combobox(user_info_frame,values=["Mr.","Ms.","Dr."])#every widget specify parent
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label=tkinter.Label(user_info_frame,text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame,from_=18,to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox=ttk.Combobox(user_info_frame,values=["Africa","Antarctica","Asia","Europe","North America","South America"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

#change padding for all widgets so they are spaced out 
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


#saving course info
courses_frame=tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)#news expand in north,east,west,south and padding to keep consistent padding and size as first frame
registered_label=tkinter.Label(courses_frame,text="Registration Status")
reg_status_var=tkinter.StringVar(value="Not registered")#variable that stores info of checkbutton
registered_check=tkinter.Checkbutton(courses_frame,text="Currently Registered",
                                     variable=reg_status_var,onvalue="Registered",offvalue="Not Registered")#enables to get value 4button
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label=tkinter.Label(courses_frame,text="#Completed Courses")
numcourses_spinbox=tkinter.Spinbox(courses_frame,from_=0,to='infinity')
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label=tkinter.Label(courses_frame,text="# Semesters")
numsemesters_spinbox=tkinter.Spinbox(courses_frame,from_=0,to="Infinity")
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

#change padding for all widgets so they are spaced out 
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Accept terms
terms_frame=tkinter.LabelFrame(frame,text="Terms and Conditions")
terms_frame.grid(row=2,column=0,sticky='news',padx=20,pady=20)
accept_var=tkinter.StringVar(value="Not Accepted")
terms_check=tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions.",
                                variable=accept_var,onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=0,column=1)

#button
button=tkinter.Button(frame,text="Enter data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)

#data tree view
data_treeview=ttk.Treeview(frame,columns=("First Name", "Last Name", "Title", "Age", "Nationality", "#Courses", "#Semesters", "Registration status"))
for column in ("First Name", "Last Name", "Title", "Age", "Nationality", "#Courses", "#Semesters", "Registration status"):
    data_treeview.heading(column, text=column)
for column in ("First Name", "Last Name", "Title", "Age", "Nationality", "#Courses", "#Semesters", "Registration status"):
    data_treeview.column(column, width=100)

data_treeview.grid(row=7,column=0,padx=20,pady=10)


window.mainloop()#runs an infinite loop as long as app is running until x is pressed


