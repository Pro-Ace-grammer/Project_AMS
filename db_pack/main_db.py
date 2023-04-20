import mysql.connector as con
def submit_form(reg_no,name,gender,category,math_marks,science_marks,english_marks,total_marks):
    # reg_no = reg_no_entry.get()
    # name = name_entry.get()
    # gender = gender_var.get()
    # category = category_entry.get()
    # math_marks = math_marks_entry.get()
    # science_marks = science_marks_entry.get()
    # english_marks = english_marks_entry.get()
    # total_marks = total_marks_entry.get()
    c = con.connect(host='localhost',port=3306,user='root',password='Yash_Arsu_00510',database='pythontest')
    mycursor = c.cursor()
    query="insert into testing(reg_no,name,gender,category,math_marks,science_marks,english_marks,total_marks)""values({},'{}','{}','{}',{},{},{},{})".format(reg_no, name, gender, category, math_marks, science_marks, english_marks, total_marks)

    #mycursor = c.cursor()
    mycursor.execute(query)
    c.commit()
    # do something with the input values here, like storing in a database
    
    print(reg_no, name, gender, category, math_marks, science_marks, english_marks, total_marks)