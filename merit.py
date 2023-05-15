import pandas as pd
import mysql.connector as con
import os


path = "F:/StudentData"
# os.makedirs(path)
# connect to MySQL database
c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')

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


# # read data into pandas dataframe
# df = pd.read_sql("SELECT * FROM all_student", con)

# loop through each course
for course in ['MO', 'PY', 'ENGG']:
    
    # add course heading
    # with open(output_path, 'a') as f:
    #     f.write(f"Course: {course}\n\n")
    
    # loop through each category
    for category in ['GEN', 'CSP', 'SC', 'ST', 'OBC']:
        output_path = os.path.join(path, f"{course}_{category}_merit_list.csv")
        
        if(course == 'MO' or course == 'PY'):
            # filter dataframe to include only eligible students from current category and course
            filtered_df = df[(df[category]) & (df[course+'_ELG'] == 1)]

            # sort dataframe based on merit list criteria
            sorted_df = filtered_df.sort_values(by=['HSSC_TOTAL_600', 'HSSC_ENG_100', 'SSC_TOTAL_600', 'SSC_ENG_100'], ascending=False)

            # add category heading
            heading = f"Course: {course}\n Category: {category}\n\n".center(50)
            with open(output_path, 'a') as f:
                f.write(heading)
            
            # write sorted data to CSV file
            sorted_df.to_csv(output_path, mode='a', index=False)

            # add blank rows to separate data for different categories
            with open(output_path, 'a') as f:
                f.write('\n\n')
            
            # filter dataframe to include only not-eligible students from current category and course
            not_eligible_df = df[(df[category] == 0) & (df[course+'EL'] == 0)]

            # add not eligible heading
            with open(output_path, 'a') as f:
                f.write("Not Eligible Cases\n\n")

            # write not-eligible data to CSV file
            not_eligible_df.to_csv(output_path, mode='a', index=False)

            # add blank rows to separate not-eligible data from next category
            with open(output_path, 'a') as f:
                f.write('\n\n')
        else:
            # filter dataframe to include only eligible students from current category and course
            filtered_df = df[(df[category] == 1) & (df[course+'_ELG'] == 1)]

            # sort dataframe based on merit list criteria
            sorted_df = filtered_df.sort_values(by=['SSC_TOTAL_600', 'SSC_MAT_100', 'SSC_SCI_100','SSC_ENG_100'], ascending=False)

            # add category heading
            heading = f"Course: {course}\n Category: {category}\n\n".center(50)
            with open(output_path, 'a') as f:
                f.write(heading)
            
            # write sorted data to CSV file
            sorted_df.to_csv(output_path, mode='a', index=False)

            # add blank rows to separate data for different categories
            with open(output_path, 'a') as f:
                f.write('\n\n')
            
            # filter dataframe to include only not-eligible students from current category and course
            not_eligible_df = df[(df[category] == 0) & (df[course+'EL'] == 0)]

            # add not eligible heading
            with open(output_path, 'a') as f:
                f.write("Not Eligible\n\n")

            # write not-eligible data to CSV file
            not_eligible_df.to_csv(output_path, mode='a', index=False)

            # add blank rows to separate not-eligible data from next category
            with open(output_path, 'a') as f:
                f.write('\n\n')
        
# close MySQL connection
con.close()