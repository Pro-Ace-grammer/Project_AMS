# from tkinter import *
from customtkinter import *
from tkinter import *
from tkinter import ttk
import main_db as db
import mysql.connector as con



#----------------DATBASE--------------------
def submit_data_FY():

    reg_no = int(reg_no_entry.get())
    str1 = name_entry.get()
    name = str1.upper()
    gender = gender_var.get()


    mo = mo_var.get()
    py = py_var.get()
    engg = engg_var.get()


    gen_csp = gen_csp_var.get()
    sc_st_obc = sc_st_obc_var.get()
    pwd_esm = pwd_esm_var.get()
    gn_nri_la_oga = gn_nri_la_oga_var.get()


    ssc_eng = int(ssc_eng_entry.get())
    ssc_sci = int(ssc_sci_entry.get())
    ssc_mat = int(ssc_mat_entry.get())
    ssc_total= int(ssc_total_entry.get())

    if (ssc_ad_entry.get()=="" or ssc_ad_entry.get()==" "):
        ssc_AD=0
        ssc_q_total = ssc_total
    else:
        ssc_AD = int(ssc_ad_entry.get())
        ssc_q_total = ssc_total+ssc_AD 

    if(mo_var.get() ==True or py_var.get() == True):
        hssc_eng = hssc_eng_entry.get()
        hssc_phy  = hssc_phy_entry.get()
        hssc_che = hssc_che_entry.get()
        hssc_math = hssc_math_entry.get()
        hssc_bio = hssc_bio_entry.get()
    else:
        hssc_eng = 0
        hssc_phy = 0
        hssc_che = 0
        hssc_math = 0
        hssc_bio = 0



    if(mo_var.get() ==True or py_var.get() == True):
        pcm = hssc_phy + hssc_che + hssc_math
        pcb = hssc_phy + hssc_che + hssc_bio
        if(pcm>=pcb):
            pcm_b = pcm
        elif(pcm<=pcb):
            pcm_b = pcb
        else:
            pcm_b = 0
        if(hssc_math>=hssc_bio):
            mat_bio = hssc_math
        elif(hssc_math>=hssc_bio):
            mat_bio = hssc_bio
        else:
            mat_bio = 0
    else:
        pcm = 0
        pcb = 0
        pcm_b = 0
        mat_bio = 0
        

    
    

    if(mo_var.get() ==True or py_var.get() == True):

        hssc_a_total = hssc_a_total_var.get()
        hssc_c_total = hssc_c_total_var.get()
        hssc_s_total = hssc_s_total_var.get()
        hssc_v_total = hssc_v_total_var.get()

        if(hssc_total_var.get() == "HSSC V"):
            hssc_all = (hssc_v_total * 600)//800
        elif(hssc_total_var.get() == "HSSC A"):
            hssc_all = hssc_a_total
        elif(hssc_total_var.get() == "HSSC C"):
            hssc_all = hssc_c_total
        else:
            hssc_all = hssc_s_total
        hssc_ad = hssc_ad_entry.get()
        hssc_q_tot = hssc_all + hssc_ad
        hssc_per = (hssc_all/600)*100
    else:

        hssc_per = 0
        hssc_all = 0
        hssc_a_total = 0
        hssc_c_total = 0
        hssc_s_total = 0
        hssc_v_total = 0
        hssc_ad = 0
        hssc_q_tot = 0



    el="EL"
    ne="NE"
    na="NA"

    ssc_per = (ssc_total/600)*100

    if(engg_var.get()==True):
        if(ssc_per>=35):
            ENGG = el
        else:
            ENGG = ne
    else:
        ENGG = na


    if(py_var.get()==True):
        if(hssc_per>=35):
            PY = el
        else:
            PY = ne
    else:
        PY = na


    if(mo_var.get()==True):
        if(hssc_per>=35):
            MO = el
        else:
            MO = ne
    else:
        MO = na

            
    fy_remarks = fy_remarks_entry.get()
    
    db.submit_form(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks)
    #there are some fields I need to put here 
    


    




#--------Function to clear all fields--------
def clear():
   register_var=''
   reg_no_entry.delete(0,END)
   name_var=''
   name_entry.delete(0,END)
   gender_var=''
   male_radiobtn.deselect()
   female_radiobtn.deselect()
   other_radiobtn.deselect()
   mo_var.set(0)
   py_var.set(0)
   engg_var.set(0)
   gen_csp_var=''
   gen_radiobtn.deselect()
   csp_radiobtn.deselect()
   sc_st_obc_var=''
   sc_radiobtn.deselect()
   st_radiobtn.deselect()
   obc_radiobtn.deselect()
   pwd_esm_var=''
   pwd_radiobtn.deselect()
   esm_radiobtn.deselect()
   gn_nri_la_oga_var=''
   gn_radiobtn.deselect()
   nri_radiobtn.deselect()
   la_radiobtn.deselect()
   oga_radiobtn.deselect()
   ssc_eng_entry.delete(0,END)
   ssc_mat_entry.delete(0,END)
   ssc_sci_entry.delete(0,END)
   ssc_total_entry.delete(0,END)
   hssc_eng_entry.delete(0,END)
   hssc_phy_entry.delete(0,END)
   hssc_che_entry.delete(0,END)
   hssc_math_entry.delete(0,END)
   hssc_bio_entry.delete(0,END)
   hssc_eng_entry.configure(placeholder_text='')
   hssc_phy_entry.configure(placeholder_text='')
   hssc_che_entry.configure(placeholder_text='')
   hssc_math_entry.configure(placeholder_text='')
   hssc_bio_entry.configure(placeholder_text='')
   hssc_eng_entry.configure(state='disabled')
   hssc_phy_entry.configure(state='disabled')
   hssc_che_entry.configure(state='disabled')
   hssc_math_entry.configure(state='disabled')
   hssc_bio_entry.configure(state='disabled')
   hssc_total_var=''
   hssc_a_radiobtn.deselect()
   hssc_a_radiobtn.configure(state='disabled')
   hssc_c_radiobtn.deselect()
   hssc_c_radiobtn.configure(state='disabled')
   hssc_s_radiobtn.deselect()
   hssc_s_radiobtn.configure(state='disabled')
   hssc_v_radiobtn.deselect()
   hssc_v_radiobtn.configure(state='disabled')
   hssc_a_total_var=''
   hssc_c_total_var=''
   hssc_s_total_var=''
   hssc_v_total_var=''
   hssc_a_total_entry.delete(0,END)
   hssc_c_total_entry.delete(0,END)
   hssc_s_total_entry.delete(0,END)
   hssc_v_total_entry.delete(0,END)
   hssc_a_total_entry.configure(state='disabled')
   hssc_c_total_entry.configure(state='disabled')
   hssc_s_total_entry.configure(state='disabled')
   hssc_v_total_entry.configure(state='disabled')
   fy_remarks_var=''
   fy_remarks_entry.delete(0,END)
   ssc_ad_entry.delete(0,END)
   hssc_ad_entry.configure(placeholder_text="")
   hssc_ad_entry.delete(0,END)
   hssc_ad_entry.configure(state='disabled')
   hssc_label.configure(state='disabled')
   hssc_type_label.configure(state='disabled')
   hssc_total_label.configure(state='disabled')
   ssc_eng_entry.configure(placeholder_text='English')
   ssc_mat_entry.configure(placeholder_text='Maths')
   ssc_sci_entry.configure(placeholder_text='Science')
   ssc_total_entry.configure(placeholder_text='Total')
   ssc_ad_entry.configure(placeholder_text='AD marks')



