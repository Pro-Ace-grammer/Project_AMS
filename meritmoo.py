import pandas as pd
import mysql.connector as con
#from reportlab.lib.pagesizes import letter, landscape
#from reportlab.platypus import SimpleDocTemplate, Table
import csv

'''
def convert_csv_to_pdf(csv_file, pdf_file):
    # Set the page size to landscape and adjust the width
    page_width, page_height = 3800,1400
    table_width = page_width # Adjust the margin as needed

    # Create a PDF document
    pdf = SimpleDocTemplate(pdf_file, pagesize=(page_width, page_height))

    # Open the CSV file and read its contents
    with open(csv_file, 'r') as file:
        csv_data = list(csv.reader(file))

    # Calculate the number of columns in the table
    num_columns = len(csv_data[0])
    
    # Create a table from the CSV data
    table = Table(csv_data)
    
    # Build the PDF document with the table
    elements = [table]
    pdf.build(elements)
'''


def gensy():
    #----------below code generate merit list for the sy student--------
    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
    mycursor = c.cursor()

    query = 'select REG_NO, NAME, GENDER, HSSC_SCI, VOC_ABD, ITI_ABC, SSC_ENG, SSC_MAT, SSC_SCI, SSC_Q_TOT, SSC_AD_MARKS, SSC_M_TOT, HSSC_MAT, HSSC_S, HSSC_V, HSSC_Q_TOT_ALL, ITI, ITI_TOT, HSSC_AD_MKS, HSSC_Q_TOT, VOC_Q_TOT, ITI_Q_TOT, SSC_Q_PER, HSSC_Q_PER, ITI_Q_PER, HSSC__SCI_EL, VOC_ABD_EL, ITI_ABC_EL, REMARK from direct_sy'
    mycursor.execute(query)
    data = mycursor.fetchall()
    rg, nm, gnd, hssci, vabd, iabc, seng, ssci, smat, sqtot, sad, smtot, hsmat, hsss, hssv, hsqtall, iti, ititol, hsad, hsqt, vqt, iqt, sper, hsper, iper, hsciel, voel, itiel, remark = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] 

    for REG_NO, NAME, GENDER, HSSC_SCI, VOC_ABD, ITI_ABC, SSC_ENG, SSC_MAT, SSC_SCI, SSC_Q_TOT, SSC_AD_MARKS, SSC_M_TOT, HSSC_MAT, HSSC_S, HSSC_V, HSSC_Q_TOT_ALL, ITI, ITI_TOT, HSSC_AD_MKS, HSSC_Q_TOT, VOC_Q_TOT, ITI_Q_TOT, SSC_Q_PER, HSSC_Q_PER, ITI_Q_PER, HSSC__SCI_EL, VOC_ABD_EL, ITI_ABC_EL, REMARK in data:
        rg.append(REG_NO)
        nm.append(NAME)
        gnd.append(GENDER)
        hssci.append(HSSC_SCI)
        vabd.append(VOC_ABD)
        iabc.append(ITI_ABC)
        seng.append(SSC_ENG)
        ssci.append(SSC_SCI)
        smat.append(SSC_MAT)
        sqtot.append(SSC_Q_TOT)
        sad.append(SSC_AD_MARKS)
        smtot.append(SSC_M_TOT)
        hsmat.append(HSSC_MAT)
        hsss.append(HSSC_S)
        hssv.append(HSSC_V)
        hsqtall.append(HSSC_Q_TOT_ALL)
        iti.append(ITI)
        ititol.append(ititol)
        hsad.append(HSSC_AD_MKS)
        hsqt.append(HSSC_Q_TOT)
        vqt.append(VOC_Q_TOT)
        iqt.append(ITI_Q_TOT)
        sper.append(SSC_Q_PER)
        hsper.append(HSSC_Q_PER)
        iper.append(ITI_Q_PER)
        hsciel.append(HSSC__SCI_EL)
        voel.append(VOC_ABD_EL)
        itiel.append(ITI_ABC_EL)
        remark.append(REMARK)

    dic = {'REG.NO.':rg, 'NAME':nm, 'GENDER':gnd, 'HSSC(SCI)':hssci, 'VOC=A,B,D':vabd, 'ITI=A,B,C':iabc, 'SSC-ENG.(100)':seng, 'SSC-MAT-100':smat, 'SSC-SCI-100':ssci, 'SSC-Q.TOTA-600':sqtot, 'SSC-AD.MKS':sad, 'SSC-M.TOTAL':smtot, 'HSSC-MAT.(100)':hsmat, 'HSSC-S(600)':hsss, 'HSSC-V(800)':hssv, 'HSSC-Q-TOTAL-600-ALL':hsqtall, 'ITI(700)':iti, 'ITI-Q-TOTAL-700':iqt, 'HSSC-AD.MKS':hsad, 'HSSC-Q.TOT-600':hsqt, 'VOC-Q.TOT-800':vqt, 'ITI-Q.TOT-700':iqt, 'SSC-Q.%':sper, 'HSSC-Q.%':hsper, 'ITI-Q.%':iper, 'HSSC.(SCI)':hsciel, 'VOC-(A,B,D)':voel, 'ITI-(A,B,C)':itiel, 'REMARK COMPLIANCE':remark }
    df = pd.DataFrame(dic)
    print('done dic')
    for cat in ['HSSC(SCI)','VOC=A,B,D','ITI=A,B,C']:
        print('inside for ')
        course = "ENGINEERING (DIRECT SECOND YEAR)"

        if cat == 'VOC=A,B,D':
            print('inside voc cond')
            cat_sep = ['A','B','D']
            i=0
            for indv_cat in cat_sep:
                category = 'VOC {}'.format(indv_cat)
                filtered_EL = pd.DataFrame()
                filtered_NE = pd.DataFrame()
                print('inside cat for')
                filtered_EL = df[(df[cat]== cat_sep[i]) & (df['VOC-(A,B,D)'] == 'EL')]
                sortedel_df = filtered_EL.sort_values(by=['VOC-Q.TOT-800', 'SSC-M.TOTAL', 'SSC-MAT-100','SSC-ENG.(100)'], ascending=False)
                sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))
                print('done el sort data') 
                filtered_NE = df[(df[cat]== cat_sep[i]) & (df['VOC-(A,B,D)'] == 'NE')]
                sortedne_df = filtered_NE.sort_values(by=['VOC-Q.TOT-800', 'SSC-M.TOTAL', 'SSC-MAT-100','SSC-ENG.(100)'], ascending=False)
                sortedne_df.insert(0, 'merit_no', None)
                i+=1
                print('done ne sort')
                if not sortedel_df.empty:
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'DIRECTORATE OF TECHNICAL EDUCATION, PORVORIM GOA'}\n")
                            f.write(f"{'MERIT LIST, DIPLOMA 2022-23' }\n")
                            f.write(f"{'COURSE : {}'.format(course)}\n")
                            f.write(f"{'CATEGORY : {}'.format(category)}\n")
                            sortedel_df.to_csv(f, index=False)
                            f.write(f'\n\n\n')
                            print('done writing in el voc')
                     
                if not filtered_NE.empty:
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'NOT ELIGIBLE CASES'}\n")
                            sortedne_df.to_csv(f, index=False)
                            f.write("\n\n\n\n")
                            print('done writing in ne voc')
            
        elif cat == 'ITI=A,B,C':
            print('inside iti')
            cat_sep = ['A','B','C']
            i=0
            for indv_cat in cat_sep:
                category = 'ITI {}'.format(indv_cat)
                filtered_EL = pd.DataFrame()
                filtered_NE = pd.DataFrame()

                filtered_EL = df[(df[cat]== cat_sep[i]) & (df['ITI-(A,B,C)'] == 'EL')]
                sortedel_df = filtered_EL.sort_values(by=['ITI-Q.TOT-700', 'SSC-M.TOTAL', 'SSC-MAT-100','SSC-ENG.(100)'], ascending=False)
                sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))
                    
                filtered_NE = df[(df[cat]== cat_sep[i]) & (df['ITI-(A,B,C)'] == 'NE')]
                sortedne_df = filtered_NE.sort_values(by=['ITI-Q.TOT-700', 'SSC-M.TOTAL', 'SSC-MAT-100','SSC-ENG.(100)'], ascending=False)
                sortedne_df.insert(0, 'merit_no', None)
                i+=1
                print('done filter sort of iti')
                if not sortedel_df.empty:
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'DIRECTORATE OF TECHNICAL EDUCATION, PORVORIM GOA'}\n")
                            f.write(f"{'MERIT LIST, DIPLOMA 2022-23'}\n")
                            f.write(f"{'COURSE : {}'.format(course)}\n")
                            f.write(f"{'CATEGORY : {}'.format(category)}\n")
                            sortedel_df.to_csv(f, index=False)
                            f.write(f'\n\n\n')
                            print('done writing ITI')
                     
                if not filtered_NE.empty:
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'NOT ELIGIBLE CASES'}\n")
                            sortedne_df.to_csv(f, index=False)
                            f.write("\n\n\n\n")
                            print('done Writing ITI NE')
        elif cat == 'HSSC(SCI)':
            print('inside hssc sci')
            cat_sep = ['HSSC(SCI)']
            i=0
            for indv_cat in cat_sep:
                category = 'HSSC(SCIENCE)'
                filtered_EL = pd.DataFrame()
                filtered_NE = pd.DataFrame()

                filtered_EL = df[(df['HSSC(SCI)'] == '1') & (df['HSSC.(SCI)'] == 'EL')]
                sortedel_df = filtered_EL.sort_values(by=['HSSC-S(600)','HSSC-MAT.(100)', 'SSC-M.TOTAL', 'SSC-ENG.(100)'], ascending=False)
                sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))
                    
                filtered_NE = df[(df['HSSC(SCI)']== '1') & (df['HSSC.(SCI)'] == 'NE')]
                sortedne_df = filtered_NE.sort_values(by=['HSSC-S(600)','HSSC-MAT.(100)', 'SSC-M.TOTAL', 'SSC-ENG.(100)'], ascending=False)
                sortedne_df.insert(0, 'merit_no', None)
                i+=1
                print('done sorting')
                if not sortedel_df.empty:
                        print("not empty hssc")
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'DIRECTORATE OF TECHNICAL EDUCATION, PORVORIM GOA'}\n")
                            f.write(f"{'MERIT LIST, DIPLOMA 2022-23'}\n")
                            f.write(f"{'COURSE : {}'.format(course)}\n")
                            f.write(f"{'CATEGORY : {}'.format(category)}\n")
                            sortedel_df.to_csv(f, index=False)
                            f.write(f'\n\n\n')
                            print('done writing in hssc')
                     
                if not filtered_NE.empty:
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'NOT ELIGIBLE CASES'}\n")
                            sortedne_df.to_csv(f, index=False)
                            f.write("\n\n\n\n")
                            print('done writing in hssc SCI')
        else:
            continue 
    print('Generated Merit List')
    

    
