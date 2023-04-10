import customtkinter as ctk
root = ctk.CTk()
root.geometry("600x600")
root.title("Students Details")





#elect_year_label = CTkLabel(root, text="Select Year")
#select_year_label.pack()

year_var = ctk.IntVar()
year1_radiobtn = ctk.CTkRadioButton(root, text="1st Year", variable=year_var, value=1)
year2_radiobtn = ctk.CTkRadioButton(root, text="Direct Second Year", variable=year_var, value=2)
year1_radiobtn.pack()
year2_radiobtn.pack()


reg_no_label = ctk.CTkLabel(root, text="Registration Number").place(x=10,y=80)
reg_no_entry = ctk.CTkEntry(root)
reg_no_entry.place(x=150,y=80)
# reg_no_label.pack()
# reg_no_entry.pack()

name_label = ctk.CTkLabel(root, text="Name").place(x=10,y=100)
name_entry =ctk.CTkEntry(root)
name_entry.place(x=150,y=100)
# name_label.pack()
# name_entry.pack()

gender_var = ctk.StringVar()
gender = ctk.CTkLabel(root, text="Gender").place(x=10,y=120)
male_radiobtn = ctk.CTkRadioButton(root, text="Male", variable=gender_var, value="M").place(x=80,y=120)
female_radiobtn = ctk.CTkRadioButton(root, text="Female", variable=gender_var, value="F").place(x=160,y=120)
other_radiobtn =ctk.CTkRadioButton(root, text="Otherec", variable=gender_var, value="O").place(x=240,y=120)

mo_var = ctk.BooleanVar()
py_var = ctk.BooleanVar()
engg_var = ctk.BooleanVar()
prog = ctk.CTkLabel(root, text="Program").place(x=10,y=140)
mo_radiobtn = ctk.CTkCheckBox(root, text="MO", variable=mo_var).place(x=80,y=140)
py_radiobtn = ctk.CTkCheckBox(root, text="PY", variable=py_var).place(x=160,y=140)
engg_radiobtn = ctk.CTkCheckBox(root, text="ENGG", variable=engg_var).place(x=240,y=140)



root.mainloop()