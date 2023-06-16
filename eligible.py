import mysql.connector as con
import pandas as pd
import os



#tocsv_fy()

def tocsv_sy():

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
    df_csv = df.to_csv('F:\StudentData\Eligibility\SY_data.csv')
    print("created succesfully")
    

# tocsv_sy()
#def read():
#    pd.read_csv()

def tocsv_fy():
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
    # username = os.getlogin()
    # path = "C:/Users/'{}'/Desktop/StudentData".format(username)
    # os.makedirs(path)
    # path = "F:/StudentData"
    # os.makedirs(path)
    df_csv = df.to_csv('F:\StudentData\Eligibility\FY_data1.csv')
    tocsv_sy()
    print("created succesfully")
   