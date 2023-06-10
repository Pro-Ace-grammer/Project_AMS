import pandas as pd
import mysql.connector as con
import os

# connect to MySQL database
c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')

#path = "F:/StudentData"
#output_path = os.path.join(path,"_merit_list.csv")

mycursor = c.cursor()
query = "select REG_NO, NAME, Gender, MO, PY, ENGG, GEN_CSP, SC_ST_OBC, PwD_ESM, GN_NRI_LA_OGA, SSC_ENG_100, SSC_SCI_100, SSC_MAT_100, SSC_TOTAL_600, SSC_AD_MKS, SSC_Q_TOTAL, HSSC_ENG_100, HSSC_PHY_100, HSSC_CHE_100, HSSC_MAT_100, HSSC_BIO_100, PCM, PCB, PCM_B, MAT_BIO, HSSC_A_600, HSSC_C_600, HSSC_S_600, HSSC_V_800, HSSC_ALL, HSSC_AD_MKS, HSSC_Q_TOT_600, SSC_PER, HSSC_PER, ENGG_ELG, MO_ELG, PY_ELG, REMARKS_COMPLIANCE from all_student"
mycursor.execute(query)
data = mycursor.fetchall()
rg, nm, gnd, mo, py, engg, gc, sc, pwd, gnri, seng, ssci, smat, stot, sad, sqtot, hseng, hsphy, hsche, hsmat, hsbio, pcm, pcb, pcmb, matbio, hssa, hssc, hsss, hssv, hssall, hssad, hssqtot, sper, hsper, engel, moel, pyel, remark = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ,[], [], [], [], [], [], [], [], [], [], [] ,[], [], [], [], [], []

for REG_NO, NAME, Gender, MO, PY, ENGG, GEN_CSP, SC_ST_OBC, PwD_ESM, GN_NRI_LA_OGA, SSC_ENG_100, SSC_SCI_100, SSC_MAT_100, SSC_TOTAL_600, SSC_AD_MKS, SSC_Q_TOTAL, HSSC_ENG_100, HSSC_PHY_100, HSSC_CHE_100, HSSC_MAT_100, HSSC_BIO_100, PCM, PCB, PCM_B, MAT_BIO, HSSC_A_600, HSSC_C_600, HSSC_S_600, HSSC_V_800, HSSC_ALL, HSSC_AD_MKS, HSSC_Q_TOT_600, SSC_PER, HSSC_PER, ENGG_ELG, MO_ELG, PY_ELG, REMARKS_COMPLIANCE in data:
    rg.append(REG_NO) 
    nm.append(NAME)
    gnd.append(Gender) 
    mo.append(MO) 
    py.append(PY) 
    engg.append(ENGG) 
    gc.append(GEN_CSP) 
    sc.append(SC_ST_OBC) 
    pwd.append(PwD_ESM)
    gnri.append(GN_NRI_LA_OGA)
    seng.append(SSC_ENG_100) 
    ssci.append(SSC_SCI_100)
    smat.append(SSC_MAT_100) 
    stot.append(SSC_TOTAL_600)
    sad.append(SSC_AD_MKS)
    sqtot.append(SSC_Q_TOTAL) 
    hseng.append(HSSC_ENG_100)
    hsphy.append(HSSC_PHY_100)
    hsche.append(HSSC_CHE_100)
    hsmat.append(HSSC_MAT_100) 
    hsbio.append(HSSC_BIO_100)
    pcm.append(PCB) 
    pcb.append(PCB)
    pcmb.append(PCM_B)
    matbio.append(MAT_BIO)
    hssa.append(HSSC_A_600) 
    hssc.append(HSSC_C_600)
    hsss.append(HSSC_S_600) 
    hssv.append(HSSC_V_800) 
    hssall.append(HSSC_ALL)
    hssad.append(HSSC_AD_MKS)
    hssqtot.append(HSSC_Q_TOT_600)
    sper.append(SSC_PER) 
    hsper.append(HSSC_PER) 
    engel.append(ENGG_ELG)
    moel.append(MO_ELG) 
    pyel.append(PY_ELG) 
    remark.append(REMARKS_COMPLIANCE)
    

