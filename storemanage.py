from cProfile import label
from cgitb import text
from textwrap import fill
import tkinter as tk
import variables as v
from dbConnect import searchItemsFromTable, shopsList,checkActive,updateShop,deleteShopRow,insertShop,showShopItems,addItemsIntoShop

def storeManage():
    menuWindow=tk.Tk()

    menuWindow.geometry("%dx%d+%d+%d" %(1360-195,768-110,195,80))
    menuWindow.title("Stores Manager")

    bigFrame=tk.Label(menuWindow, background=v.c2)
    bigFrame.grid()
    menuHeading=tk.Label(bigFrame, text="Stores", font=v.fontSimple, background=v.c2)
    menuHeading.grid(row=0, column=0, sticky="W")
    subHeading=tk.Label(bigFrame, text="Alter and Change the Stores's Details", font=v.fontCaption, background=v.c2, foreground=v.c4)
    subHeading.grid(row=2, column=0, sticky="W",pady=(0,20))

    # brief Area with small boxes
    
    shopsLists=shopsList() # Request the data from dbConnect (Stores shops Detail)
    activeUser=checkActive() # stores Open Shops in Mart

    brief=tk.Frame(bigFrame,background=v.c2)
    brief.grid()
    menuName=(
    ("Total Customer",len(shopsLists),"","#ff8b8b")
    , ("Last Added",shopsLists[len(shopsLists)-1][0],shopsLists[len(shopsLists)-1][3],"#6284ff")
    , ("Currently Active",len(activeUser),"","#ff62f9")
    , ("Recent","-----","","#40ACEA")
    )
    def reloadThis():
        menuWindow.destroy()
        storeManage()
    def briefFrame(name,numbers,extras,color,col):
        brief_1frame=tk.Frame(brief,width=210, height=100, background=color, cursor="hand2")
        brief_1frame.grid(row=0, column=col, padx=(19))
        headline1=tk.Label(brief_1frame,text=name,font=v.fontCaption ,background=color,foreground=v.c1)
        headline1.place(relx=0.05, rely=0.1)
        headline_Number=tk.Label(brief_1frame,text=numbers,font=v.fontHeading ,background=color,foreground=v.c1)
        headline_Number.place(relx=0.05, rely=0.4)
        headline_Number=tk.Label(brief_1frame,text=extras,font=v.fontCaption ,background=color,foreground=v.c1)
        headline_Number.place(relx=0.05, rely=0.65)

    for x in range(len(menuName)):
        count=0
        briefFrame(menuName[x][count],menuName[x][count+1],menuName[x][count+2],menuName[x][count+3],x)
    
    #Shops List Print Area
    customerBigFrame=tk.LabelFrame(menuWindow,text="Customers")
    customerBigFrame.grid()
    # Shops Heading Data
    customerHeadingFrame=tk.Frame(customerBigFrame)
    customerHeadingFrame.pack()
    tk.Label(customerHeadingFrame,text="ID" ,bg="orange",font=v.fontSimple,width=5).grid(row=0,column=0,)
    tk.Label(customerHeadingFrame,text="Name" ,bg="orange",font=v.fontSimple,width=20).grid(row=0,column=1,)
    tk.Label(customerHeadingFrame,text="Owner." ,bg="orange",font=v.fontSimple,width=10).grid(row=0,column=2,)
    tk.Label(customerHeadingFrame,text="Contact" ,bg="orange",font=v.fontSimple,width=20).grid(row=0,column=3,)
    tk.Label(customerHeadingFrame,text="Type" ,bg="orange",font=v.fontSimple,width=15).grid(row=0,column=4,)
    tk.Label(customerHeadingFrame,text="Address" ,bg="orange",font=v.fontSimple,width=15).grid(row=0,column=5,)
    tk.Label(customerHeadingFrame,text="Status",bg="orange",font=v.fontSimple,width=10).grid(row=0,column=6,)
    tk.Label(customerHeadingFrame,text="" ,font=v.fontSimple,width=5).grid(row=0,column=7,padx=(0,5)) 
    tk.Label(customerHeadingFrame,text="" ,font=v.fontSimple,width=10).grid(row=0,column=8,)
    tk.Label(customerHeadingFrame,text="" ,font=v.fontSimple,width=10).grid(row=0,column=9,)
