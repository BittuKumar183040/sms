from tkinter import *

def customerAfterLogin():

    window=Tk()
    window.geometry("800x400+50+100")
    customer="Ron"
    customerName=Label(window,text="Welcome %s" %customer)
    customerName.place(relx=0.5,y=10)

    logoutBtn=Button(window,text="Logout")
    logoutBtn.place(relx=0.9,y=10)

    topFrame=Frame(window,bg="white")
    topFrame.pack(pady=(100,0),anchor="center")
    Label(topFrame,text="Shop Name").grid(row=0,column=0)
    Label(topFrame,text="Search Item").grid(row=0,column=1)
    Label(topFrame,text="Sort By").grid(row=0,column=2)
    searchShop=Entry(topFrame)
    searchShop.grid(row=1,column=0,padx=20)
    serachitem=Entry(topFrame)
    serachitem.grid(row=1,column=1,padx=20)
    sortList=Entry(topFrame)
    sortList.grid(row=1,column=2,padx=20)

    midFrame=LabelFrame(window,text="Search")
    midFrame.pack(pady=5)
    def headingLabel(Snum,item,shop,quantity,total,r):
        Label(midFrame,text=Snum,width=15).grid(row=r,column=0)
        Label(midFrame,text=item,width=15).grid(row=r,column=1)
        Label(midFrame,text=shop,width=15).grid(row=r,column=2)
        Label(midFrame,text=quantity,width=15).grid(row=r,column=3)
        Label(midFrame,text=total,width=15).grid(row=r,column=4)
    headingLabel("S.No","Item","Shop","Quantity","Total Paid",0)


    # searchedItem Output
    midFrame2=LabelFrame(window,text="")
    midFrame2.pack(pady=5)
    def dataFound(Snum,item,shop,quantity,total,r):
        Label(midFrame2,text=Snum,width=15).grid(row=r,column=0)
        Label(midFrame2,text=item,width=15).grid(row=r,column=1)
        Label(midFrame2,text=shop,width=15).grid(row=r,column=2)
        Label(midFrame2,text=quantity,width=15).grid(row=r,column=3)
        Label(midFrame2,text=total,width=15).grid(row=r,column=4)

    items=(["Shampoo","Raj Store",10,150],
        ["Milk","Desh Ki Dhaba",2,234],
        ["Orange","IconShop",1,45],
        ["Pizza","Linda Store",1,456],
        ["Drink","Apka Apna",2,345],
        ["Long Dress","Pakanti",1,474],
    )

    for x in range (len(items)):
        print(x)
        dataFound(x+1,items[x][0],items[x][1],items[x][2],items[x][3],x)


    bottomFrame=Frame(window)
    bottomFrame.pack()
    window.mainloop()
customerAfterLogin()