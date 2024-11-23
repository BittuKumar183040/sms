import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

db=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def admin_check(aname,apass):
    print("Checking --- ", aname, apass)
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM admin WHERE name = '%s' and pass='%s';" %(aname,apass))
    
    try:
        mycursor.fetchall()[0][0]
        mycursor.execute('update admin set status=1 where name="%s" and pass="%s";' %(aname,apass))
        db.commit()
        return True
    except:
        return False
def shop_check(user_id, apass):
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM shops WHERE id = '%s' and password='%s';" %(user_id,apass))
    
    try:
        mycursor.fetchall()[0][0]
        mycursor.execute('update shops set status=1 where id="%s" and password="%s";' %(user_id,apass))
        db.commit()
        return True
    except:
        return False

def customer_check(id):
    mycursor=db.cursor()
    try:
        mycursor.execute("SELECT * FROM customer WHERE c_ID='%s'"%id)
        return mycursor.fetchall()[0]
        
    except:
        return False

def item_search(id,shop_name):
    mycursor=db.cursor()
    try:
        mycursor.execute("SELECT * FROM %s WHERE Item_no='%s'"%(shop_name,id))
        return mycursor.fetchall()[0]
    except:
        return False

def admin_logout(aname):
    mycursor=db.cursor()
    mycursor.execute('update admin set status=0 where name="%s";' %aname)
    db.commit()

def count_cust(tname):
    mycursor=db.cursor()
    try:
        mycursor.execute('select count(*) from %s;' %tname)
        return (mycursor.fetchall()[0][0])
    except:
        return False
def customer_list():
    mycursor=db.cursor()
    try:
        mycursor.execute('select * from customer')
        return (mycursor.fetchall())
    except:
        return False

#Update Data
def update_cust(new_data_list):
    mycursor=db.cursor()
    try:
        mycursor.execute("UPDATE customer SET Name='%s', contact ='%s',email='%s',Address='%s',pincode='%s' WHERE c_ID='%s';" %(new_data_list))
        db.commit()
        print(mycursor.rowcount, " Row is Affected")
    except:
        print("Data Not Inserted")
def add_cust(c_data):
    mycursor=db.cursor()
    try:
        mycursor.execute("INSERT INTO customer VALUES('%s','%s','%s','%s','%s','%s');"%c_data)
        db.commit()
        print(mycursor.rowcount," Row inserted")
    except:
        print("Error: Connection")

def delete_row(table_name,id):
    mycursor=db.cursor()
    try:
        mycursor.execute("DELETE FROM %s WHERE c_ID='%s';" %(table_name,id))
        db.commit()
        print(mycursor.rowcount, " Row is removed.")
    except:
        print("Something Went Wrong!")

# Shop Management 

def shops_list():
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM shops;")
    # messagebox.showerror('All Data Loaded')
    return mycursor.fetchall()

def check_active():
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM shops WHERE status=1;")
    return mycursor.fetchall()

def update_shop(new_data_list):
    mycursor=db.cursor()
    try:
        # print(new_data_list)
        mycursor.execute("UPDATE shops SET name='%s', owner ='%s',phone_no='%s',type='%s',address='%s',status='%s' WHERE id='%s';" %(new_data_list))
        db.commit()
        print(mycursor.rowcount, " Row is Affected")
    except:
        print("Data Not Inserted")
def delete_shop_row(table_name,id):
    mycursor=db.cursor()
    try:
        mycursor.execute("DELETE FROM %s WHERE id='%s';" %(table_name,id))
        db.commit()
        print(mycursor.rowcount, " Row is removed")
    except:
        print("Something Went Wrong!!!")
def insert_shop(new_data_list):
    # print("INSERT INTO shops values('%s','%s','%s','%s','%s','%s','%s',%d);"%new_data_list)
    mycursor=db.cursor()
    try:
        mycursor.execute("INSERT INTO shops values('%s','%s','%s','%s','%s','%s','%s',%d);"%new_data_list)
        db.commit()
        print(mycursor.rowcount, " Row is removed")
    except:
        print("Something Went Wrong!!!")

def show_shop_items(id):
    mycursor=db.cursor()
    try:
        mycursor.execute("SELECT * FROM shop_%s;"%id)
        return mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE IF NOT EXISTS shop_%s(Item_no varchar(20) PRIMARY KEY,Item_name varchar(20),mrp int);"%id);
        return "No Data Found"
def add_items_into_shop(id,values):
    try:
        print("INSERT INTO shop_%s values %s;"%(id,values))
        # mycursor.execute("INSERT INTO shop_%s values %s;"%(id,values))
    except:
        pass;
def search_items_from_table(ref):
    mycursor=db.cursor()
    try:
        mycursor.execute("select Item_no FROM shop_123 WHERE Item_no LIKE '%s%%';" %ref)
        return mycursor.fetchall()
    except:
        print("No Data Matched")