dic = {'REG.NO.(F)':rg, 'NAME':nm, 'GENDER':gnd, 'MO':mo, 'PY':py, 'ENGG':engg, 'GEN/CSP':gc, 'SC/ST/OBC':sc, 'PWD/FF/ESM':pwd, 'GN/NRI/LA/OGA':gnri, 'SSC-ENG-(100)':seng, 'SSC-MAT-100':smat, 'SSC-SCI-100':ssci, 'SSC-TOTAL-600':stot, 'SSC-AD.MKS.':sad, 'SSC-Q-TOTAL':sqtot, 'HSSC-ENG-(100)':hseng, 'HSSC-PHY-(100)':hsphy, 'HSSC-CHE-(100)':hsche, 'HSSC-MAT-(100)':hsmat, 'HSSC-BIO-(100)':hsbio, 'PCM':pcm, 'PCB':pcb, 'PCM/B':pcmb, 'MAT/BIO':matbio, 'HSSC-A(600)':hssa, 'HSSC-C(600)':hssc, 'HSSC-S(600)':hsss, 'HSSC-V(600)':hssv, '600-HSSC-ALL':hssall, 'HSSC-AD.MKS.':hssad, 'HSSC-Q.TOT-600+':hssqtot, 'SSC-%':sper, 'HSSC-%':hsper, 'ENGG_':engel, 'PY_':pyel, 'MO_':moel, 'REMARKS/COMLIANCE (DOCUMENTS TO BE SUBMITTED)':remark,}

df = pd.DataFrame(dic)

# read data into pandas dataframe
# df = pd.read_sql("SELECT * FROM student_data", con)


for course in dic['MO']:
    # loop through each category
    # ['GEN/CSP', 'SC/ST/OBC', 'PWD/FF/ESM', 'GN/NRI/LA/OGA']
        for category in dic['GEN/CSP']:
            if category == 'GEN':
                if(course == 1):
                    print('yes it is')
                    if(dic['MO_'] == 'EL'):
                        print('in MO check')
                        
                        filtered_df = df[(df['GEN/CSP'] == 'GEN')  & (df['MO']==1) & (df['MO_'] == 'EL')]
                        #heading = f"Course: Modern Office\n Category: {category}\n\n".center(50)
                        #with open(output_path, 'a') as f:
                        #    f.write(heading)
                        # sort dataframe based on merit list criteria
                        sorted_df = filtered_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600', 'HSSC-MAT-(100)'], ascending=False)

                        # write sorted data to CSV file
                        sorted_df.to_csv(output_path, index=False)

                        # add blank rows to separate data for different courses
                        with open(f"F:/StudentData", 'a') as f:
                            f.write('\n')
                        print('did something')  
                    elif(dic['MO_'] == 'NE'):
                        print('elsae me huuu')
                        # filter dataframe to include only not-eligible students from current category and course
                        not_eligible_df = df[(df['GEN/CSP'] == 'GEN') & (df['MO']==1) & (df['MO_'] == 'NE')]

                        # add not eligible heading
                        with open(output_path, 'a') as f:
                            f.write("Not Eligible\n\n")
                        not_eligible_df.to_csv(output_path, mode='a', index=False)
                        # add blank rows to separate not-eligible data from next category
                        with open(output_path, 'a') as f:
                            f.write('\n\n')       
                        print('did something')
                    else:
                        continue   
                else:
                    continue        
print("created successfullyyyyy:")
# close MySQL connection
c.close()

























def submit_form_SY(reg_no, name, gender, hssc_if, voc_if, iti_if, ssc_eng, ssc_mat, ssc_sci, ssc_tot, ssc_ad, ssc_m_tot, hssc_mat, hssc_s, hssc_v, hssc_q_tot_all, iti, iti_q_tot_all, hssc_ad, hssc_q_tot, voc_q_tot, iti_q_tot, ssc_per, hssc_per, iti_per, hssc_sci_el, voc_el, iti_el, sy_remarks_entry):


    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
    mycursor = c.cursor()
    query="insert into direct_sy(REG_NO, NAME, GENDER, HSSC_SCI, VOC_ABD, ITI_ABC, SSC_ENG, SSC_MAT, SSC_SCI, SSC_Q_TOT, SSC_AD_MARKS, SSC_M_TOT, HSSC_MAT, HSSC_S, HSSC_V, HSSC_Q_TOT_ALL, ITI, ITI_TOT, HSSC_AD_MKS, HSSC_Q_TOT, VOC_Q_TOT, ITI_Q_TOT, SSC_Q_PER, HSSC_Q_PER, ITI_Q_PER, HSSC__SCI_EL, VOC_ABD_EL, ITI_ABC_EL, REMARK) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}')".format(reg_no, name, gender, hssc_if, voc_if, iti_if, ssc_eng, ssc_mat, ssc_sci, ssc_tot, ssc_ad, ssc_m_tot, hssc_mat, hssc_s, hssc_v, hssc_q_tot_all, iti, iti_q_tot_all, hssc_ad, hssc_q_tot, voc_q_tot, iti_q_tot, ssc_per, hssc_per, iti_per, hssc_sci_el, voc_el, iti_el, sy_remarks_entry)

    mycursor = c.cursor()
    mycursor.execute(query)
    c.commit()
    print("successfully inserted the data")