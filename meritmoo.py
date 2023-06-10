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
                        with open("fsymerit.csv","a") as f:
                            f.write(f"{'DIRECTORATE OF TECHNICAL EDUCATION, PORVORIM GOA'.center(20)}\n")
                            f.write(f"{'MERIT LIST, DIPLOMA 2022-23'.center(20)}\n")
                            f.write(f"{'COURSE : {}'.format(course).center(20)}\n")
                            f.write(f"{'CATEGORY : {}'.format(cat_str).center(20)}\n")
                            sortedel_df.to_csv(f, index=False)
                            f.write(f'\n\n\n')
                            print('done with el csv')
                    print('checking if NE empt')
                    if not filtered_NE_df.empty:
                        print('checked ne inside')
                        with open("fsymerit.csv","a") as f:
                            f.write(f"{'NOT ELIGIBLE CASES'.center(20)}\n")
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
                        with open("fsymerit.csv","a") as f:
                            f.write(f"{'DIRECTORATE OF TECHNICAL EDUCATION, PORVORIM GOA'.center(20)}\n")
                            f.write(f"{'MERIT LIST, DIPLOMA 2022-23'.center(20)}\n")
                            f.write(f"{'COURSE : {}'.format(course).center(20)}\n")
                            f.write(f"{'CATEGORY : {}'.format(cat_str).center(20)}\n")
                            sortedel_df.to_csv(f, index=False)
                            f.write(f'\n\n\n')
                            print('done with el csv')
                    print('checking if NE empt')
                    if not filtered_NE_df.empty:
                        print('checked ne inside')
                        with open("fsymerit.csv","a") as f:
                            f.write(f"{'NOT ELIGIBLE CASES'.center(20)}\n")
                            sortedne_df.to_csv(f, index=False)
                            f.write("\n\n\n\n")
                            print('done with NE csv')
    print("GENERATED THE MERIT LIST")                 
           
gen_mer()            

'''    for course in ['MO']:
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
                f.write(f"Category: CSP\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')
            



        for category in ['SC/ST/OBC']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'SC') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'SC') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: SC\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')

        


        for category in ['SC/ST/OBC']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'ST') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'ST') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: ST\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')
        



        for category in ['SC/ST/OBC']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'OBC') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'OBC') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: OBC\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')



        
        for category in ['PWD/FF/ESM']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'PWD') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'PWD') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: PWD\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')

            


        for category in ['PWD/FF/ESM']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'FF') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'FF') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: FF\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['PWD/FF/ESM']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'ESM') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'ESM') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: ESM\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')


        
        
        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'GN') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'GN') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: GN\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'NRI') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'NRI') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: NRI\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'LA') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'LA') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: LA\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'OGA') & (df[course] == 1) & (df['MO_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'OGA') & (df[course] == 1) & (df['MO_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: OGA\n")
                f.write("Merit List \n")
    
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')


    








    #---------------------PY---------------------


    for course in ['PY']:
        # loop through each category
        for category in ['GEN/CSP']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'GEN') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'GEN') & (df[course] == 1) & (df['PY_'] == 'NE')]
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
           
            elig_df = df[(df[category] == 'CSP') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))
            
            nelig_df = df[(df[category] == 'CSP') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)
            # write sorted data to CSV file
            with open(f"merit_list.csv", 'a') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: CSP\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')
            



        for category in ['SC/ST/OBC']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'SC') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'SC') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: SC\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')

        


        for category in ['SC/ST/OBC']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'ST') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'ST') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: ST\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')
        



        for category in ['SC/ST/OBC']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'OBC') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'OBC') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: OBC\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')



        
        for category in ['PWD/FF/ESM']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'PWD') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'PWD') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: PWD\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')

            


        for category in ['PWD/FF/ESM']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'FF') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'FF') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: FF\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['PWD/FF/ESM']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'ESM') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'ESM') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: ESM\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')


        
        
        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'GN') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'GN') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: GN\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'NRI') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'NRI') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: NRI\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'LA') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'LA') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: LA\n")
                f.write("Merit List \n")
                
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')




        for category in ['GN/NRI/LA/OGA']:
            # filter dataframe to include only eligible students from current category and course
            elig_df = df[(df[category] == 'OGA') & (df[course] == 1) & (df['PY_'] == 'EL')]
            # sort dataframe based on merit list criteria
            sortedel_df = elig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            # add merit_no column
            sortedel_df.insert(0, 'merit_no', range(1, 1 + len(sortedel_df)))

            #performing same operation as done for the eligible students
            nelig_df = df[(df[category] == 'OGA') & (df[course] == 1) & (df['PY_'] == 'NE')]
            sortedne_df = nelig_df.sort_values(by=['600-HSSC-ALL', 'HSSC-ENG-(100)', 'SSC-TOTAL-600','SSC-ENG-(100)'], ascending=False)
            sortedne_df.insert(0, 'merit_no', None)

            # write sorted data to CSV file
            with open(f"merit_list.csv", 'w') as f:
                # write table headers
                f.write(f"Course: {course}\n")
                f.write(f"Category: OGA\n")
                f.write("Merit List \n")
    
                # write sorted data
                sortedel_df.to_csv(f, index=False)
                # write blank rows for not eligible cases
                f.write("\n\nNot Eligible Cases:\n")
                sortedne_df.to_csv(f, index=False)
                f.write('\n\n\n\n')
    print('GENERATED THE MERIT LIST')'''
