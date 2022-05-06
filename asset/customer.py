from tkinter import *
from asset.welcomeCustomer import customerAfterLogin
def customerPanel():
    window=Tk()
    window.geometry("800x500+50+100")
    window.title("Customer Login Window")
    leftFrame=Frame(window)
    leftFrame.grid(row=0,column=0)

    customerBtn=Button(leftFrame,text="Sign In")
    customerBtn.grid(column=0,row=0,padx=20)
    adminBtn=Button(leftFrame,text="Admin Login")
    adminBtn.grid(column=1,row=0,padx=20)
    shopBtn=Button(leftFrame,text="Shop Login")
    shopBtn.grid(column=2,row=0,padx=20)

    rightFrame=Frame(window)
    rightFrame.grid(row=0,column=1)

    loginRightTop=Frame(rightFrame)
    loginRightTop.grid(row=0,column=0)

    Login=Label(loginRightTop,text="Customer Login")
    Login.pack()

    loginCred=LabelFrame(rightFrame,text="Login Crediential")
    loginCred.grid(row=1,column=0)

    Login=Label(loginCred,text="Customer ID").grid(row=0,column=0)
    adminBtn=Entry(loginCred).grid(row=0,column=1)
    Login=Label(loginCred,text="Password").grid(row=1,column=0,pady=15)
    shopBtn=Entry(loginCred).grid(row=1,column=1,pady=15)

    def welcometo():
        window.destroy()
        customerAfterLogin()
    submitBtn=Button(loginCred,text="Login", command=welcometo).grid(row=2,column=0, columnspan=2)
    window.mainloop()