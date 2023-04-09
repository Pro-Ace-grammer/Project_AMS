from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Students Details")

select_year_label = Label(root, text="Select Year")
select_year_label.pack()

year_var = IntVar()
year1_radiobtn = Radiobutton(root, text="1st Year", variable=year_var, value=1)
year2_radiobtn = Radiobutton(root, text="Direct Second Year", variable=year_var, value=2)
year1_radiobtn.pack()
year2_radiobtn.pack()


reg_no_label = Label(root, text="Registration Number").place(x=10,y=80)
reg_no_entry = Entry(root)
reg_no_entry.place(x=150,y=80)
# reg_no_label.pack()
# reg_no_entry.pack()

name_label = Label(root, text="Name").place(x=10,y=100)
name_entry = Entry(root)
name_entry.place(x=150,y=100)
# name_label.pack()
# name_entry.pack()

gender_var = StringVar()
gender = Label(root, text="Gender").place(x=10,y=120)
male_radiobtn = Radiobutton(root, text="Male", variable=gender_var, value="M").place(x=80,y=120)
female_radiobtn = Radiobutton(root, text="Female", variable=gender_var, value="F").place(x=160,y=120)
other_radiobtn = Radiobutton(root, text="Otherec", variable=gender_var, value="O").place(x=240,y=120)

mo_var = BooleanVar()
py_var = BooleanVar()
engg_var = BooleanVar()
prog = Label(root, text="Program").place(x=10,y=140)
mo_radiobtn = Checkbutton(root, text="MO", variable=mo_var).place(x=80,y=140)
py_radiobtn = Checkbutton(root, text="PY", variable=py_var).place(x=160,y=140)
engg_radiobtn = Checkbutton(root, text="ENGG", variable=engg_var).place(x=240,y=140)

root.mainloop()