#--------Clear function for second year form--------

def s_clear():
   s_register_var=''
   s_reg_no_entry.delete(0,END)
   s_name_var=''
   s_name_entry.delete(0,END)
   s_hssc_ad_entry.delete(0,END)
   s_hssc_ad_total_label.configure(state='disabled')
   s_hssc_ad_entry.configure(state='disabled')
   
   s_gender_var=''
   s_male_radiobtn.deselect()
   s_female_radiobtn.deselect()
   s_other_radiobtn.deselect()


   s_ssc_ad_entry.delete(0,END)


   s_hssc_var=''
   s_voc_var=''
   s_iti_var=''
   s_course_var=''

   s_hssc_radiobtn.deselect()
   s_voc_radiobtn.deselect()
   s_iti_radiobtn.deselect()
   s_voc_drop.set('')
   s_iti_drop.set('')
   s_hssc_mat_var=''
   s_hssc_mat_total_entry.delete(0,END)
   s_hssc_s=''
   s_hssc_s_entry.delete(0,END)
   s_hssc_v=''
   s_hssc_v_entry.delete(0,END)
   s_iti_total=''
   s_iti_total_entry.delete(0,END)
   s_voc_drop_label.configure(state="disabled")
   s_voc_drop.configure(state="disabled")
   s_iti_drop_label.configure(state="disabled")
   s_iti_drop.configure(state="disabled")
   s_hssc_mat_total_entry.delete(0,END)
   s_hssc_s_entry.delete(0,END)
   s_hssc_v_entry.delete(0,END)
   s_iti_total_entry.delete(0,END)
   s_hssc_mat_var=''
   s_hssc_s=''
   s_hssc_v=''
   s_iti_total=''






   s_ssc_eng_entry.delete(0,END)
   s_ssc_eng_entry.configure(placeholder_text="English")
   s_ssc_mat_entry.delete(0,END)
   s_ssc_mat_entry.configure(placeholder_text="Maths")
   s_ssc_sci_entry.delete(0,END)
   s_ssc_sci_entry.configure(placeholder_text="Science")
   s_ssc_total_entry.delete(0,END)
   s_ssc_total_entry.configure(placeholder_text="Total")
   s_ssc_ad_entry.delete(0,END)
   s_ssc_ad_entry.configure(placeholder_text="SSC AD")

   sy_remarks_var=''
   sy_remarks_entry.delete(0,END)

   s_hssc_s_total_label.configure(state='disabled')
   s_hssc_s_entry.configure(state='disabled')
   s_hssc_v_total_label.configure(state='disabled')
   s_hssc_v_entry.configure(state='disabled')
   
   s_iti_total_label.configure(state='disabled')
   hssc_a_total_entry.configure(state='disabled')
   s_iti_total_entry.configure(state='disabled')
   hssc_a_total_entry.configure(state='disabled')
 
   s_hssc_mat_total_label.configure(state='disabled')
   s_hssc_mat_total_entry.configure(state='disabled')

   s_hssc_ad_total_label.configure(state='disabled')
   s_hssc_ad_entry.configure(state='disabled')
   


#--------Main window--------
app=CTk()
width= app.winfo_screenwidth()               
height= app.winfo_screenheight() 
set_appearance_mode("system")
# app.resizable(width=FALSE, height=FALSE)
app.geometry("%dx%d+0+0" %(width,height))
app.title("App")
# print(width)
# print(height)

#--------Functions--------
mode=True
def change_mode():
    global mode
    if(mode==True):
        mode=False
        set_appearance_mode("dark")
    else:
        mode=True
        set_appearance_mode("light")

def year1():
    s_year_frame.grid_forget()
    # f_year_frame.grid_propagate()
    f_year_frame.grid(row=0,column=1,sticky="N",padx=5,pady=5)   



def year2():
    f_year_frame.grid_forget()
    # s_year_frame.grid_propagate()
    s_year_frame.grid(row=0,column=1,sticky="N",padx=5,pady=5)   






f_width=13.616398243*width/100
year_frame_width=84.1874084919*width/100
frame1=CTkFrame(app,width=f_width,height=height)
frame1.grid(row=0,column=0,padx=10,pady=5,sticky="E")
frame1.grid_propagate(0)

