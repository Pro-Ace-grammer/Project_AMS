import mysql.connector as con
def submit_form_FY(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks):
    
    
    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
    mycursor = c.cursor()
    query="insert into all_student(REG_NO, NAME, Gender, MO, PY, ENGG, GEN_CSP, SC_ST_OBC, PwD_ESM, GN_NRI_LA_OGA, SSC_ENG_100, SSC_SCI_100, SSC_MAT_100, SSC_TOTAL_600, SSC_AD_MKS, SSC_Q_TOTAL, HSSC_ENG_100, HSSC_PHY_100, HSSC_CHE_100, HSSC_MAT_100, HSSC_BIO_100, PCM, PCB, PCM_B, MAT_BIO, HSSC_A_600, HSSC_C_600, HSSC_S_600, HSSC_V_800, HSSC_ALL, HSSC_AD_MKS, HSSC_Q_TOT_600, SSC_PER, HSSC_PER, ENGG_EL, MO_EL, PY_EL, REMARKS_COMPLIANCE) values({},'{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}')".format(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,MO,PY,fy_remarks)

    mycursor = c.cursor()
    mycursor.execute(query)
    c.commit()
    # do something with the input values here, like storing in a database
    
    print("successfully inserted the data")




#-----------database for direct 2nd year---------

def submit_form_SY(reg_no, name, gender, hssc_if, voc_if, iti_if, ssc_eng, ssc_mat, ssc_sci, ssc_tot, ssc_ad, ssc_m_tot, hssc_mat, hssc_s, hssc_v, hssc_q_tot_all, iti, iti_q_tot_all, hssc_ad, hssc_q_tot, voc_q_tot, iti_q_tot, ssc_per, hssc_per, iti_per, hssc_sci_el, voc_el, iti_el, sy_remarks_entry):


    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
    mycursor = c.cursor()
    query="insert into direct_sy(REG_NO, NAME, GENDER, HSSC_SCI, VOC_ABD, ITI_ABC, SSC_ENG, SSC_MAT, SSC_SCI, SSC_Q_TOT, SSC_AD_MARKS, SSC_M_TOT, HSSC_MAT, HSSC_S, HSSC_V, HSSC_Q_TOT_ALL, ITI, ITI_TOT, HSSC_AD_MKS, HSSC_Q_TOT, VOC_Q_TOT, ITI_Q_TOT, SSC_Q_PER, HSSC_Q_PER, ITI_Q_PER, HSSC__SCI_EL, VOC_ABD_EL, ITI_ABC_EL, REMARK) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}')".format(reg_no, name, gender, hssc_if, voc_if, iti_if, ssc_eng, ssc_mat, ssc_sci, ssc_tot, ssc_ad, ssc_m_tot, hssc_mat, hssc_s, hssc_v, hssc_q_tot_all, iti, iti_q_tot_all, hssc_ad, hssc_q_tot, voc_q_tot, iti_q_tot, ssc_per, hssc_per, iti_per, hssc_sci_el, voc_el, iti_el, sy_remarks_entry)

    mycursor = c.cursor()
    mycursor.execute(query)
    c.commit()
    print("successfully inserted the data")





