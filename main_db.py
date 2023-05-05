import mysql.connector as con
def submit_form(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks):
    
    
    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
    mycursor = c.cursor()
    query="insert into all_student(REG_NO, NAME, Gender, MO, PY, ENGG, GEN_CSP, SC_ST_OBC, PwD_ESM, GN_NRI_LA_OGA, SSC_ENG_100, SSC_SCI_100, SSC_MAT_100, SSC_TOTAL_600, SSC_AD_MKS, SSC_Q_TOTAL, HSSC_ENG_100, HSSC_PHY_100, HSSC_CHE_100, HSSC_MAT_100, HSSC_BIO_100, PCM, PCB, PCM_B, MAT_BIO, HSSC_A_600, HSSC_C_600, HSSC_S_600, HSSC_V_800, HSSC_ALL, HSSC_AD_MKS, HSSC_Q_TOT_600, SSC_Percent, HSSC_Percent, ENGG_ELG, MO_ELG, PY_ELG, REMARKS_COMPLIANCE) values({},'{}','{}',{},{},{},'{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}','{}','{}')".format(reg_no,name,gender,mo,py,engg,gen_csp,sc_st_obc,pwd_esm,gn_nri_la_oga,ssc_eng,ssc_mat,ssc_sci,ssc_total,ssc_AD,ssc_q_total,hssc_eng,hssc_phy,hssc_che,hssc_math,hssc_bio,pcm,pcb,pcm_b,mat_bio,hssc_a_total,hssc_c_total,hssc_s_total,hssc_v_total,hssc_all,hssc_ad,hssc_q_tot,ssc_per,hssc_per,ENGG,PY,MO,fy_remarks)

    mycursor = c.cursor()
    mycursor.execute(query)
    c.commit()
    # do something with the input values here, like storing in a database
    
    print("successfully inserted the data")