year_var=IntVar()
year_var.set(1)

f_year_button=CTkRadioButton(frame1,text="1st Year",height=10,width=10,value=1,variable=year_var,command=year1)
f_year_button.grid(padx=10,pady=10)

s_year_buton=CTkRadioButton(frame1,text="2nd Year",height=10,width=10,value=2,variable=year_var,command=year2)
s_year_buton.grid(padx=10,pady=10)

win=CTk()









#--------SHOW DATA FUNCTION--------
def show_data_window():

    show_window=CTkToplevel(win)
    show_window.geometry("%dx%d+0+0" %(width,height))
    show_window.title("Show Data")

    
    show_year_var=''

    def change_year1():

        
        s_show_btn.place_forget()
        show_btn.place_forget()

        # canvas=CTkCanvas(show_window,height=height,width=width,background='#2B2B2B')
        # canvas.grid(row=0,column=0)
        # canvas.grid_propagate(0)
        canvas=CTkScrollableFrame(show_window,height=height-100,width=width-20,orientation="horizontal")
        canvas.grid(row=0,column=0)
        canvas.grid_propagate()

        
   
        
       
        
        
        
        
        # #Add a Vertical Scrollbar
        # scroll_v = CTkScrollbar(canvas)
        # scroll_v.grid(row=0,column=0)

        # #Add a Horizontal Scrollbar
        # scroll_h = CTkScrollbar(canvas, orientation= HORIZONTAL)
        # scroll_h.grid(column=0,sticky='S')







        id_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        id_head.insert(0,'REGNO')
        id_head.grid(row=0,padx=2,column=0,pady=10)
        id_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=200,border_width=1)
        name_head.insert(0,'NAME')
        name_head.grid(row=0,padx=2,column=1,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'GEN')
        name_head.grid(row=0,padx=2,column=2,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'MO')
        name_head.grid(row=0,padx=2,column=3,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'PY')
        name_head.grid(row=0,padx=2,column=4,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'ENGG')
        name_head.grid(row=0,padx=2,column=5,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'GEN.CSP')
        name_head.grid(row=0,padx=2,column=6,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'SC.ST.OBC')
        name_head.grid(row=0,padx=2,column=7,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'PwD.ESM')
        name_head.grid(row=0,padx=2,column=8,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'GN.NRI.LA.OGA')
        name_head.grid(row=0,padx=2    ,column=9,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'SSC.ENG')
        name_head.grid(row=0,padx=2,column=10,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'MAT')
        name_head.grid(row=0,padx=2,column=11,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'SCI')
        name_head.grid(row=0,padx=2,column=12,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'TOTAL')
        name_head.grid(row=0,padx=2,column=13,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'AD')
        name_head.grid(row=0,padx=2,column=14,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'Q.TOTAL')
        name_head.grid(row=0,padx=2,column=15,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC.ENG')
        name_head.grid(row=0,padx=2,column=16,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'PHY')
        name_head.grid(row=0,padx=2,column=17,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'CHE')
        name_head.grid(row=0,padx=2,column=18,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'MAT')
        name_head.grid(row=0,padx=2,column=19,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'BIO')
        name_head.grid(row=0,padx=2,column=20,pady=10)
        name_head.configure(state='readonly')


        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'PCM')
        name_head.grid(row=0,padx=2,column=21,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'PCB')
        name_head.grid(row=0,padx=2,column=22,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'PCM/B')
        name_head.grid(row=0,padx=2,column=23,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'MAT/BIO')
        name_head.grid(row=0,padx=2,column=24,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC-A')
        name_head.grid(row=0,padx=2,column=25,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC-C')
        name_head.grid(row=0,padx=2,column=26,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC-S')
        name_head.grid(row=0,padx=2,column=27,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC-V')
        name_head.grid(row=0,padx=2,column=28,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC-ALL')
        name_head.grid(row=0,padx=2,column=29,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC.AD')
        name_head.grid(row=0,padx=2,column=30,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'Q.TOTAL')
        name_head.grid(row=0,padx=2,column=31,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'SSC %')
        name_head.grid(row=0,padx=2,column=32,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'HSSC %')
        name_head.grid(row=0,padx=2,column=33,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'ENGG')
        name_head.grid(row=0,padx=2,column=34,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'PY')
        name_head.grid(row=0,padx=2,column=35,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=100,border_width=1)
        name_head.insert(0,'MO')
        name_head.grid(row=0,padx=2,column=36,pady=10)
        name_head.configure(state='readonly')



        name_head=CTkEntry(canvas,height=30,width=200,border_width=1)
        name_head.insert(0,'REMARKS')
        name_head.grid(row=0,padx=2,column=37,pady=10)
        name_head.configure(state='readonly')













        

        
        c = con.connect(host='localhost',user='root',password='Yash_Arsu_00510',database='project_ams')
        mycursor = c.cursor()
        sql='select * from project_ams.all_students'
        mycursor = c.cursor()
        mycursor.execute(sql)
        data=mycursor.fetchall()


        
        row=2
        for i in data:

            col=0

            for j in i:
                if(col==1 or col=='1' or col == '37' or col==37):
                    item_label=CTkEntry(canvas,height=30,width=200,border_width=0)
                else:
                    item_label=CTkEntry(canvas,height=30,width=100,border_width=0)
                item_label.insert(0,j)
                item_label.grid(row=row,column=col,pady=1,padx=2)
                item_label.configure(state='readonly')
                col=col+1
            row=row+1












    def change_year2():
        s_canvas.grid()
        s_canvas=CTkScrollableFrame(show_window,height=height,width=width)
        print(2)






    show_btn=CTkButton(show_window,text='First Year',height=50,width=200,command=change_year1)
    show_btn.place(x=450,y=300)
    s_show_btn=CTkButton(show_window,text='Direct Second Year',height=50,width=200,command=change_year2)
    s_show_btn.place(x=700,y=300)








            # show_id_label=CTkLabel()









def delete_data_window():
    delete_window=CTkToplevel(win)
    delete_window.geometry('750x750')
    delete_window.title("Delete Data")









show_btn=CTkButton(frame1,text="SHOW",command=show_data_window)
show_btn.place(x=20,y=400)

delete_btn=CTkButton(frame1,text="DELETE",command=delete_data_window)
delete_btn.place(x=20,y=450)

eligibiity_btn=CTkButton(frame1,text="Eligibility")
eligibiity_btn.place(x=20,y=500)

merit_btn=CTkButton(frame1,text="Merit")
merit_btn.place(x=20,y=500)


mode_btn=CTkButton(frame1,text="Change Mode",command=change_mode,width=40,height=40)
mode_btn.place(x=20,y=600)




#--------First Year Frame--------
f_year_frame=CTkFrame(app,width=year_frame_width,height=height)
f_year_frame.grid(row=0,column=1,sticky="N",padx=5,pady=5)
f_year_frame.grid_propagate()



# print(year_frame_width)

# label=CTkLabel(f_year_frame,text='.')
# label.grid()
# myscrollbar=CTkScrollbar(f_year_frame,orientation="vertical",height=height)
# myscrollbar.pack(side="right",fill="y")
#--------Frame content--------


register_var=StringVar()

reg_no_label = CTkLabel(f_year_frame, text="Registration Number:")
reg_no_label.place(x=20,y=20)
reg_no_entry = CTkEntry(f_year_frame,textvariable=register_var)
reg_no_entry.place(x=140,y=20)



name_var=StringVar()

name_label = CTkLabel(f_year_frame, text="Name:")
name_label.place(x=340,y=20)
name_entry = CTkEntry(f_year_frame,textvariable=name_var)
name_entry.place(x=410,y=20)


# genderframe=CTkFrame(f_year_frame)
# genderframe.place(x=20,y=)

gender_var = StringVar()

gender = CTkLabel(f_year_frame, text="Gender:")
gender.place(x=20,y=70)


male_radiobtn = CTkRadioButton(f_year_frame, text="Male", variable=gender_var, value="M" )
male_radiobtn.place(x=100,y=70)
female_radiobtn = CTkRadioButton(f_year_frame, text="Female", variable=gender_var, value="F")
female_radiobtn.place(x=180,y=70)
other_radiobtn =CTkRadioButton(f_year_frame, text="Other", variable=gender_var, value="O")
other_radiobtn.place(x=260,y=70)



#--------MO_PY_ENGG--------


#--------Function to validate HSSC fields based on MO PY and ENGG--------
def disab_enab():

    if(((engg_var.get()==True) and (py_var.get()==False and mo_var.get()==False)) or( engg_var.get()==False and py_var.get()==False and mo_var.get()==False)):
        hssc_eng_entry.configure(placeholder_text="")
        hssc_eng_entry.configure(state="disabled")
        # hssc_eng_label.configure(state="disabled")
        hssc_phy_entry.configure(placeholder_text="")
        hssc_phy_entry.configure(state="disabled")
        # hssc_phy_label.configure(state="disabled")
        hssc_che_entry.configure(placeholder_text="")
        hssc_che_entry.configure(state="disabled")
        # hssc_che_label.configure(state="disabled")
        hssc_bio_entry.configure(placeholder_text="")
        hssc_bio_entry.configure(state="disabled")
        # hssc_bio_label.configure(state="disabled")
        hssc_math_entry.configure(placeholder_text="")
        hssc_math_entry.configure(state="disabled")
        
        hssc_a_radiobtn.configure(state="disabled")
        hssc_c_radiobtn.configure(state="disabled")
        hssc_s_radiobtn.configure(state="disabled")
        hssc_v_radiobtn.configure(state="disabled")
        hssc_label.configure(state='disabled')
        hssc_total_label.configure(state='disabled')
        hssc_type_label.configure(state='disabled')
        hssc_a_radiobtn.deselect()
        hssc_c_radiobtn.deselect()
        hssc_s_radiobtn.deselect()
        hssc_v_radiobtn.deselect()
        hssc_a_total_var=''
        hssc_c_total_var=''
        hssc_s_total_var=''
        hssc_v_total_var=''
        hssc_a_total_entry.delete(0,END)
        hssc_c_total_entry.delete(0,END)
        hssc_s_total_entry.delete(0,END)
        hssc_v_total_entry.delete(0,END)
        hssc_eng_entry.delete(0,END)
        hssc_phy_entry.delete(0,END)
        hssc_che_entry.delete(0,END)
        hssc_math_entry.delete(0,END)
        hssc_bio_entry.delete(0,END)
        hssc_total_var=''
        hssc_ad_entry.delete(0,END)
        hssc_ad_entry.configure(state='disabled')

    else:
        hssc_eng_entry.configure(state="normal",placeholder_text="English")
        # hssc_eng_label.configure(state="disabled")
    
        hssc_phy_entry.configure(state="normal",placeholder_text="Physics")
        # hssc_phy_label.configure(state="disabled")
        hssc_che_entry.configure(state="normal",placeholder_text="Chemistry")
        # hssc_che_label.configure(state="disabled")
        hssc_bio_entry.configure(state="normal",placeholder_text="Biology")
        # hssc_bio_label.configure(state="normal")
        hssc_math_entry.configure(state="normal",placeholder_text="Maths")
        hssc_ad_entry.configure(state='normal',placeholder_text="AD Marks")


        hssc_a_radiobtn.configure(state="normal")
        hssc_c_radiobtn.configure(state="normal")
        hssc_s_radiobtn.configure(state="normal")
        hssc_v_radiobtn.configure(state="normal")
        hssc_label.configure(state='normal')
        hssc_total_label.configure(state='normal')
        hssc_type_label.configure(state='normal')








mo_var = BooleanVar()
py_var = BooleanVar()
engg_var = BooleanVar()
program = CTkLabel(f_year_frame, text="Program:")
program.place(x=20,y=130)
mo_btn = CTkCheckBox(f_year_frame, text="MO", variable=mo_var ,command=disab_enab)
mo_btn.place(x=100,y=130)
py_btn = CTkCheckBox(f_year_frame, text="PY", variable=py_var ,command=disab_enab)
py_btn.place(x=180,y=130)
engg_btn = CTkCheckBox(f_year_frame, text="ENGG", variable=engg_var ,command=disab_enab)
engg_btn.place(x=260,y=130)




#--------GEN/CSP--------




gen_csp_var= StringVar()
gen_csp_label = CTkLabel(f_year_frame, text="GEN/CSP:" )
gen_csp_label.place(x=20,y=180)

gen_radiobtn = CTkRadioButton(f_year_frame, text="GEN",variable=gen_csp_var, value="GEN")
gen_radiobtn.place(x=100,y=180)



csp_radiobtn = CTkRadioButton(f_year_frame,text="CSP", variable=gen_csp_var, value="CSP")
csp_radiobtn.place(x=180,y=180)



#--------SC/ST/OBC--------
sc_st_obc_var= StringVar()
sc_st_obc_label = CTkLabel(f_year_frame, text="SC/ST/OBC:")
sc_st_obc_label.place(x=20,y=230)

sc_radiobtn = CTkRadioButton(f_year_frame, text="SC",variable=sc_st_obc_var, value="SC")
sc_radiobtn.place(x=100,y=230)

st_radiobtn = CTkRadioButton(f_year_frame,text="ST", variable=sc_st_obc_var, value="ST")
st_radiobtn.place(x=180,y=230)

obc_radiobtn = CTkRadioButton(f_year_frame,text="OBC", variable=sc_st_obc_var, value="OBC")
obc_radiobtn.place(x=260,y=230)


#--------PwD/ESM--------

pwd_esm_var=StringVar()
pwd_esm_label=CTkLabel(f_year_frame, text="PwD/ESM")
pwd_esm_label.place(x=20,y=280)

pwd_radiobtn = CTkRadioButton(f_year_frame, text="PwD",variable=sc_st_obc_var, value="PwD")
pwd_radiobtn.place(x=100,y=280)

esm_radiobtn = CTkRadioButton(f_year_frame,text="ESM", variable=sc_st_obc_var, value="ESM")
esm_radiobtn.place(x=260,y=280)




#--------GN/NRI/LA/OGA--------

gn_nri_la_oga_var=StringVar()

gn_nri_la_oga_label=CTkLabel(f_year_frame, text="GN/NRI/LA/OGA")
gn_nri_la_oga_label.place(x=20,y=330)

gn_radiobtn = CTkRadioButton(f_year_frame, text="GN",variable=gn_nri_la_oga_var, value="GN")
gn_radiobtn.place(x=100,y=330)

nri_radiobtn = CTkRadioButton(f_year_frame,text="NRI", variable=gn_nri_la_oga_var, value="NRI")
nri_radiobtn.place(x=180,y=330)

la_radiobtn = CTkRadioButton(f_year_frame,text="LA", variable=gn_nri_la_oga_var, value="LA")
la_radiobtn.place(x=260,y=330)


oga_radiobtn = CTkRadioButton(f_year_frame,text="OGA", variable=gn_nri_la_oga_var, value="OGA")
oga_radiobtn.place(x=340,y=330)







ssc_label=CTkLabel(f_year_frame, text="SSC  marks:" ,font=('Helvetica', 24))
ssc_label.place(x=20,y=380)

# ssc_eng_label=CTkLabel(f_year_frame, text=":")
# ssc_eng_label.place(x=80,y=380)
ssc_eng_entry = CTkEntry(f_year_frame,placeholder_text='English',width=100)
ssc_eng_entry.place(x=20,y=430)




# ssc_mat_label=CTkLabel(f_year_frame, text=":")
# ssc_mat_label.place(x=,y=430)
ssc_mat_entry = CTkEntry(f_year_frame,placeholder_text='Maths',width=100)
ssc_mat_entry.place(x=125,y=430)




# ssc_sci_label=CTkLabel(f_year_frame, text=":")
# ssc_sci_label.grid()
ssc_sci_entry = CTkEntry(f_year_frame,placeholder_text='Science',width=100)
ssc_sci_entry.place(x=230,y=430)




# ssc_total_label=CTkLabel(f_year_frame, text=":" )
# ssc_total_label.grid()
ssc_total_entry = CTkEntry(f_year_frame,placeholder_text='Total',width=100)
ssc_total_entry.place(x=335,y=430)


#ssc ad marks added by arsalan.
ssc_ad_entry = CTkEntry(f_year_frame,placeholder_text='AD marks',width=100)
ssc_ad_entry.place(x=440,y=430)





#--------HSSC Marks--------

hssc_label=CTkLabel(f_year_frame, text="HSSC marks:" ,font=('Helvetica', 24),state='disabled')
hssc_label.place(x=20,y=480)

# hssc_eng_label=CTkLabel(f_year_frame, text=":",state="disabled")
# hssc_eng_label.place(x=20,y=530)
hssc_eng_entry = CTkEntry(f_year_frame,state="disabled",placeholder_text='HSSC English marks',width=100)
hssc_eng_entry.place(x=20,y=530)




# hssc_phy_label=CTkLabel(f_year_frame, text=":",state="disabled")
# hssc_phy_label.grid()
hssc_phy_entry = CTkEntry(f_year_frame,state="disabled",placeholder_text='HSSC Physics marks',width=100)
hssc_phy_entry.place(x=125,y=530)




# hssc_che_label=CTkLabel(f_year_frame, text=":",state="disabled")
# hssc_che_label.grid()
hssc_che_entry = CTkEntry(f_year_frame,state="disabled",placeholder_text='HSSC Chemistry marks',width=100)
hssc_che_entry.place(x=230,y=530)


# hssc_math_label=CTkLabel(f_year_frame, text=":" ,state="disabled")
# hssc_math_label.grid()
hssc_math_entry = CTkEntry(f_year_frame,state="disabled",placeholder_text='HSSC Math marks',width=100)
hssc_math_entry.place(x=335,y=530)


# hssc_bio_label=CTkLabel(f_year_frame, text=":" ,state="disabled")
# hssc_bio_label.grid()
hssc_bio_entry = CTkEntry(f_year_frame,state="disabled",placeholder_text='HSSC Biology marks',width=100)
hssc_bio_entry.place(x=440,y=530)



hssc_ad_entry = CTkEntry(f_year_frame,state="disabled",placeholder_text='HSSC AD marks',width=100)
hssc_ad_entry.place(x=545,y=530)




#--------HSSC RadioButtons--------

#--------Function to validate HSSC total marks  based on radio buttons--------
def hssc_total():
    

    if(hssc_total_var.get()=="HSSC A"):

        hssc_a_total_entry.configure(state="normal")
        hssc_a_total_entry.configure(placeholder_text="HSSC A total")
        hssc_c_total_entry.configure(placeholder_text="")
        hssc_s_total_entry.configure(placeholder_text="")
        hssc_v_total_entry.configure(placeholder_text="")
        # hssc_a_total_label.configure(state="normal")
        hssc_c_total_entry.configure(state="disabled")
        # hssc_c_total_label.configure(state="disabled")
        hssc_s_total_entry.configure(state="disabled")
        # hssc_s_total_label.configure(state="disabled")
        hssc_v_total_entry.configure(state="disabled")
        # hssc_v_total_label.configure(state="disabled")

    elif(hssc_total_var.get()=="HSSC C"):

        hssc_c_total_entry.configure(state="normal")
        hssc_a_total_entry.configure(placeholder_text="")
        hssc_c_total_entry.configure(placeholder_text="HSSC C total")
        hssc_v_total_entry.configure(placeholder_text="")
        hssc_s_total_entry.configure(placeholder_text="")
        hssc_a_total_entry.configure(state="disabled")
        # hssc_a_total_label.configure(state="disabled")
        # hssc_c_total_label.configure(state="normal")
        hssc_s_total_entry.configure(state="disabled")
        # hssc_s_total_label.configure(state="disabled")
        hssc_v_total_entry.configure(state="disabled")
        # hssc_v_total_label.configure(state="disabled")

    elif(hssc_total_var.get()=="HSSC S"):

        hssc_s_total_entry.configure(state="normal")
        hssc_a_total_entry.configure(placeholder_text="")
        hssc_c_total_entry.configure(placeholder_text="")
        hssc_s_total_entry.configure(placeholder_text="HSSC C total")
        hssc_v_total_entry.configure(placeholder_text="")
        hssc_a_total_entry.configure(state="disabled")
        # hssc_a_total_label.configure(state="disabled")
        hssc_c_total_entry.configure(state="disabled")
        # hssc_c_total_label.configure(state="disabled")
        # hssc_s_total_label.configure(state="normal")
        hssc_v_total_entry.configure(state="disabled")
        # hssc_v_total_label.configure(state="disabled")

    else:

        hssc_v_total_entry.configure(state="normal")
        hssc_a_total_entry.configure(placeholder_text="")
        hssc_c_total_entry.configure(placeholder_text="")
        hssc_s_total_entry.configure(placeholder_text="")
        hssc_v_total_entry.configure(placeholder_text="HSSC V total")
        hssc_a_total_entry.configure(state="disabled")
        # hssc_a_total_label.configure(state="disabled")
        hssc_c_total_entry.configure(state="disabled")
        # hssc_c_total_label.configure(state="disabled")
        hssc_s_total_entry.configure(state="disabled")
        # hssc_s_total_label.configure(state="disabled")
        # hssc_v_total_label.configure(state="normal")







hssc_total_var=StringVar()


hssc_type_label=CTkLabel(f_year_frame, text="HSSC :",state='disabled')
hssc_type_label.place(x=500,y=130)

hssc_a_radiobtn = CTkRadioButton(f_year_frame, text="HSSC A",variable=hssc_total_var,value="HSSC A",command=hssc_total,state="disabled",width=100)
hssc_a_radiobtn.place(x=580,y=130)

hssc_c_radiobtn = CTkRadioButton(f_year_frame,text="HSSC C", variable=hssc_total_var,value="HSSC C",command=hssc_total,state="disabled",width=100)
hssc_c_radiobtn.place(x=660,y=130)

hssc_s_radiobtn = CTkRadioButton(f_year_frame,text="HSSC S", variable=hssc_total_var,value="HSSC S",command=hssc_total,state="disabled",width=100)
hssc_s_radiobtn.place(x=740,y=130)


hssc_v_radiobtn = CTkRadioButton(f_year_frame,text="HSSC V", variable=hssc_total_var,value="HSSC V",command=hssc_total,state="disabled",width=100)
hssc_v_radiobtn.place(x=820,y=130)

#------HSSC Total Entry--------





hssc_a_total_var=StringVar()
hssc_c_total_var=StringVar()
hssc_s_total_var=StringVar()
hssc_v_total_var=StringVar()


hssc_total_label=CTkLabel(f_year_frame, text="HSSC Total marks:" ,state='disabled')
hssc_total_label.place(x=500,y=180)

# hssc_a_total_label=CTkLabel(f_year_frame, text="",state="disabled")
# hssc_a_total_label.place(x=,y=)
hssc_a_total_entry = CTkEntry(f_year_frame,textvariable=hssc_a_total_var,state="disabled",placeholder_text='Total',width=100)
hssc_a_total_entry.place(x=500,y=230)

 


# hssc_c_total_label=CTkLabel(f_year_frame, text="",state="disabled")
# hssc_c_total_label.grid()
hssc_c_total_entry = CTkEntry(f_year_frame,textvariable=hssc_c_total_var,state="disabled",placeholder_text='HSSC C total',width=100)
hssc_c_total_entry.place(x=605,y=230)




# hssc_s_total_label=CTkLabel(f_year_frame, text="",state="disabled")
# hssc_s_total_label.grid()
hssc_s_total_entry = CTkEntry(f_year_frame,textvariable=hssc_s_total_var,state="disabled",placeholder_text='HSSC S total',width=100)
hssc_s_total_entry.place(x=710,y=230)




# hssc_v_total_label=CTkLabel(f_year_frame, text="",state="disabled")
# hssc_v_total_label.grid()
hssc_v_total_entry = CTkEntry(f_year_frame,textvariable=hssc_v_total_var,state="disabled",placeholder_text='HSSC V total',width=100)
hssc_v_total_entry.place(x=815,y=230)

#--------Remarks Text Box--------
fy_remarks_var=StringVar()


fy_remarks_label=CTkLabel(f_year_frame, text="Remarks:")
fy_remarks_label.place(x=500,y=280)
fy_remarks_entry = CTkEntry(f_year_frame,textvariable=fy_remarks_var)
fy_remarks_entry.place(x=500,y=330)



submit_button = CTkButton(f_year_frame,text ='submit',command=submit_data_FY)
submit_button.place(x=500,y=640)

clear_button = CTkButton(f_year_frame,text ='clear',command=clear)
clear_button.place(x=300,y=640)


#--------First Year Frame Ends------

#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------




#--------Second Year Frame--------

s_year_frame=CTkFrame(app,width=year_frame_width,height=height-80)
s_year_frame.grid_propagate()







s_register_var=StringVar()

s_reg_no_label = CTkLabel(s_year_frame, text="Registration Number")
s_reg_no_label.place(x=20,y=20)
s_reg_no_entry = CTkEntry(s_year_frame,textvariable=s_register_var)
s_reg_no_entry.place(x=140,y=20)



s_name_var=StringVar()

s_name_label = CTkLabel(s_year_frame, text="Name")
s_name_label.place(x=340,y=20)
s_name_entry =CTkEntry(s_year_frame,textvariable=s_name_var)
s_name_entry.place(x=410,y=20)

#--------Gender Radio Buttons--------

s_gender_var = StringVar()
s_gender = CTkLabel(s_year_frame, text="Gender")
s_gender.place(x=20,y=70)



s_male_radiobtn = CTkRadioButton(s_year_frame, text="Male", variable=s_gender_var, value="M")
s_male_radiobtn.place(x=100,y=70)
s_female_radiobtn = CTkRadioButton(s_year_frame, text="Female", variable=s_gender_var, value="F")
s_female_radiobtn.place(x=180,y=70)
s_other_radiobtn =CTkRadioButton(s_year_frame, text="Other", variable=s_gender_var, value="O")
s_other_radiobtn.place(x=260,y=70)

#--------Courses radiobuttons--------

s_course_label=CTkLabel(s_year_frame,text="Course:")
s_course_label.place(x=20,y=130)


s_hssc_var=StringVar()
s_voc_var=StringVar()
s_iti_var=StringVar()


s_course_var = StringVar()

def radio_sel():
    if s_course_var.get()=="1":
        s_hssc_var.set(1)
        s_hssc_ad_total_label.configure(state='normal')
        s_hssc_ad_entry.configure(state='normal')
        s_voc_drop_label.configure(state="disabled")
        s_voc_drop.configure(state="disabled")
        s_iti_drop_label.configure(state="disabled")
        s_iti_drop.configure(state="disabled")


        s_hssc_mat_total_label.configure(state="normal")
        s_hssc_mat_total_entry.configure(state="normal",placeholder_text='HSSC Maths(100)')
        s_hssc_s_total_label.configure(state="normal")
        s_hssc_s_entry.configure(state="normal",placeholder_text='HSSC S (600)')

        s_hssc_v_total_label.configure(state="disabled")
        s_hssc_v_entry.configure(state="disabled")


        s_iti_total_label.configure(state="disabled")
        s_iti_total_entry.configure(state="disabled")

        s_hssc_ad.configure(state="normal")
        s_iti_total=''
        s_hssc_v=''
        
        s_hssc_ad_total_label.configure(state="normal")
        s_hssc_ad_entry.configure(state="normal")
        
        s_hssc_ad_entry.configure(placeholder_text="HSSC AD")



    elif s_course_var.get()=="2":
        s_voc_drop_label.configure(state="normal")
        s_voc_drop.configure(state="normal")
        s_iti_drop_label.configure(state="disabled")
        s_iti_drop.configure(state="disabled")


        s_hssc_mat_total_label.configure(state="disabled")
        s_hssc_mat_total_entry.configure(state="disabled",placeholder_text='HSSC Maths(100)')
        s_hssc_s_total_label.configure(state="disabled")
        s_hssc_s_entry.configure(state="disabled",placeholder_text='HSSC S (600)')


        s_hssc_v_total_label.configure(state="normal")
        s_hssc_v_entry.configure(state="normal")


        s_iti_total_label.configure(state="disabled")
        s_iti_total_entry.configure(state="disabled")
        
        s_hssc_ad_entry.configure(state="disabled")
        s_hssc_ad_total_label.configure(state="disabled")

        s_hssc_ad=''
        s_hssc_s=''
        s_hssc_mat_var=''
        s_iti_total=''
        
    else:
        s_hssc_ad=''
        s_hssc_v=''
        s_hssc_s=''
        s_hssc_mat_var=''
        s_iti_drop_label.configure(state="normal")
        s_iti_drop.configure(state="normal")
        s_voc_drop_label.configure(state="disabled")
        s_voc_drop.configure(state="disabled")

        s_hssc_mat_total_label.configure(state="disabled")
        s_hssc_mat_total_entry.configure(state="disabled",placeholder_text='HSSC Maths(100)')
        s_hssc_s_total_label.configure(state="disabled")
        s_hssc_s_entry.configure(state="disabled",placeholder_text='HSSC S (600)')

        s_hssc_v_total_label.configure(state="disabled")
        s_hssc_v_entry.configure(state="disabled")

        s_iti_total_label.configure(state="normal")
        s_iti_total_entry.configure(state="normal")
        
        s_hssc_ad_entry.configure(state="disabled")
        s_hssc_ad_total_label.configure(state="disabled")


s_hssc_radiobtn = CTkRadioButton(s_year_frame, text="HSSC(SCI)", variable=s_course_var, value="1" , command=radio_sel)
s_hssc_radiobtn.place(x=100,y=130)
s_voc_radiobtn = CTkRadioButton(s_year_frame, text="VOC", variable=s_course_var, value="2",command=radio_sel)
s_voc_radiobtn.place(x=180,y=130)
s_iti_radiobtn =CTkRadioButton(s_year_frame, text="ITI", variable=s_course_var, value="3",command=radio_sel)
s_iti_radiobtn.place(x=260,y=130)



s_voc_drop_label=CTkLabel(s_year_frame,text="VOC",state="disabled")
s_voc_drop_label.place(x=20,y=180)
s_voc_drop= CTkOptionMenu(s_year_frame,variable=s_voc_var, values=["A", "B", "D"],state="disabled")
s_voc_drop.place(x=100,y=180)




s_iti_drop_label=CTkLabel(s_year_frame,text="ITI",state="disabled")
s_iti_drop_label.place(x=20,y=230)
s_iti_drop= CTkOptionMenu(s_year_frame,variable=s_iti_var, values=["A", "B", "C"],state="disabled")
s_iti_drop.place(x=100,y=230)






s_hssc_mat_var=StringVar()




s_hssc_mat_total_label=CTkLabel(s_year_frame, text="HSSC Maths:" ,state='disabled')
s_hssc_mat_total_label.place(x=500,y=180)
s_hssc_mat_total_entry = CTkEntry(s_year_frame,textvariable=s_hssc_mat_var,state="disabled",placeholder_text='HSSC Maths',width=100)
s_hssc_mat_total_entry.place(x=500,y=230)



s_hssc_s=StringVar()

s_hssc_s_total_label=CTkLabel(s_year_frame, text="HSSC S:" ,state='disabled')
s_hssc_s_total_label.place(x=605,y=180)
s_hssc_s_entry = CTkEntry(s_year_frame,textvariable=s_hssc_s,state="disabled",placeholder_text='HSSC S ',width=100)
s_hssc_s_entry.place(x=605,y=230)




s_hssc_v=StringVar()

s_hssc_v_total_label=CTkLabel(s_year_frame, text="HSSC V:" ,state='disabled')
s_hssc_v_total_label.place(x=710,y=180)
s_hssc_v_entry = CTkEntry(s_year_frame,textvariable=s_hssc_v,state="disabled",placeholder_text='HSSC V',width=100)
s_hssc_v_entry.place(x=710,y=230)


s_hssc_ad=StringVar()

s_hssc_ad_total_label=CTkLabel(s_year_frame, text="HSSC AD:",state="disabled")
s_hssc_ad_total_label.place(x=815,y=180)
s_hssc_ad_entry = CTkEntry(s_year_frame,textvariable=s_hssc_ad,state="disabled",placeholder_text='HSSC AD',width=100)
s_hssc_ad_entry.place(x=815,y=230)

s_iti_total=StringVar()

s_iti_total_label=CTkLabel(s_year_frame, text="ITI Tot:" ,state='disabled')
s_iti_total_label.place(x=920,y=180)
s_iti_total_entry = CTkEntry(s_year_frame,textvariable=s_iti_total,state="disabled",placeholder_text='ITI',width=100)
s_iti_total_entry.place(x=920,y=230)




#--------SSC Marks--------



s_ssc_label=CTkLabel(s_year_frame, text="SSC marks:" ,font=('Helvetica', 24))
s_ssc_label.place(x=20,y=380)


s_ssc_eng_entry = CTkEntry(s_year_frame,placeholder_text='English',width=100)
s_ssc_eng_entry.place(x=20,y=430)





s_ssc_mat_entry = CTkEntry(s_year_frame,placeholder_text='Maths',width=100)
s_ssc_mat_entry.place(x=125,y=430)





s_ssc_sci_entry = CTkEntry(s_year_frame,placeholder_text='Science',width=100)
s_ssc_sci_entry.place(x=230,y=430)





s_ssc_total_entry = CTkEntry(s_year_frame,placeholder_text='Total',width=100)
s_ssc_total_entry.place(x=335,y=430)


s_ssc_ad_entry = CTkEntry(s_year_frame,placeholder_text='SSC AD',width=100)
s_ssc_ad_entry.place(x=440,y=430)

#--------Remarks--------


sy_remarks_var=StringVar()

sy_remarks_label=CTkLabel(s_year_frame, text="Remarks")
sy_remarks_label.place(x=600,y=280)
sy_remarks_entry = CTkEntry(s_year_frame,textvariable=sy_remarks_var,width=300,height=100)
sy_remarks_entry.place(x=600,y=330)


s_submit_button = CTkButton(s_year_frame,text ='submit')
s_submit_button.place(x=500,y=640)

s_clear_button = CTkButton(s_year_frame,text ='clear',command=s_clear)
s_clear_button.place(x=300,y=640)







#--------Second Year Frame Ends--------




app.mainloop()
 