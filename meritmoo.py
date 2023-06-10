import pandas as pd
import mysql.connector as con

def gen_mer():
    # connect to MySQL database
    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')

    mycursor = c.cursor()
    query = "select REG_NO, NAME, Gender, MO, PY, ENGG, GEN_CSP, SC_ST_OBC, PwD_ESM, GN_NRI_LA_OGA, SSC_ENG_100, SSC_SCI_100, SSC_MAT_100, SSC_TOTAL_600, SSC_AD_MKS, SSC_Q_TOTAL, HSSC_ENG_100, HSSC_PHY_100, HSSC_CHE_100, HSSC_MAT_100, HSSC_BIO_100, PCM, PCB, PCM_B, MAT_BIO, HSSC_A_600, HSSC_C_600, HSSC_S_600, HSSC_V_800, HSSC_ALL, HSSC_AD_MKS, HSSC_Q_TOT_600, SSC_PER, HSSC_PER, ENGG_EL, MO_EL, PY_EL, REMARKS_COMPLIANCE from all_student"
    mycursor.execute(query)
    data = mycursor.fetchall()
    rg, nm, gnd, mo, py, engg, gc, sc, pwd, gnri, seng, ssci, smat, stot, sad, sqtot, hseng, hsphy, hsche, hsmat, hsbio, pcm, pcb, pcmb, matbio, hssa, hssc, hsss, hssv, hssall, hssad, hssqtot, sper, hsper, engel, moel, pyel, remark = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ,[], [], [], [], [], [], [], [], [], [], [] ,[], [], [], [], [], []

    for REG_NO, NAME, Gender, MO, PY, ENGG, GEN_CSP, SC_ST_OBC, PwD_ESM, GN_NRI_LA_OGA, SSC_ENG_100, SSC_SCI_100, SSC_MAT_100, SSC_TOTAL_600, SSC_AD_MKS, SSC_Q_TOTAL, HSSC_ENG_100, HSSC_PHY_100, HSSC_CHE_100, HSSC_MAT_100, HSSC_BIO_100, PCM, PCB, PCM_B, MAT_BIO, HSSC_A_600, HSSC_C_600, HSSC_S_600, HSSC_V_800, HSSC_ALL, HSSC_AD_MKS, HSSC_Q_TOT_600, SSC_PER, HSSC_PER, ENGG_EL, MO_EL, PY_EL, REMARKS_COMPLIANCE in data:
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
        engel.append(ENGG_EL)
        moel.append(MO_EL) 
        pyel.append(PY_EL) 
        remark.append(REMARKS_COMPLIANCE)
        

    dic = {'REG.NO.(F)':rg, 'NAME':nm, 'GENDER':gnd, 'MO':mo, 'PY':py, 'ENGG':engg, 'GEN/CSP':gc, 'SC/ST/OBC':sc, 'PWD/FF/ESM':pwd, 'GN/NRI/LA/OGA':gnri, 'SSC-ENG-(100)':seng, 'SSC-MAT-100':smat, 'SSC-SCI-100':ssci, 'SSC-TOTAL-600':stot, 'SSC-AD.MKS.':sad, 'SSC-Q-TOTAL':sqtot, 'HSSC-ENG-(100)':hseng, 'HSSC-PHY-(100)':hsphy, 'HSSC-CHE-(100)':hsche, 'HSSC-MAT-(100)':hsmat, 'HSSC-BIO-(100)':hsbio, 'PCM':pcm, 'PCB':pcb, 'PCM/B':pcmb, 'MAT/BIO':matbio, 'HSSC-A(600)':hssa, 'HSSC-C(600)':hssc, 'HSSC-S(600)':hsss, 'HSSC-V(600)':hssv, '600-HSSC-ALL':hssall, 'HSSC-AD.MKS.':hssad, 'HSSC-Q.TOT-600+':hssqtot, 'SSC-%':sper, 'HSSC-%':hsper, 'ENGG_':engel, 'PY_':pyel, 'MO_':moel, 'REMARKS/COMLIANCE (DOCUMENTS TO BE SUBMITTED)':remark,}
    df = pd.DataFrame(dic)

    for course in ['MO']:
        # loop through each category
        for category in ['GEN/CSP']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'GEN') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'GEN') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: GENERAL\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')

                
        for category in ['GEN/CSP']:
            # filter dataframe to include only eligible students from current category and course
           
            elig_df = df[(df[category] == 'CSP') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))
            
            nelig_df = df[(df[category] == 'CSP') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)
            # write sorted data to CSV file
            with open(f"merit_list.csv", 'a') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: GENERAL\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')
            
    print('GENERATED THE MERIT LIST')