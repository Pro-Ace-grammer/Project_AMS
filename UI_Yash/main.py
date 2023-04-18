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
    f_year_frame.grid_propagate()
    # f_year_frame.grid(row=0,column=1) 
    f_year_frame.grid(row=0,column=1,sticky="N",padx=5,pady=5)   



def year2():
    f_year_frame.grid_forget()
    s_year_frame.grid_propagate(0)
    # s_year_frame.grid(row=0,column=1)
    s_year_frame.grid(row=0,column=1,sticky="N",padx=5,pady=5)   







frame1=CTkFrame(app,width=185,height=height)
frame1.grid(row=0,column=0,padx=5,pady=5,sticky="E")
frame1.grid_propagate(0)

year_var=IntVar()
year_var.set(1)

f_year_button=CTkRadioButton(frame1,text="1st Year",height=10,width=10,value=1,variable=year_var,command=year1)
f_year_button.grid(padx=10,pady=10)

s_year_buton=CTkRadioButton(frame1,text="2nd Year",height=10,width=10,value=2,variable=year_var,command=year2)
s_year_buton.grid(padx=10,pady=10)





#--------First Year Frame--------
f_year_frame=CTkScrollableFrame(app,width=1150,height=height-80,orientation="vertical")
f_year_frame.grid(row=0,column=1,sticky="N",padx=5,pady=5)
f_year_frame.grid_propagate()
# f_label=CTkLabel(f_year_frame,text='1st year')
# f_label.grid()


#--------Frame content--------
reg_no_label = CTkLabel(f_year_frame, text="Registration Number")
reg_no_label.grid(padx=500,pady=5)
reg_no_entry = CTkEntry(f_year_frame)
reg_no_entry.grid(padx=500,pady=5)



name_var=StringVar()

name_label = CTkLabel(f_year_frame, text="Name")
name_label.grid(padx=500,pady=10)
name_entry =CTkEntry(f_year_frame)
name_entry.grid(padx=500,pady=10)


gender_var = StringVar()
gender = CTkLabel(f_year_frame, text="Gender")
gender.grid(padx=500,pady=10)

male_radiobtn = CTkRadioButton(f_year_frame, text="Male", variable=gender_var, value="M")
male_radiobtn.grid(padx=500,pady=10)
female_radiobtn = CTkRadioButton(f_year_frame, text="Female", variable=gender_var, value="F")
female_radiobtn.grid(padx=500,pady=10)
other_radiobtn =CTkRadioButton(f_year_frame, text="Other", variable=gender_var, value="O")
other_radiobtn.grid(padx=500,pady=10)



#--------MO_PY_ENGG--------


#--------Function to validate HSSC fields based on MO PY and ENGG--------
def disab_enab():

    if(((engg_var.get()==True) and (py_var.get()==False and mo_var.get()==False)) or( engg_var.get()==False and py_var.get()==False and mo_var.get()==False)):
        hssc_eng_entry.configure(state="disabled")
        hssc_eng_label.configure(state="disabled")
        hssc_phy_entry.configure(state="disabled")
        hssc_phy_label.configure(state="disabled")
        hssc_che_entry.configure(state="disabled")
        hssc_che_label.configure(state="disabled")
        hssc_bio_entry.configure(state="disabled")
        hssc_bio_label.configure(state="disabled")
        hssc_a_radiobtn.configure(state="disabled")
        hssc_c_radiobtn.configure(state="disabled")
        hssc_s_radiobtn.configure(state="disabled")
        hssc_v_radiobtn.configure(state="disabled")
    else:
        hssc_eng_entry.configure(state="normal")
        hssc_eng_label.configure(state="normal")
        hssc_phy_entry.configure(state="normal")
        hssc_phy_label.configure(state="normal")
        hssc_che_entry.configure(state="normal")
        hssc_che_label.configure(state="normal")
        hssc_bio_entry.configure(state="normal")
        hssc_bio_label.configure(state="normal")
        hssc_a_radiobtn.configure(state="normal")
        hssc_c_radiobtn.configure(state="normal")
        hssc_s_radiobtn.configure(state="normal")
        hssc_v_radiobtn.configure(state="normal")








