#I've shown my project to Rajat





 # if c == 'HSSC(SCI)':
        #     course = 'HSSC(SCI)'
        #     elig = df['HSSC.(SCI)']
        # elif c == 'VOC=A,B,D' and df['VOC-(A,B,D)'] == 'A':
        #     course = 'VOC-(A,B,D)'
        #     elig = df['VOC-(A,B,D)']
        # elif c == 'VOC=A,B,D' and df['VOC-(A,B,D)'] == 'B':
        #     course = 'VOC-(A,B,D)'
        #     elig = df['VOC-(A,B,D)']
        # elif c == 'VOC=A,B,D' and df['VOC-(A,B,D)'] == 'D':
        #     course = 'VOC-(A,B,D)'
        #     elig = df['VOC-(A,B,D)']
        # elif c == 'ITI=A,B,C' and df['ITI-(A,B,C)'] == 'A':
        #     course = 'ITI=A,B,C'
        #     elig = df['ITI-(A,B,C)']
        # elif c == 'ITI=A,B,C' and df['ITI-(A,B,C)'] == 'B':
        #     course = 'ITI=A,B,C'
        #     elig = df['ITI-(A,B,C)']
        # elif c == 'ITI=A,B,C' and df['ITI-(A,B,C)'] == 'C':
        #     course = 'ITI=A,B,C'
        #     elig = df['ITI-(A,B,C)']
        # else:
        #     continue





'''import pandas as pd
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
'''























'''
def submit_form_SY(reg_no, name, gender, hssc_if, voc_if, iti_if, ssc_eng, ssc_mat, ssc_sci, ssc_tot, ssc_ad, ssc_m_tot, hssc_mat, hssc_s, hssc_v, hssc_q_tot_all, iti, iti_q_tot_all, hssc_ad, hssc_q_tot, voc_q_tot, iti_q_tot, ssc_per, hssc_per, iti_per, hssc_sci_el, voc_el, iti_el, sy_remarks_entry):


    c = con.connect(host='localhost',user='root',password='yasharsu',database='project_ams')
    mycursor = c.cursor()
    query="insert into direct_sy(REG_NO, NAME, GENDER, HSSC_SCI, VOC_ABD, ITI_ABC, SSC_ENG, SSC_MAT, SSC_SCI, SSC_Q_TOT, SSC_AD_MARKS, SSC_M_TOT, HSSC_MAT, HSSC_S, HSSC_V, HSSC_Q_TOT_ALL, ITI, ITI_TOT, HSSC_AD_MKS, HSSC_Q_TOT, VOC_Q_TOT, ITI_Q_TOT, SSC_Q_PER, HSSC_Q_PER, ITI_Q_PER, HSSC__SCI_EL, VOC_ABD_EL, ITI_ABC_EL, REMARK) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}')".format(reg_no, name, gender, hssc_if, voc_if, iti_if, ssc_eng, ssc_mat, ssc_sci, ssc_tot, ssc_ad, ssc_m_tot, hssc_mat, hssc_s, hssc_v, hssc_q_tot_all, iti, iti_q_tot_all, hssc_ad, hssc_q_tot, voc_q_tot, iti_q_tot, ssc_per, hssc_per, iti_per, hssc_sci_el, voc_el, iti_el, sy_remarks_entry)

    mycursor = c.cursor()
    mycursor.execute(query)
    c.commit()
    print("successfully inserted the data")

'''





'''
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 1948, in __call__      
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python311\Lib\site-packages\customtkinter\windows\widgets\ctk_button.py", line 553, in _clicked
    self._command()
  File "c:\Users\Sunny\Project_AMS\meritmoo.py", line 82, in gen_mer
    if((df[category] == 'GEN') & (df[course] == 1) & (df['MO_'] == 'NE')):
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 1466, 
in __nonzero__
    raise ValueError(
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

'''

















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