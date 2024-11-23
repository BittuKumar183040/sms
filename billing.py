from print import printData
import tkinter as tk
import variables as v
import dbConnect as Db
import time

def shopBilling(id,password):
    cursor=Db.db.cursor()
    cursor.execute("SELECT * FROM shops WHERE id = '%s' and password='%s';" %(id,password))
    data=cursor.fetchall()[0]
    shop_name=data[0]
    # owner=data[3]
    # phone_no=data[4]
    # type=data[5]
    
    window=tk.Tk()
    window.geometry("880x600+100+20")
    window.title(shop_name)
    options_list = ["All Customer", "Employee", "Subscribed"]
    entryWidth=25

    discount=[0,0]              #Additional Discount in % Section (ID, above '1000')
    totalSection=[0,0]          # items, total price,
    listItems=[]                #Holds items Added in List
    billNo=time.strftime("%d%m%y%H%M%S", time.localtime())

    mainTopFrame=tk.LabelFrame(window, text="")
    mainTopFrame.pack()

    # bill details
    billFrame=tk.Frame(mainTopFrame)
    billFrame.grid(row=0,column=0)

    billLeft=tk.Frame(billFrame)
    
    l1=tk.Label(billLeft,text="Bill No")
    e1=tk.Label(billLeft,text=billNo, anchor='w',bg="white",font="13")
    l2=tk.Label(billLeft,text="Bill Date")
    e2=tk.Label(billLeft,text=time.strftime("%A, %d %b %Y", time.localtime()), anchor='w',bg="white",font=v.fontCaption)
    l1.grid(row=0,column=0, sticky=tk.W)
    e1.grid(row=0,column=1,pady=10,padx=(20,0))
    l2.grid(row=1,column=0, sticky=tk.W)
    e2.grid(row=1,column=1,padx=(20,0))

    billRight=tk.Frame(billFrame)
    billLeft.grid(row=0,column=0, padx=20, pady=20)
    billRight.grid(row=0,column=1, padx=(0,20))

    l3=tk.Label(billRight,text="Customer")
    value_inside = tk.StringVar(billRight)
    value_inside.set(options_list[0])
    e3 = tk.OptionMenu(billRight, value_inside, *options_list)
    l4=tk.Label(billRight,text="Address")
    e4=tk.Label(billRight,text="PATNA",anchor='w',bg='white')
    l3.grid(row=0,column=0,sticky=tk.W)
    e3.grid(row=0,column=1, pady=10,sticky=tk.E)
    l4.grid(row=1,column=0, sticky=tk.W)
    e4.grid(row=1,column=1, sticky=tk.E)

    # entry Config
    e1.config(width=entryWidth)
    e2.config(width=entryWidth)
    e3.config(width=entryWidth-7)
    e3["border"]=1
    e4.config(width=entryWidth)

    # hardware Support
    billFrame=tk.LabelFrame(mainTopFrame, text="Barcode Entry")
    billFrame.grid(row=0,column=1, sticky=tk.N)

    barcodeValue=tk.Entry(billFrame, width=40)
    barcodeValue.pack(padx=5, pady=10)

    #product Information
    enterItem=[""]                                  #value taken by entrybox
    searchedData = ["","",""]                       #[0]ItemNo,itemName,itemMRP

    def addToList():
        if enterItem[0]=='' or searchedData[0]=='':
            pass
        else:
            itemAdded(searchedData[0],searchedData[1],searchedData[2])
            listItems.append([searchedData[0],searchedData[1],searchedData[2]])
            totalSection[1]=searchedData[2]+totalSection[1]
            total()
            searchedData[0]=searchedData[1]=searchedData[2]=""
            itemNo_Entry.delete(0,"end")
            enterItem[0]=''
    def searchItem(e):
        if e.char=="\x08":
            enterItem[0]=enterItem[0][:-1]
        elif e.char=="\r":
            addToList()
        else:
            enterItem[0]=enterItem[0]+e.char

        if Db.item_search(enterItem[0],"shop_123"):
            a=Db.item_search(enterItem[0],"shop_123")
            searchedData[0]=a[0]
            searchedData[1]=a[1]
            searchedData[2]=a[2]
            itemName_Entry['text']=searchedData[1]
            itemPrice_Entry['text']=searchedData[2]
        else:
            itemName_Entry['text']=""
            itemPrice_Entry['text']=""

    itemFrame=tk.LabelFrame(mainTopFrame, text="Product")
    itemFrame.grid(row=1,column=0,sticky=tk.N)
    
    itemNo_Label=tk.Label(itemFrame, text="ID")
    itemNo_Entry=tk.Entry(itemFrame)
    itemNo_Entry.bind("<Key>",searchItem)

    itemName=tk.Label(itemFrame, text="Name")
    itemName_Entry=tk.Label(itemFrame,text="",anchor='w',width=15,bg="white",fg="gray")
    itemNo_Entry.config(width=15)

    itemPrice=tk.Label(itemFrame, text="Price (pic/kg)")
    itemPrice_Entry=tk.Label(itemFrame,anchor='w',text="",width=10,bg="white",fg="gray")

    addButton=tk.Button(itemFrame,text="ADD", bg=v.c4, fg=v.c1,command=addToList ,width=12, font=v.fontCaption, cursor="hand2")

    itemNo_Label.grid(row=0,column=0)
    itemNo_Entry.grid(row=0,column=1,padx=3)
    itemName.grid(row=0,column=2,padx=(10,0))
    itemName_Entry.grid(row=0,column=3,padx=3)
    itemPrice.grid(row=0,column=4,padx=(10,0))
    itemPrice_Entry.grid(row=0,column=5,padx=3)
    addButton.grid(row=0,column=6,padx=(10),pady=(0,8))
    # ------------------------------------------------------------------
    
    # Item Purchest List
    listAreaScroll=tk.LabelFrame(mainTopFrame,text="%s C A R T %s" %("-"*54,"-"*54))
    listAreaScroll.grid(row=1,column=0,pady=(60,0),sticky=tk.NS)
    s=tk.Scrollbar(listAreaScroll)
    s.pack(side=tk.RIGHT,fill=tk.Y)

    listFrame=tk.Frame(listAreaScroll)
    listFrame.pack(side=tk.LEFT,fill=tk.BOTH)

    listFrame.config(borderwidth=3)
    tk.Label(listFrame,text="S.No.", background=v.bgColor,width=10).grid(row=0,column=0)
    tk.Label(listFrame,text="Item No", background=v.bgColor,width=15).grid(row=0,column=1)
    tk.Label(listFrame,text="Item Name", background=v.bgColor, width=35).grid(row=0,column=2)
    tk.Label(listFrame,text="MRP", background=v.bgColor, width=18).grid(row=0,column=3)

    def itemAdded(no="",name="",mrp=0):
        totalSection[0]+=1 # count the items in the cart section
        tk.Label(listFrame,text=totalSection[0], background=v.c3,width=10).grid(row=totalSection[0],column=0)
        tk.Label(listFrame,text=no, background=v.c1,width=15).grid(row=totalSection[0],column=1)
        tk.Label(listFrame,text=name,anchor='w', background=v.c2, width=35).grid(row=totalSection[0],column=2)
        tk.Label(listFrame,text=mrp,anchor='e', background=v.c5,width=18).grid(row=totalSection[0],column=3)
    
    def total():
        tk.Label(totalFrame,width=5,text=totalSection[0],bg=v.c3).grid(row=0,column=0)
        tk.Label(totalFrame,width=10,bg=v.c3).grid(row=0,column=1)
        tk.Label(totalFrame,width=25,bg=v.c3).grid(row=0,column=2)
        tk.Label(totalFrame,width=10,bg=v.c3).grid(row=0,column=3)
        tk.Label(totalFrame,width=5,bg=v.c3).grid(row=0,column=4)
        tk.Label(totalFrame,width=9,bg=v.c1,text="Total").grid(row=0,column=5)
        tk.Label(totalFrame,width=12,bg=v.c6,anchor='w',text="Rs. %s"%totalSection[1],fg=v.c1, font=v.fontCaption).grid(row=0,column=6)
    # for x in range(13):
    #     itemAdded("a","sdf",35)
    listItemsFrame=tk.Frame(listFrame)
    listItemsFrame.grid(row=0,column=0, sticky=tk.NW,pady=(30,0))
    listItemsFrame.config(background="red")

    totalFrame=tk.Frame(mainTopFrame)
    totalFrame.grid(row=4,column=0)
    
    #payment
    p_modeOption=["Cash","Online"]
    
    paymentFrame=tk.LabelFrame(mainTopFrame, text="")
    paymentFrame.grid(row=1,column=1)

    p_ModeHeading=tk.Label(paymentFrame,text="GENERATE BILL", font=v.fontHeading)
    p_ModeHeading.grid(padx=43)

    payment_mode=tk.Frame(paymentFrame)
    payment_mode.grid()
    p_Mode=tk.Label(payment_mode,text="Payment Mode").grid(row=0,column=0,padx=4)
    activeOption=tk.StringVar(payment_mode)
    activeOption.set(p_modeOption[0])
    p_Options=tk.OptionMenu(payment_mode,activeOption,*p_modeOption)
    p_Options.grid(row=0,column=1,padx=(18,5),pady=2,sticky=tk.E)
    p_Options["border"]=1
    p_Options["width"]=16
    # top_next=41
    def colorChange():
        p_Id["bg"]="white"
    def key_findCustomer(e):
        findCustomer()
    def findCustomer():
        id=p_Id.get()
        if len(id)>9:
            p_name.delete(0,"end")
            p_address.delete(0,"end")
            p_contact.delete(0,"end")
            p_email.delete(0,"end")
            p_pinCode.delete(0,"end")
            if Db.customer_check(id):
                customerData=Db.customer_check(id)
                # print(Db.customer_check("2132104465"))
                p_name.insert(0,customerData[1])
                p_address.insert(0,customerData[2])
                p_contact.insert(0,customerData[3])
                p_email.insert(0,customerData[4])
                p_pinCode.insert(0,customerData[5])
                discount[0]=2
                totalSection[1]=totalSection[1]-(totalSection[1]*2/100)
            else:
                p_name.insert(0,"NULL")
                p_address.insert(0,"NULL")
                p_contact.insert(0,"NULL")
                p_email.insert(0,"NULL")
                p_pinCode.insert(0,"NULL")
                customerData=['']
        else:
            p_Id["bg"]="red"
            window.after(500, lambda: colorChange())
    
    def NotFilledwarning():
        listAreaScroll["bg"]="white"
        p_name["bg"]="white"

    def printInFile():
        c_info=(billNo,p_name.get(),p_address.get(),p_contact.get(),p_email.get(),p_pinCode.get())
        if len(listItems)==0 or len(p_name.get())==0:
            listAreaScroll["bg"]="red"
            p_name["bg"]="red"
            window.after(500,lambda: NotFilledwarning())
        else:
            printData(data,listItems,totalSection,c_info,discount)
            Db.add_cust(c_info)
            # reset()
            window.destroy()
            shopBilling(id,password)

    p_name=tk.Entry(paymentFrame,width=40)
    p_name.grid(pady=(22,0))
    tk.Label(paymentFrame,text="Name").place(relx=0.02,y=64)
    tk.Label(paymentFrame,text="*",fg="red").place(relx=0.16,y=64)

    p_address=tk.Entry(paymentFrame,width=40)
    p_address.grid(pady=(22,0))
    tk.Label(paymentFrame,text="Address").place(relx=0.02,y=105)

    p_contact=tk.Entry(paymentFrame,width=40)
    p_contact.grid(pady=(22,0))
    tk.Label(paymentFrame,text="Contact").place(relx=0.02,y=146)

    p_email=tk.Entry(paymentFrame,width=40)
    p_email.grid(pady=(22,0))
    tk.Label(paymentFrame,text="Email").place(relx=0.02,y=187)

    p_pinCode=tk.Entry(paymentFrame,width=40)
    p_pinCode.grid(pady=(22,0))
    tk.Label(paymentFrame,text="PinCode").place(relx=0.02,y=228)

    p_Id=tk.Entry(paymentFrame,width=25)
    p_Id.bind("<Return>",key_findCustomer)
    p_Id.grid(pady=(25,0),padx=(0,7),sticky=tk.NE)
    tk.Label(paymentFrame,text="Customer ID", font=v.fontCaption).place(relx=0.02,y=290)

    payment_mode=tk.Frame(paymentFrame)
    payment_mode.grid(pady=20)

    s_cust=tk.Button(payment_mode,text="Check Customer", width=25,command=findCustomer)
    s_cust.grid(row=0,columnspan=2, pady=(0,15))

    p_payLater=tk.Button(payment_mode,text="Later")
    p_payLater.grid(row=1,column=0,padx=5)
    p_payNow=tk.Button(payment_mode,text="Received", command=printInFile)
    p_payNow.grid(row=1,column=1,padx=5)
    p_payLater["width"]=p_payNow["width"]=14

    #Status Bar
    TotalCustomer=9582135787
    sales=5484123
    statusFrame=tk.LabelFrame(window, text="")
    statusFrame.pack(fill="both", side=tk.BOTTOM)

    tk.Label(statusFrame, text="Total Customers - %d  ||" %Db.count_cust("customer")).grid(row=0,column=0)
    tk.Label(statusFrame, text=" Sale Rs. %d" %sales).grid(row=0,column=1)

    window.state('zoomed')
    # window.attributes('-fullscreen', True)
    window.mainloop()