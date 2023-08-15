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
    mycursor.execute("SELECT * FROM Esa")
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
   
    mycursor.execute("SELECT EXISTS (SELECT * FROM Register WHERE name=%s AND password=%s)", (username, password))
    val =  bool(mycursor.fetchone()[0])
    if val is True:
        create_query = f"CREATE TABLE {username} (email VARCHAR(50), link VARCHAR(500))"
        try:
            mycursor.execute(create_query)
            db.commit()
            tru = 1
        except:
            pass
        tru = 1
        if tru == 1:
            return True
    else:
        return False
    

def check_result_data(email_dict, table_name):
    email_url_tuple_list = list((k, v) for k, v in email_dict.items())
    checked_duplicates = list() #this is a list of tuples
    for i, n in enumerate(email_url_tuple_list):
        query_get = f"SELECT EXISTS (SELECT * FROM {table_name} WHERE email=%s)"
        query_insert = f"INSERT INTO {table_name}(email, link) VALUE(%s, %s)"
        mycursor.execute(query_get, (n[0],))
        exists = bool(mycursor.fetchone()[0])
        if exists is False:
            try:
                mycursor.execute(query_insert, (n[0], n[1]))
                db.commit()
                checked_duplicates.append((n[0], n[1]))
            except:
                pass
    return checked_duplicates

            




        
    
if __name__ == "__main__":
    #registered("Esa", "swiss")
    # delete()
    #get_dta()
    dta_print_all()
    #mycursor.execute("DELETE FROM Esa")
    #db.commit()
    
  