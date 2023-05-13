from customtkinter import *
# import main_db as db



#----------If not entered--------------


#----------If not entered--------------
def not_entered():
    enroot = CTkToplevel()
    enroot.grab_set()
    enroot.geometry("350x100")
    ssc_label=CTkLabel(enroot, text="Please select and enter the HSSC Total marks" ,font=('Helvetica', 14))
    ssc_label.place(x=10,y=10)
    ok_button = CTkButton(enroot, text ='okay',command = enroot.grab_release)
    ok_button.place(x=100,y=50)
    enroot.mainloop()


#----------------DATBASE FOR SECOND YEAR--------------------
def submit_data_SY():
    reg_no = int(s_reg_no_entry.get())
    name = s_name_entry.get()
    gender = s_gender_var.get()
    hssc_if = s_hssc_var.get()
    voc_if = s_voc_var.get()
    iti_if = s_iti_var.get()
    ssc_eng = int(s_ssc_eng_entry.get())
    ssc_mat = int(s_ssc_mat_entry.get())
    ssc_sci = int(s_ssc_sci_entry.get())
    ssc_tot = int(s_ssc_total_entry.get())
    



    db.submit_form_FY(reg_no,name,gender,hssc_if,voc_if,iti_if,str(ssc_eng),str(ssc_mat),str(ssc_sci),str(ssc_tot))