def gen_mer():


    #--------------below program generates merit list for fy stydents-------------------
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
        
    print('defining dictionary \n')
    dic = {'REG.NO.(F)':rg, 'NAME':nm, 'GENDER':gnd, 'MO':mo, 'PY':py, 'ENGG':engg, 'GEN/CSP':gc, 'SC/ST/OBC':sc, 'PWD/FF/ESM':pwd, 'GN/NRI/LA/OGA':gnri, 'SSC-ENG-(100)':seng, 'SSC-MAT-100':smat, 'SSC-SCI-100':ssci, 'SSC-TOTAL-600':stot, 'SSC-AD.MKS.':sad, 'SSC-Q-TOTAL':sqtot, 'HSSC-ENG-(100)':hseng, 'HSSC-PHY-(100)':hsphy, 'HSSC-CHE-(100)':hsche, 'HSSC-MAT-(100)':hsmat, 'HSSC-BIO-(100)':hsbio, 'PCM':pcm, 'PCB':pcb, 'PCM/B':pcmb, 'MAT/BIO':matbio, 'HSSC-A(600)':hssa, 'HSSC-C(600)':hssc, 'HSSC-S(600)':hsss, 'HSSC-V(600)':hssv, '600-HSSC-ALL':hssall, 'HSSC-AD.MKS.':hssad, 'HSSC-Q.TOT-600+':hssqtot, 'SSC-%':sper, 'HSSC-%':hsper, 'ENGG_':engel, 'PY_':pyel, 'MO_':moel, 'REMARKS/COMLIANCE (DOCUMENTS TO BE SUBMITTED)':remark,}
    df = pd.DataFrame(dic)



    print('going thorough first loop\n')
    for c in ['MO','PY','ENGG']:
        print('entered into 1st under enum',c)
        if c == 'MO':
            course = 'Modern Office Practices'
            elig = df['MO_']
        elif c == 'PY':
            course = 'Pharmacy'
            elig = df['PY_']
        elif c == 'ENGG':
            course = 'Engineering'
            elig = df['ENGG_']
        else: 
            continue
        print('going for second if',course)
        if c == 'MO' or c == 'PY':
            for cat in ['GEN/CSP','SC/ST/OBC','PWD/FF/ESM','GN/NRI/LA/OGA']:
                cat_sep = cat.split('/')
                print('checked category',cat,cat_sep)
                # merge_EL_df = pd.DataFrame()
                # temp_NE_df = pd.DataFrame()
                i=0
                for individ_cat in cat_sep:
                    print('i is',i)
                    filtered_EL_df = pd.DataFrame()
                    filtered_NE_df = pd.DataFrame()
                    print("inside filter loop",individ_cat)
                    #filtering the data on the basis of course, category and on eligiblility as per the applied course under particular category.
                    filtered_EL_df = df[(df[cat] == cat_sep[i]) & (df[c] == 1) & (elig == 'EL')]
                    #sorting out the data as per the merit list criteria
                    sortedel_df = filtered_EL_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
                    sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))
                    print('filtered and sorted el\n')


                    #doing the same for the not eligible cases
                    filtered_NE_df = df[(df[cat] == cat_sep[i]) & (df[c] == 1) & (elig == 'NE')]
                    sortedne_df = filtered_NE_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 
                    'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
                    sortedne_df.insert(0, 'merit_no', None)
                    print('filtered and sorted NE\n')
                    i+=1
                    print('i is after iteration',i)
                    if individ_cat == 'GEN':
                        cat_str = 'GENERAL'
                    elif individ_cat == 'CSP':
                        cat_str = 'CSP'
                    elif individ_cat == 'SC':
                        cat_str = 'SC'
                    elif individ_cat == 'ST':
                        cat_str = 'ST'
                    elif individ_cat == 'OBC':
                        cat_str = 'OBC'
                    elif individ_cat == 'PWD':
                        cat_str = 'PWD'
                    elif individ_cat == 'FF':
                        cat_str = 'FF'
                    elif individ_cat == 'ESM':
                        cat_str = 'ESM'
                    elif individ_cat == 'GN':
                        cat_str = 'GN'
                    elif individ_cat == 'NRI':
                        cat_str = 'NRI'
                    elif individ_cat == 'LA':
                        cat_str = 'LA'
                    elif individ_cat == 'OGA':
                        cat_str = 'OGA'
                    else:
                        continue
                    print('done with if elif')
                    print('checking condition if empty')
                    if not sortedel_df.empty:
                        print('inside if')
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'DIRECTORATE OF TECHNICAL EDUCATION, PORVORIM GOA'}\n")
                            f.write(f"{'MERIT LIST, DIPLOMA 2022-23'}\n")
                            f.write(f"{'COURSE : {}'.format(course)}\n")
                            f.write(f"{'CATEGORY : {}'.format(cat_str)}\n")
                            sortedel_df.to_csv(f, index=False)
                            f.write(f'\n\n\n')
                            print('done with el csv')
                    print('checking if NE empt')
                    if not filtered_NE_df.empty:
                        print('checked ne inside')
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'NOT ELIGIBLE CASES'}\n")
                            sortedne_df.to_csv(f, index=False)
                            f.write("\n\n\n\n")
                            print('done with NE csv')
        elif c == 'ENGG':
            for cat in ['GEN/CSP','SC/ST/OBC','PWD/FF/ESM','GN/NRI/LA/OGA']:
                cat_sep = cat.split('/')
                print('checked category',cat,cat_sep)
                # merge_EL_df = pd.DataFrame()
                # temp_NE_df = pd.DataFrame()
                i=0
                for individ_cat in cat_sep:
                    print('i is',i)
                    filtered_EL_df = pd.DataFrame()
                    filtered_NE_df = pd.DataFrame()
                    print("inside filter loop",individ_cat)
                    #filtering the data on the basis of course, category and on eligiblility as per the applied course under particular category.
                    filtered_EL_df = df[(df[cat] == cat_sep[i]) & (df[c] == 1) & (elig == 'EL')]
                    #sorting out the data as per the merit list criteria
                    sortedel_df = filtered_EL_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
                    sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))
                    print('filtered and sorted el\n')


                    #doing the same for the not eligible cases
                    filtered_NE_df = df[(df[cat] == cat_sep[i]) & (df[c] == 1) & (elig == 'NE')]
                    sortedne_df = filtered_NE_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 
                    'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
                    sortedne_df.insert(0, 'merit_no', None)
                    print('filtered and sorted NE\n')
                    i+=1
                    print('i is after iteration',i)
                    if individ_cat == 'GEN':
                        cat_str = 'GENERAL'
                    elif individ_cat == 'CSP':
                        cat_str = 'CSP'
                    elif individ_cat == 'SC':
                        cat_str = 'SC'
                    elif individ_cat == 'ST':
                        cat_str = 'ST'
                    elif individ_cat == 'OBC':
                        cat_str = 'OBC'
                    elif individ_cat == 'PWD':
                        cat_str = 'PWD'
                    elif individ_cat == 'FF':
                        cat_str = 'FF'
                    elif individ_cat == 'ESM':
                        cat_str = 'ESM'
                    elif individ_cat == 'GN':
                        cat_str = 'GN'
                    elif individ_cat == 'NRI':
                        cat_str = 'NRI'
                    elif individ_cat == 'LA':
                        cat_str = 'LA'
                    elif individ_cat == 'OGA':
                        cat_str = 'OGA'
                    else:
                        continue
                    print('done with if elif')
                    print('checking condition if empty')
                    if not sortedel_df.empty:
                        print('inside if')
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'DIRECTORATE OF TECHNICAL EDUCATION, PORVORIM GOA'}\n")
                            f.write(f"{'MERIT LIST, DIPLOMA 2022-23'}\n")
                            f.write(f"{'COURSE : {}'.format(course)}\n")
                            f.write(f"{'CATEGORY : {}'.format(cat_str)}\n")
                            sortedel_df.to_csv(f, index=False)
                            f.write(f'\n\n\n')
                            print('done with el csv')
                    print('checking if NE empt')
                    if not filtered_NE_df.empty:
                        print('checked ne inside')
                        with open("F:\StudentData\Merit_list\FSYmerit.csv","a") as f:
                            f.write(f"{'NOT ELIGIBLE CASES'}\n")
                            sortedne_df.to_csv(f, index=False)
                            f.write("\n\n\n\n")
                            print('done with NE csv')
    print("GENERATED THE MERIT LIST")   
    gensy()


       
