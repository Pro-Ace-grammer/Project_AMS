from tkinter import *
from customtkinter import *

#--------Main window--------
app=CTk()
width= app.winfo_screenwidth()               
height= app.winfo_screenheight() 
# app.resizable(width=FALSE, height=FALSE)
app.geometry("%dx%d" %(width,height))
app.title("App")

#--------Functions--------
def year1():
    s_year_frame.grid_forget()
    f_year_frame.grid_propagate(0)
    f_year_frame.grid(row=0,column=1)    

def year2():
    f_year_frame.grid_forget()
    s_year_frame.grid_propagate(0)
    s_year_frame.grid(row=0,column=1)







# frame1 = customtkinter.CTkFrame(master=root_tk, width=200, height=200)
frame1=CTkFrame(app,width=185,height=height)
frame1.grid(row=0,column=0,padx=5,pady=5)
frame1.grid_propagate(0)

year_var=IntVar()
year_var.set(1)

f_year_button=CTkRadioButton(frame1,text="1st Year",height=10,width=10,value=1,variable=year_var,command=year1)
f_year_button.grid(padx=10,pady=10)

s_year_buton=CTkRadioButton(frame1,text="2nd Year",height=10,width=10,value=2,variable=year_var,command=year2)
s_year_buton.grid(padx=10,pady=10)



f_year_frame=CTkFrame(app,width=1165,height=height)
f_year_frame.grid(row=0,column=1)
f_year_frame.grid_propagate(0)
f_label=CTkLabel(f_year_frame,text='1st year')
f_label.grid()



s_year_frame=CTkFrame(app,width=1165,height=height)
s_label=CTkLabel(s_year_frame,text='2nd year')
s_year_frame.grid_propagate(0)
s_label.grid()

app.mainloop()
