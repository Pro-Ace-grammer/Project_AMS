from tkinter import *
from tkinter.ttk import Label
import db_pack as db
root = Tk()
root.geometry('800x800')

# function to get the input values when Submit button is clicked
def submit_data():
    reg_no = reg_no_entry.get()
    name = name_entry.get()
    gender = gender_var.get()
    category = category_entry.get()
    math_marks = int(math_marks_entry.get())
    science_marks = int(science_marks_entry.get())
    english_marks = int(english_marks_entry.get())
    total_marks = int(total_marks_entry.get())
    db.submit_form(reg_no,name,gender,category,math_marks,science_marks,english_marks,total_marks)
    # c = con.connect(host='localhost',port='3306',user='root',password='Yash_Arsu_00510',database='pythontest')
    # mycursor = c.cursor()
    # query="insert into testing(reg_no,name,gender,category,math_marks,science_marks,english_marks,total_marks)""values({},'{}','{}','{}',{},{},{},{})".format(reg_no, name, gender, category, math_marks, science_marks, english_marks, total_marks)

    # #mycursor = c.cursor()
    # mycursor.execute(query)
    # c.commit()
    # # do something with the input values here, like storing in a database
    
    # print(reg_no, name, gender, category, math_marks, science_marks, english_marks, total_marks)

# create the form inputs

select_year_label = Label(root, text="Select Year")
select_year_label.pack()

year_var = IntVar()
year1_radiobtn = Radiobutton(root, text="1st Year", variable=year_var, value=1)
year2_radiobtn = Radiobutton(root, text="Direct Second Year", variable=year_var, value=2)
year1_radiobtn.pack()

reg_no_label = Label(root, text="Registration Number")
reg_no_entry = Entry(root)
reg_no_label.pack()
reg_no_entry.pack()

name_label = Label(root, text="Name")
name_entry = Entry(root)
name_label.pack()
name_entry.pack()

gender_label = Label(root, text="Gender")
gender_label.pack()

gender_var = StringVar()
male_radiobtn = Radiobutton(root, text="Male", variable=gender_var, value="Male")
female_radiobtn = Radiobutton(root, text="Female", variable=gender_var, value="Female")
male_radiobtn.pack()
female_radiobtn.pack()

category_label = Label(root, text="Category")
category_entry = Entry(root)
category_label.pack()
category_entry.pack()

math_marks_label = Label(root, text="Maths Marks")
math_marks_entry = Entry(root)
math_marks_label.pack()
math_marks_entry.pack()

science_marks_label = Label(root, text="Science Marks")
science_marks_entry = Entry(root)
science_marks_entry.pack()
science_marks_label.pack()

english_marks_label = Label(root, text="English Marks")
english_marks_entry = Entry(root)
english_marks_label.pack()
english_marks_entry.pack()

total_marks_label = Label(root, text="Total Marks")
total_marks_entry = Entry(root)
total_marks_label.pack()
total_marks_entry.pack()

submit_btn = Button(root, text="Submit", command=submit_data)
submit_btn.pack()

root.mainloop()