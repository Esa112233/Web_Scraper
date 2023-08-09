import mysql.connector

db = mysql.connector.connect(

    host="localhost",
    user="Esa",
    password="Loveesamousa1",
    database ="testdatabase"
)

mycursor = db.cursor()
try:

    mycursor.execute("CREATE TABLE Register (name VARCHAR(50), password VARCHAR(50))")
except:
    pass

def dta_print_all():
    mycursor.execute("SELECT * FROM Register")
    for x in mycursor:
        print(x)
    

def dta_print():
    for x in mycursor:
        print(x)

def registered(username):
    mycursor.execute("SELECT EXISTS (SELECT * FROM Register WHERE name=%s)", (username,))
    val =  bool(mycursor.fetchone()[0])
    return(val)
    



def register(username, password):
    status = registered(username)
    if status is False:
        mycursor.execute("INSERT INTO Register(name, password) VALUE(%s, %s)", (username, password))
        db.commit()
        return status
    else:
        return status
        


def delete():
    mycursor.execute("DELETE FROM Register WHERE name='hi'")
    db.commit()
    dta_print()


def get_dta():
    mycursor.execute("SELECT * FROM Register WHERE name=%s", ("Esa",))
    dta_print()


def login(username, password):
    pass


        
    
if __name__ == "__main__":
    #registered("Esa", "swiss")
    #delete()
    #get_dta()
    #dta_print_all()
    pass