# customer Data
    customerContent=tk.Frame(customerBigFrame)
    customerContent.pack()
    def editData(c_data):
        changeWindow=tk.LabelFrame(menuWindow,text="%s" %("Make Changes to the Shop"))
        changeWindow.place(relx=0.777,rely=0.58)
        tk.Label(changeWindow, font=v.fontSimple,text="Name").grid(row=0,column=0,padx=2,pady=5)  #Name
        tk.Label(changeWindow, font=v.fontSimple,text="Owner").grid(row=1,column=0,padx=2,pady=5) #Owner
        tk.Label(changeWindow, font=v.fontSimple,text="Contact").grid(row=2,column=0,padx=2,pady=5) #Contact
        tk.Label(changeWindow, font=v.fontSimple,text="Address").grid(row=3,column=0,padx=2,pady=5) #Address
        tk.Label(changeWindow, font=v.fontSimple,text="Type").grid(row=4,column=0,padx=2,pady=5) #Type
        tk.Label(changeWindow, font=v.fontSimple,text="Status").grid(row=5,column=0,padx=2,pady=5) #Status
        
        name=tk.Entry(changeWindow, font=v.fontSimple) #Name
        name.grid(row=0,column=1) 
        name.insert(0,c_data[0])

        owner=tk.Entry(changeWindow, font=v.fontSimple) #Owner
        owner.grid(row=1,column=1)
        owner.insert(0,c_data[3])

        contact=tk.Entry(changeWindow, font=v.fontSimple) #Contact
        contact.grid(row=2,column=1) 
        contact.insert(0,c_data[4])

        address=tk.Entry(changeWindow, font=v.fontSimple) #address
        address.grid(row=3,column=1) 
        address.insert(0,c_data[6])

        type=tk.Entry(changeWindow, font=v.fontSimple)#Type
        type.grid(row=4,column=1) 
        type.insert(0,c_data[5])

        status=tk.Entry(changeWindow, font=v.fontSimple)#Status
        status.grid(row=5,column=1) 
        status.insert(0,c_data[7])

        tk.Button(changeWindow,text="X",relief="groove",command=changeWindow.destroy,cursor="hand2",width=4,height=1).place(relx=0.85,rely=0.87)

        def setChange():
            updatedList=name.get(),owner.get(),contact.get(),type.get(),address.get(),status.get(),c_data[1];
            updateShop(updatedList)
            reloadThis()
        tk.Button(changeWindow, font=v.fontSimple, bg="#429923",fg="#fff",text="Change",width=15,command=setChange).grid(columnspan=2,pady=(15,5))

    def delete_row(id):
        def conformDelete(id_):
            deleteShopRow("shops",id_)
            reloadThis()
        deleteWindow=tk.LabelFrame(menuWindow,text="Conform Delete !!!",background="#f00")
        deleteWindow.place(relx=0.825,rely=0.85)
        tk.Label(deleteWindow,text="Do You Really Want to Delete!!!", bg="#f00").grid(padx=15)
        tk.Label(deleteWindow,text="Customer - %s" %id,bg=v.c1,font=v.fontSimple).grid()
        tk.Button(deleteWindow,text='\u2713',bg="#962212", fg="#fff",cursor="hand2",width=20,command=lambda: conformDelete(id),).grid(pady=10)
        tk.Button(deleteWindow,text='X',relief="groove",command=deleteWindow.destroy,cursor="hand2",width=2,height=1).place(relx=0.88,rely=0.61)
    def ShopItemsMethod(id):
        def addItemToShop():
            addItemsIntoShop(id,(item_id.get(),item_name.get(),item_mrp.get()))

        def checkItems(e):
            def sendRequest():
                boxData=item_search.get()
                if boxData=="" or boxData == " " or len(boxData)>10:
                    pass
                else:
                    searchResult=searchItemsFromTable(item_search.get())
                    foundFrame=tk.Frame(shopItems,width=10)
                    foundFrame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
                    itemsFound=tk.Label(foundFrame,text="--------------")
                    itemsFound.pack()
                    print(searchResult)
                    

            menuWindow.after(10,sendRequest)
                
        shopItems=tk.LabelFrame(menuWindow,text="%s" %("-"),bg="#fff")
        shopItems.place(relx=0,rely=0.5)
        
        tk.Label(shopItems,text="Search ID",bg="#fff").grid(row=0,column=0,padx=(10,0)) 
        item_search=tk.Entry(shopItems)   #search item box at the top of itemmenu
        item_search.grid(row=0,column=1)
        item_search.bind("<Key>",checkItems)

        tk.Label(shopItems, font=v.fontSimple,text="ID").grid(row=1,column=0,padx=2,pady=5) 
        tk.Label(shopItems, font=v.fontSimple,text="Name").grid(row=1,column=1,padx=2,pady=5)
        tk.Label(shopItems, font=v.fontSimple,text="MRP").grid(row=1,column=2,padx=2,pady=5)
        tk.Button(shopItems,text="X",relief="groove",command=shopItems.destroy,cursor="hand2",width=2,height=1).place(relx=0.9,y=-17)
        data=showShopItems(123)
        for x in range(len(data)):
            count=x+2;
            tk.Label(shopItems,text=data[x][0],bg="#fff").grid(row=count,column=0)
            tk.Label(shopItems,text=data[x][1],bg="#fff").grid(row=count,column=1)
            tk.Label(shopItems,text=data[x][2],bg="#fff").grid(row=count,column=2)
        
        shopItemsChange=tk.Frame(shopItems,padx=15,pady=5)
        shopItemsChange.grid(columnspan=3,sticky=tk.E,padx=15,pady=2)
        tk.Label(shopItemsChange,text="ID   :").grid(row=1,column=0)
        item_id=tk.Entry(shopItemsChange)
        tk.Label(shopItemsChange,text="Name :").grid(row=2,column=0)
        item_name=tk.Entry(shopItemsChange)
        tk.Label(shopItemsChange,text="MRP  :").grid(row=3,column=0)
        item_mrp=tk.Entry(shopItemsChange)
        item_id.grid(row=1,column=1)
        item_name.grid(row=2,column=1)
        item_mrp.grid(row=3,column=1)
        tk.Button(shopItemsChange,text="ADD",command=addItemToShop,width=10).grid(columnspan=2,pady=5)

    def storeRowGenerator(row_no,details):
        tk.Label(customerContent,text=details[1],font=v.fontCaption,width=5).grid(row=row_no,column=0,pady=5)  #id
        tk.Label(customerContent,text=details[0],anchor="center",font=v.fontCaption,width=20).grid(row=row_no,column=1,)  #Name
        tk.Label(customerContent,text=details[3],font=v.fontCaption,width=10).grid(row=row_no,column=2,)  #Owner
        tk.Label(customerContent,text=details[4],font=v.fontCaption,width=20).grid(row=row_no,column=3,)  #eContact
        tk.Label(customerContent,text=details[5],font=v.fontCaption,width=15).grid(row=row_no,column=4,)  #Type
        tk.Label(customerContent,text=details[6],font=v.fontCaption,width=15).grid(row=row_no,column=5,)  #Address
        if details[7]:
            tk.Label(customerContent,text="ACTIVE",bg="#0f0",fg="#fff",font=v.fontCaption,width=10).grid(row=row_no,column=7,)  #Status
        else:
            tk.Label(customerContent,text="OFF",bg="#f00",fg="#fff",font=v.fontCaption,width=10).grid(row=row_no,column=7,)  #Status
        tk.Button(customerContent,text="EDIT",bg=v.bgColor,font=v.fontCaption,width=5,cursor="hand2",command=lambda: editData(details)).grid(row=row_no,column=8,padx=(0,5))  #Edit
        tk.Button(customerContent,text="DELETE",bg="#f30",fg=v.c1,font=v.fontCaption,width=10,cursor="hand2", command=lambda: delete_row(details[1])).grid(row=row_no,column=9)  #Delete
        tk.Button(customerContent,text="ITEMS",bg=v.c3,fg=v.c6,font=v.fontCaption,width=10,cursor="hand2", command=lambda: ShopItemsMethod(details[1])).grid(row=row_no,column=10)  #Delete
    for x in range(len(shopsLists)):
        storeRowGenerator(x,shopsLists[x])

    def addIntoShop():
        addShops=tk.LabelFrame(menuWindow,text="")
        addShops.place(relx=0.4,rely=0.5,width=360)

        def insertShopRequest():
            lists=shopsList()
            lastId=lists[len(lists)-1][1]
            data=(name.get(),int(lastId)+1,password.get(),owner.get(),phone.get(),type.get(),address.get(),0)
            insertShop(data)
            reloadThis()

        tk.Label(addShops, font=v.fontSimple,text="Shop's Name").grid(row=0,column=0,padx=2,pady=5)  #Name
        tk.Label(addShops, font=v.fontSimple,text="Owner's Name").grid(row=1,column=0,padx=2,pady=5) #Owner
        tk.Label(addShops, font=v.fontSimple,text="Phone No").grid(row=2,column=0,padx=2,pady=5) #phone
        tk.Label(addShops, font=v.fontSimple,text="Type").grid(row=3,column=0,padx=2,pady=5) #Type
        tk.Label(addShops, font=v.fontSimple,text="Address").grid(row=4,column=0,padx=2,pady=5) #Address
        tk.Label(addShops, font=v.fontSimple,text="Password",anchor='w').grid(row=5,column=0,padx=2,pady=5) #Password
        tk.Label(addShops, font=v.fontSimple,text="Conform Password").grid(row=6,column=0,padx=2,pady=5) #Re-password
        
        addShopBtn=tk.Button(addShops,text="ADD",cursor="hand2",width=15,command=insertShopRequest,font=v.fontSimple,fg=v.c1,bg=v.c5)
        addShopBtn.grid(row=7,column=0,padx=2,pady=5,columnspan=2) #addShop

        name=tk.Entry(addShops, font=v.fontSimple) #Name
        owner=tk.Entry(addShops, font=v.fontSimple) #Owner
        phone=tk.Entry(addShops, font=v.fontSimple) #Phone
        type=tk.Entry(addShops, font=v.fontSimple)#Type
        address=tk.Entry(addShops, font=v.fontSimple)#Address
        password=tk.Entry(addShops, font=v.fontSimple)#password
        repass=tk.Entry(addShops, font=v.fontSimple)#Conform Password

        name.grid(row=0,column=1) 
        owner.grid(row=1,column=1)
        phone.grid(row=2,column=1) 
        type.grid(row=3,column=1) 
        address.grid(row=4,column=1)
        password.grid(row=5,column=1)
        repass.grid(row=6,column=1)

        def addShopClose():
            addShops.destroy()
            addBtn['state']=tk.NORMAL

        tk.Button(addShops,text="X",width=2,relief="groove",command=addShopClose,cursor="hand2").place(relx=0.935,y=-2)
        addBtn['state']=tk.DISABLED

    addBtn=tk.Button(menuWindow,text="ADD SHOP", bg="#317",fg="#fff",command=addIntoShop,font=v.fontCaption,width=10,cursor="hand2")
    addBtn.place(relx=0.5,rely=0.95)

    menuWindow.wm_attributes('-topmost',tk.TRUE)
    menuWindow.mainloop();
storeManage()