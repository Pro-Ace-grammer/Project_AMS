from tkinter import *

root = Tk()

root.title('Student Management System')
root.config(bg="gray17")
root.geometry("1174x700+100+30")


#-----------------------dashborad----------------------

dash_frm= Frame(bg="#8B8B81",relief=SOLID,borderwidth=3)
dash_frm.place(x=9,y=5,width=284,height=50)

dash_lab=Label(root,text="Admin Dashboard",font="harington-20",bg="#8B8B81")
dash_lab.pack()
dash_lab.place(x=20,y=15)


#-------------------------- frames -----------------------

data_entry= Frame(bg="#8B8B81",relief=SOLID,borderwidth=3)
data_entry.place(x=9,y=50,width=300,height=800)

show_data = Frame(bg="#8B8B81",relief=SOLID,borderwidth=3)
show_data.place(x=290,y=50,width=880,height=800)

root.mainloop()