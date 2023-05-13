from tkinter import *
import mysql.connector as con
import tkinter.messagebox as mb
import pandas as pd

# root = Tk()
# root.geometry("600x700")



c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
cursor = c.cursor()
sql ="select * from all_student"
# data = pd.read_sql(sql, c)
# pd.DataFrame(data)
cursor.execute(sql)
data = cursor.fetchall()
sh = pd.read_sql_table(data, c)
sh.head()
# listt = Listbox(root)
# listt.place(x=5,y=5,width=500,height=700)
# show()

# root.mainloop()

 