import mysql.connector
from tkinter import messagebox 
db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="sbs"
    )

def adminCheck(aname,apass):
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM admin WHERE name = '%s' and pass='%s';" %(aname,apass))
    
    try:
        mycursor.fetchall()[0][0]
        mycursor.execute('update admin set status=1 where name="%s" and pass="%s";' %(aname,apass))
        db.commit()
        return True
    except:
        return False
def shopCheck(aname,apass):
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM shops WHERE id = '%s' and password='%s';" %(aname,apass))
    
    try:
        mycursor.fetchall()[0][0]
        mycursor.execute('update shops set status=1 where id="%s" and password="%s";' %(aname,apass))
        db.commit()
        return True
    except:
        return False

def customerCheck(id):
    mycursor=db.cursor()
    try:
        mycursor.execute("SELECT * FROM customer WHERE c_ID='%s'"%id)
        return mycursor.fetchall()[0]
        
    except:
        return False

def itemSearch(id,shopName):
    mycursor=db.cursor()
    try:
        mycursor.execute("SELECT * FROM %s WHERE Item_no='%s'"%(shopName,id))
        return mycursor.fetchall()[0]
    except:
        return False

def adminLogout(aname):
    mycursor=db.cursor()
    mycursor.execute('update admin set status=0 where name="%s";' %aname)
    db.commit()

def countCust(tname):
    mycursor=db.cursor()
    try:
        mycursor.execute('select count(*) from %s;' %tname)
        return (mycursor.fetchall()[0][0])
    except:
        return False
def customerList():
    mycursor=db.cursor()
    try:
        mycursor.execute('select * from customer')
        return (mycursor.fetchall())
    except:
        return False

#Update Data
def updateCust(new_dataList):
    mycursor=db.cursor()
    try:
        # print(new_dataList)
        mycursor.execute("UPDATE customer SET Name='%s', contact ='%s',email='%s',Address='%s',pincode='%s' WHERE c_ID='%s';" %(new_dataList))
        db.commit()
        print(mycursor.rowcount, " Row is Affected")
    except:
        print("Data Not Inserted")
def addCust(c_data):
    mycursor=db.cursor()
    try:
        mycursor.execute("INSERT INTO customer VALUES('%s','%s','%s','%s','%s','%s');"%c_data)
        db.commit()
        print(mycursor.rowcount," Row inserted")
    except:
        print("Error: Connection")

def deleteRow(tableName,id):
    mycursor=db.cursor()
    try:
        mycursor.execute("DELETE FROM %s WHERE c_ID='%s';" %(tableName,id))
        db.commit()
        print(mycursor.rowcount, " Row is removed")
    except:
        print("Something Went Wrong!!!")

# Shop Management 

def shopsList():
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM shops;")
    # messagebox.showerror('All Data Loaded')
    return mycursor.fetchall()

def checkActive():
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM shops WHERE status=1;")
    return mycursor.fetchall()

def updateShop(new_dataList):
    mycursor=db.cursor()
    try:
        # print(new_dataList)
        mycursor.execute("UPDATE shops SET name='%s', owner ='%s',phone_no='%s',type='%s',address='%s',status='%s' WHERE id='%s';" %(new_dataList))
        db.commit()
        print(mycursor.rowcount, " Row is Affected")
    except:
        print("Data Not Inserted")
def deleteShopRow(tableName,id):
    mycursor=db.cursor()
    try:
        mycursor.execute("DELETE FROM %s WHERE id='%s';" %(tableName,id))
        db.commit()
        print(mycursor.rowcount, " Row is removed")
    except:
        print("Something Went Wrong!!!")
def insertShop(new_dataList):
    # print("INSERT INTO shops values('%s','%s','%s','%s','%s','%s','%s',%d);"%new_dataList)
    mycursor=db.cursor()
    try:
        mycursor.execute("INSERT INTO shops values('%s','%s','%s','%s','%s','%s','%s',%d);"%new_dataList)
        db.commit()
        print(mycursor.rowcount, " Row is removed")
    except:
        print("Something Went Wrong!!!")

def showShopItems(id):
    mycursor=db.cursor()
    try:
        mycursor.execute("SELECT * FROM shop_%s;"%id)
        return mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE IF NOT EXISTS shop_%s(Item_no varchar(20) PRIMARY KEY,Item_name varchar(20),mrp int);"%id);
        return "No Data Found"
def addItemsIntoShop(id,values):
    # mycursor=db.cursor()
    try:
        print("INSERT INTO shop_%s values %s;"%(id,values))
        # mycursor.execute("INSERT INTO shop_%s values %s;"%(id,values))
    except:
        pass;
def searchItemsFromTable(ref):
    mycursor=db.cursor()
    try:
        mycursor.execute("select Item_no FROM shop_123 WHERE Item_no LIKE '%s%%';" %ref)
        return mycursor.fetchall()
    except:
        print("No Data Matched")