mo_var = BooleanVar()
py_var = BooleanVar()
engg_var = BooleanVar()
program = CTkLabel(f_year_frame, text="Program:")
program.grid(padx=500,pady=10)
mo_btn = CTkCheckBox(f_year_frame, text="MO", variable=mo_var ,command=disab_enab)
mo_btn.grid(padx=500,pady=10)
py_btn = CTkCheckBox(f_year_frame, text="PY", variable=py_var ,command=disab_enab)
py_btn.grid(padx=500,pady=10)
engg_btn = CTkCheckBox(f_year_frame, text="ENGG", variable=engg_var ,command=disab_enab)
engg_btn.grid(padx=500,pady=10)




#--------GEN/CSP--------




gen_csp_var= StringVar()
gen_csp_label = CTkLabel(f_year_frame, text="GEN/CSP:" )
gen_csp_label.grid(padx=500,pady=10)

gen_radiobtn = CTkRadioButton(f_year_frame, text="GEN",variable=gen_csp_var, value="GEN")
gen_radiobtn.grid(padx=500,pady=10)



csp_radiobtn = CTkRadioButton(f_year_frame,text="CSP", variable=gen_csp_var, value="CSP")
csp_radiobtn.grid(padx=500,pady=10)



#--------SC/ST/OBC--------
sc_st_obc_var= StringVar()
sc_st_obc_label = CTkLabel(f_year_frame, text="SC/ST/OBC:")
sc_st_obc_label.grid(padx=500,pady=10)

sc_radiobtn = CTkRadioButton(f_year_frame, text="SC",variable=sc_st_obc_var, value="SC")
sc_radiobtn.grid(padx=500,pady=10)

st_radiobtn = CTkRadioButton(f_year_frame,text="ST", variable=sc_st_obc_var, value="ST")
st_radiobtn.grid(padx=500,pady=10)

obc_radiobtn = CTkRadioButton(f_year_frame,text="OBC", variable=sc_st_obc_var, value="OBC")
obc_radiobtn.grid(padx=500,pady=10)


#--------PwD/FF/ESM--------

pwd_ff_esm_var=StringVar()
pwd_ff_esm_label=CTkLabel(f_year_frame, text="PwD/FF/ESM")
pwd_ff_esm_label.grid(padx=500,pady=10)

pwd_radiobtn = CTkRadioButton(f_year_frame, text="PwD",variable=sc_st_obc_var, value="PwD")
pwd_radiobtn.grid(padx=500,pady=10)

ff_radiobtn = CTkRadioButton(f_year_frame,text="FF", variable=sc_st_obc_var, value="FF")
ff_radiobtn.grid(padx=500,pady=10)

esm_radiobtn = CTkRadioButton(f_year_frame,text="ESM", variable=sc_st_obc_var, value="ESM")
esm_radiobtn.grid(padx=500,pady=10)




#--------GN/NRI/LA/OGA--------

gn_nri_la_oga_var=StringVar()

gn_nri_la_oga_label=CTkLabel(f_year_frame, text="GN/NRI/LA/OGA")
gn_nri_la_oga_label.grid(padx=500,pady=10)

gn_radiobtn = CTkRadioButton(f_year_frame, text="GN",variable=gn_nri_la_oga_var, value="GN")
gn_radiobtn.grid(padx=500,pady=10)

nri_radiobtn = CTkRadioButton(f_year_frame,text="NRI", variable=gn_nri_la_oga_var, value="NRI")
nri_radiobtn.grid(padx=500,pady=10)

la_radiobtn = CTkRadioButton(f_year_frame,text="LA", variable=gn_nri_la_oga_var, value="LA")
la_radiobtn.grid(padx=500,pady=10)


