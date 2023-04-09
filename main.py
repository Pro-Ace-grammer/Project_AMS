#database connection using python
#so first we import mysql.connector (connector to databases)
import mysql.connector as connector
#so below here we define a class, lets say here as DB just to pack up our entire module
class DB:
#we  use the below __init__ function to (initialise )assign values to data members of class when object of class is created
#it is executed when the class is being initiated.
#basically it is a constructor that we will be using i.e. __init__ function is called the constructor
    def __init__(self): #self is reference to current instance of the class, used to access variable belonging to the class
        # below is the body of constructor.
        self.testcon = connector.connect(host='localhost',port='3306',user='root',password='Yash_Arsu_00510',database='pythontest')
        #we make query here as to create table if does not exist.
        query='create table if not exists user(userID int primary key, userName varchar(30), phone varchar(10))'
        #so to fire up this query we would first need to create a cursor
        #cursor is a object used to execute SQL queries
        #it acts as middleware between database connection and SQL query.. it is created after db connection.
        #so we use the variable testcon to make cursor.
        cur = self.testcon.cursor() #here we define or create
        cur.execute(query) # here we fire up or exeute.
        print("Created")
    
    # now we come out of the constructor first 
    # here we will try to make insert method(function) to insert data into table
    def insert_user(self,userid,username,phone):  #this is normally what we do in db
        #now below we define query.... we use format method to make it dynamic
        query="insert into user(userID,userName,phone)""values({},'{}','{}')".format(userid,username,phone)
        print(query)
        #now we fire the query
        cur=self.testcon.cursor()
        cur.execute(query)
        #now we commit to save the changes
        self.testcon.commit()
        print("user saved to db")




    
#now we do the main coding to create objects 
test=DB()  #thats it
#to invoke insert constructor
test.insert_user(29,"Sunil Banda","8896533257")
#print(testcon)