import mysql.connector as con
def submit_form_FY(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks):
    

    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
    mycursor = c.cursor()
    query="insert into all_student(REG_NO, NAME, Gender, MO, PY, ENGG, GEN_CSP, SC_ST_OBC, PwD_ESM, GN_NRI_LA_OGA, SSC_ENG_100, SSC_SCI_100, SSC_MAT_100, SSC_TOTAL_600, SSC_AD_MKS, SSC_Q_TOTAL, HSSC_ENG_100, HSSC_PHY_100, HSSC_CHE_100, HSSC_MAT_100, HSSC_BIO_100, PCM, PCB, PCM_B, MAT_BIO, HSSC_A_600, HSSC_C_600, HSSC_S_600, HSSC_V_800, HSSC_ALL, HSSC_AD_MKS, HSSC_Q_TOT_600, SSC_Percent, HSSC_Percent, ENGG_ELG, MO_ELG, PY_ELG, REMARKS_COMPLIANCE) values({},'{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks)

    mycursor = c.cursor()
    mycursor.execute(query)
    c.commit()
    # do something with the input values here, like storing in a database
    
    print("successfully inserted the data")
    print(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks)





# def submit_data_FY():

#     reg_no = int(reg_no_entry.get())
#     str1 = name_entry.get()
#     name = str1.upper()
#     gender = gender_var.get()


#     mo = mo_var.get()
#     py = py_var.get()
#     engg = engg_var.get()


#     gen_csp = gen_csp_var.get()
#     sc_st_obc = sc_st_obc_var.get()
#     pwd_esm = pwd_esm_var.get()
#     gn_nri_la_oga = gn_nri_la_oga_var.get()


#     ssc_eng = int(ssc_eng_entry.get())
#     ssc_sci = int(ssc_sci_entry.get())
#     ssc_mat = int(ssc_mat_entry.get())
#     ssc_total= int(ssc_total_entry.get())

#     if (ssc_ad_entry.get()=="" or ssc_ad_entry.get()==" "):
#         ssc_AD=0
#         ssc_q_total = ssc_total
#     else:
#         ssc_AD = int(ssc_ad_entry.get())
#         ssc_q_total = ssc_total+ssc_AD 

#     if(mo_var.get() ==True or py_var.get() == True):
#         hssc_eng = hssc_eng_entry.get()
#         hssc_phy  = hssc_phy_entry.get()
#         hssc_che = hssc_che_entry.get()
#         hssc_math = hssc_math_entry.get()
#         hssc_bio = hssc_bio_entry.get()
#     else:
#         hssc_eng = 0
#         hssc_phy = 0
#         hssc_che = 0
#         hssc_math = 0
#         hssc_bio = 0



#     if(mo_var.get() ==True or py_var.get() == True):
#         pcm = hssc_phy + hssc_che + hssc_math
#         pcb = hssc_phy + hssc_che + hssc_bio
#         if(pcm>=pcb):
#             pcm_b = pcm
#         elif(pcm<=pcb):
#             pcm_b = pcb
#         else:
#             pcm_b = 0
#         if(hssc_math>=hssc_bio):
#             mat_bio = hssc_math
#         elif(hssc_math>=hssc_bio):
#             mat_bio = hssc_bio
#         else:
#             mat_bio = 0
#     else:
#         pcm = 0
#         pcb = 0
#         pcm_b = 0
#         mat_bio = 0
        

    
    

#     if(mo_var.get() ==True or py_var.get() == True):

#         hssc_a_total = hssc_a_total_var.get()
#         hssc_c_total = hssc_c_total_var.get()
#         hssc_s_total = hssc_s_total_var.get()
#         hssc_v_total = hssc_v_total_var.get()

#         if(hssc_total_var.get() == "HSSC V"):
#             hssc_all = (hssc_v_total * 600)//800
#         elif(hssc_total_var.get() == "HSSC A"):
#             hssc_all = hssc_a_total
#         elif(hssc_total_var.get() == "HSSC C"):
#             hssc_all = hssc_c_total
#         else:
#             hssc_all = hssc_s_total
#         hssc_ad = hssc_ad_entry.get()
#         hssc_q_tot = hssc_all + hssc_ad
#         hssc_per = (hssc_all/600)*100
#     else:

#         hssc_per = 0
#         hssc_all = 0
#         hssc_a_total = 0
#         hssc_c_total = 0
#         hssc_s_total = 0
#         hssc_v_total = 0
#         hssc_ad = 0
#         hssc_q_tot = 0



#     el="EL"
#     ne="NE"
#     na="NA"

#     ssc_per = (ssc_total/600)*100
#     # hssc_per = (hssc_all/600)*100

#     if(engg_var.get()==True):
#         if(ssc_per>=35):
#             ENGG = el
#         else:
#             ENGG = ne
#     else:
#         ENGG = na


#     if(py_var.get()==True):
#         if(hssc_per>=35):
#             PY = el
#         else:
#             PY = ne
#     else:
#         PY = na


#     if(mo_var.get()==True):
#         if(hssc_per>=35):
#             MO = el
#         else:
#             MO = ne
#     else:
#         MO = na

            
#     fy_remarks = fy_remarks_entry.get()
    
#     db.submit_form(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks)
#     #there are some fields I need to put here 
    

 