oga_radiobtn = CTkRadioButton(f_year_frame,text="OGA", variable=gn_nri_la_oga_var, value="OGA")
oga_radiobtn.grid(padx=500,pady=10)







ssc_label=CTkLabel(f_year_frame, text="SSC  marks:" ,font=('Helvetica', 24))
ssc_label.grid(padx=500,pady=5)

ssc_eng_label=CTkLabel(f_year_frame, text="SSC English marks:")
ssc_eng_label.grid(padx=500,pady=5)
ssc_eng_entry = CTkEntry(f_year_frame)
ssc_eng_entry.grid(padx=500,pady=5)




ssc_mat_label=CTkLabel(f_year_frame, text="SSC Maths marks:")
ssc_mat_label.grid(padx=500,pady=5)
ssc_mat_entry = CTkEntry(f_year_frame)
ssc_mat_entry.grid(padx=500,pady=5)




ssc_sci_label=CTkLabel(f_year_frame, text="SSC Science marks:")
ssc_sci_label.grid(padx=500,pady=5)
ssc_sci_entry = CTkEntry(f_year_frame)
ssc_sci_entry.grid(padx=500,pady=5)




ssc_total_label=CTkLabel(f_year_frame, text="SSC Total marks:" )
ssc_total_label.grid(padx=500,pady=5)
ssc_total_entry = CTkEntry(f_year_frame)
ssc_total_entry.grid(padx=500,pady=5)








#--------HSSC Marks--------

hssc_label=CTkLabel(f_year_frame, text="HSSC  marks:" ,font=('Helvetica', 24))
hssc_label.grid(padx=500,pady=5)

hssc_eng_label=CTkLabel(f_year_frame, text="HSSC English marks:",state="disabled")
hssc_eng_label.grid(padx=500,pady=5)
hssc_eng_entry = CTkEntry(f_year_frame,state="disabled")
hssc_eng_entry.grid(padx=500,pady=5)




hssc_phy_label=CTkLabel(f_year_frame, text="HSSC Physics marks:",state="disabled")
hssc_phy_label.grid(padx=500,pady=5)
hssc_phy_entry = CTkEntry(f_year_frame,state="disabled")
hssc_phy_entry.grid(padx=500,pady=5)




hssc_che_label=CTkLabel(f_year_frame, text="HSSC Chemistry marks:",state="disabled")
hssc_che_label.grid(padx=500,pady=5)
hssc_che_entry = CTkEntry(f_year_frame,state="disabled")
hssc_che_entry.grid(padx=500,pady=5)




hssc_bio_label=CTkLabel(f_year_frame, text="HSSC Biology marks:" ,state="disabled")
hssc_bio_label.grid(padx=500,pady=5)
hssc_bio_entry = CTkEntry(f_year_frame,state="disabled")
hssc_bio_entry.grid(padx=500,pady=5)





#--------HSSC RadioButtons--------

#--------Function to validate HSSC total marks  based on radio buttons--------
def hssc_total():
    print(hssc_total_var.get())

    if(hssc_total_var.get()=="HSSC A"):

        hssc_a_total_entry.configure(state="normal")
        hssc_a_total_label.configure(state="normal")
        hssc_c_total_entry.configure(state="disabled")
        hssc_c_total_label.configure(state="disabled")
        hssc_s_total_entry.configure(state="disabled")
        hssc_s_total_label.configure(state="disabled")
        hssc_v_total_entry.configure(state="disabled")
        hssc_v_total_label.configure(state="disabled")

    elif(hssc_total_var.get()=="HSSC C"):

        hssc_a_total_entry.configure(state="disabled")
        hssc_a_total_label.configure(state="disabled")
        hssc_c_total_entry.configure(state="normal")
        hssc_c_total_label.configure(state="normal")
        hssc_s_total_entry.configure(state="disabled")
        hssc_s_total_label.configure(state="disabled")
        hssc_v_total_entry.configure(state="disabled")
        hssc_v_total_label.configure(state="disabled")

    elif(hssc_total_var.get()=="HSSC S"):

        hssc_a_total_entry.configure(state="disabled")
        hssc_a_total_label.configure(state="disabled")
        hssc_c_total_entry.configure(state="disabled")
        hssc_c_total_label.configure(state="disabled")
        hssc_s_total_entry.configure(state="normal")
        hssc_s_total_label.configure(state="normal")
        hssc_v_total_entry.configure(state="disabled")
        hssc_v_total_label.configure(state="disabled")

    else:

        hssc_a_total_entry.configure(state="disabled")
        hssc_a_total_label.configure(state="disabled")
        hssc_c_total_entry.configure(state="disabled")
        hssc_c_total_label.configure(state="disabled")
        hssc_s_total_entry.configure(state="disabled")
        hssc_s_total_label.configure(state="disabled")
        hssc_v_total_entry.configure(state="normal")
        hssc_v_total_label.configure(state="normal")







