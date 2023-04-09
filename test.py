import mysql.connector as con

class datbas:
    def __init__(self):
        self.test = con.connect(host='localhost',port='3306',user='root',password='Yash_Arsu_00510',database='project_ams')
       # query="create table if not exists marks(regno int primary key, sname varchar(20), math int, sci int, eng int)"
      #  cur = self.test.cursor() 
       # cur.execute(query)
       # print('Created successfully')

    def inser(self,reg,name,m,s,e):
        query="insert into marks(regno, sname, math, sci, eng)""values({},'{}',{},{},{})".format(reg,name,m,s,e)
        Cur = self.test.cursor()
        Cur.execute(query)
        self.test.commit()
        print('Added to database')

    def selec(self):
        query="select * from marks;"
        cur= self.test.cursor()
        cur.execute(query)
        print('this is your table after commits')
d = datbas()
reg=input('Registration No: ')
nm=input('name: ')
gen=input('gender: ')

d.inser(reg,nm,m=input('math marks: '),s=input('science marks: '),e=input('english marks: '))
d.selec()
# while(True):
#     d = datbas()
#     a=input("1. insert \n2. Display the table \n Any other key to exit: ")
#     b=int(a)
#     if(b==1):
#         #d = datbas()
#         d.inser(input('Registration No: '),input('name: '),m=input('math marks: '),s=input('science marks: '),e=input('english marks: '))
#     elif(b==2):
#         d.selec()
#     else:
#         exit