hssc_total_var=StringVar()


hssc_type_label=CTkLabel(f_year_frame, text="HSSC :")
hssc_type_label.grid(padx=500,pady=10)

hssc_a_radiobtn = CTkRadioButton(f_year_frame, text="HSSC A",variable=hssc_total_var,value="HSSC A",command=hssc_total,state="disabled")
hssc_a_radiobtn.grid(padx=500,pady=10)

hssc_c_radiobtn = CTkRadioButton(f_year_frame,text="HSSC C", variable=hssc_total_var,value="HSSC C",command=hssc_total,state="disabled")
hssc_c_radiobtn.grid(padx=500,pady=10)

hssc_s_radiobtn = CTkRadioButton(f_year_frame,text="HSSC S", variable=hssc_total_var,value="HSSC S",command=hssc_total,state="disabled")
hssc_s_radiobtn.grid(padx=500,pady=10)


hssc_v_radiobtn = CTkRadioButton(f_year_frame,text="HSSC V", variable=hssc_total_var,value="HSSC V",command=hssc_total,state="disabled")
hssc_v_radiobtn.grid(padx=500,pady=10)

#------HSSC Total Entry--------





hssc_a_total_var=StringVar()
hssc_c_total_var=StringVar()
hssc_s_total_var=StringVar()
hssc_v_total_var=StringVar()


hssc_total_label=CTkLabel(f_year_frame, text="HSSC Total marks:" )
hssc_total_label.grid(padx=500,pady=5)

hssc_a_total_label=CTkLabel(f_year_frame, text="HSSC A total marks",state="disabled")
hssc_a_total_label.grid(padx=500,pady=5)
hssc_a_total_entry = CTkEntry(f_year_frame,textvariable=hssc_a_total_var,state="disabled")
hssc_a_total_entry.grid(padx=500,pady=5)




hssc_c_total_label=CTkLabel(f_year_frame, text="HSSC C total marks",state="disabled")
hssc_c_total_label.grid(padx=500,pady=5)
hssc_c_total_entry = CTkEntry(f_year_frame,textvariable=hssc_c_total_var,state="disabled")
hssc_c_total_entry.grid(padx=500,pady=5)




hssc_s_total_label=CTkLabel(f_year_frame, text="HSSC S total marks",state="disabled")
hssc_s_total_label.grid(padx=500,pady=5)
hssc_s_total_entry = CTkEntry(f_year_frame,textvariable=hssc_s_total_var,state="disabled")
hssc_s_total_entry.grid(padx=500,pady=5)




hssc_v_total_label=CTkLabel(f_year_frame, text="HSSC V total marks",state="disabled")
hssc_v_total_label.grid(padx=500,pady=5)
hssc_v_total_entry = CTkEntry(f_year_frame,textvariable=hssc_v_total_var,state="disabled")
hssc_v_total_entry.grid(padx=500,pady=5)














#--------First Year Frame Ends------











s_year_frame=CTkFrame(app,width=1165,height=height)
s_label=CTkLabel(s_year_frame,text='2nd year')
s_year_frame.grid_propagate(0)
s_label.grid()

app.mainloop()
