import tkinter as tk
import variables as v
from dbConnect import customerList,updateCust,deleteRow

def customerManage():
    menuWindow=tk.Tk()

    menuWindow.geometry("%dx%d+%d+%d" %(1360-195,768-80,195,80))
    menuWindow.title("Customer Manager")

    bigFrame=tk.Label(menuWindow, background=v.c2)
    bigFrame.grid()
    menuHeading=tk.Label(bigFrame, text="Customer Manage", font=v.fontSimple, background=v.c2)
    menuHeading.grid(row=0, column=0, sticky="W")
    subHeading=tk.Label(bigFrame, text="Alter and Change the customer's Details", font=v.fontCaption, background=v.c2, foreground=v.c4)
    subHeading.grid(row=2, column=0, sticky="W",pady=(0,20))

    # brief Area with small boxes
    def reloadThis():
        menuWindow.destroy()
        customerManage()
    
    customerData=customerList() # Request the data from dbConnect

    brief=tk.Frame(bigFrame,background=v.c2)
    brief.grid()
    menuName=(
    ("Total Customer",len(customerData),"","#ff8b8b")
    , ("Last Added",customerData[len(customerData)-1][1],customerData[len(customerData)-1][0],"#6284ff")
    , ("Currently Active","86855","","#ff62f9")
    , ("Recent","-----","","#40ACEA")
    )

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
    
    #customer List Print Area
    customerBigFrame=tk.LabelFrame(menuWindow,text="Customers")
    customerBigFrame.grid()
    # customer Heading Data
    customerHeadingFrame=tk.Frame(customerBigFrame)
    customerHeadingFrame.pack()
    tk.Label(customerHeadingFrame,text="ID" ,bg="orange",font=v.fontSimple,width=10).grid(row=0,column=0,)
    tk.Label(customerHeadingFrame,text="Name" ,bg="orange",font=v.fontSimple,width=20).grid(row=0,column=1,)
    tk.Label(customerHeadingFrame,text="Contact No." ,bg="orange",font=v.fontSimple,width=10).grid(row=0,column=2,)
    tk.Label(customerHeadingFrame,text="Email" ,bg="orange",font=v.fontSimple,width=25).grid(row=0,column=3,)
    tk.Label(customerHeadingFrame,text="Address" ,bg="orange",font=v.fontSimple,width=20).grid(row=0,column=4,)
    tk.Label(customerHeadingFrame,text="Pincode" ,bg="orange",font=v.fontSimple,width=10).grid(row=0,column=5,)
    tk.Label(customerHeadingFrame,text="" ,font=v.fontSimple,width=5).grid(row=0,column=6,padx=(0,5)) 
    tk.Label(customerHeadingFrame,text="" ,font=v.fontSimple,width=10).grid(row=0,column=7,)
# customer Data
    customerContent=tk.Frame(customerBigFrame)
    customerContent.pack()
    def editData(c_data):
        changeWindow=tk.LabelFrame(menuWindow,text="%s" %("Make Changes to the Customer"))
        changeWindow.place(relx=0.777,rely=0.55)
        tk.Label(changeWindow, font=v.fontSimple,text="Name").grid(row=0,column=0,padx=2,pady=5)  #Name
        tk.Label(changeWindow, font=v.fontSimple,text="Contact").grid(row=1,column=0,padx=2,pady=5) #P.No
        tk.Label(changeWindow, font=v.fontSimple,text="Email").grid(row=2,column=0,padx=2,pady=5) #Email
        tk.Label(changeWindow, font=v.fontSimple,text="Address").grid(row=3,column=0,padx=2,pady=5) #Address
        tk.Label(changeWindow, font=v.fontSimple,text="Pincode").grid(row=4,column=0,padx=2,pady=5) #pin

        name=tk.Entry(changeWindow, font=v.fontSimple) #Name
        name.grid(row=0,column=1) 
        name.insert(0,c_data[1])
        p_no=tk.Entry(changeWindow, font=v.fontSimple) #P.No
        p_no.grid(row=1,column=1)
        p_no.insert(0,c_data[3])
        email=tk.Entry(changeWindow, font=v.fontSimple) #Email
        email.grid(row=2,column=1) 
        email.insert(0,c_data[4])
        address=tk.Entry(changeWindow, font=v.fontSimple)#Address
        address.grid(row=3,column=1) 
        address.insert(0,c_data[2])
        pin=tk.Entry(changeWindow, font=v.fontSimple)#Pin
        pin.grid(row=4,column=1) 
        pin.insert(0,c_data[5])
        def setChange():
            updatedList=name.get(),p_no.get(),email.get(),address.get(),pin.get(),c_data[0];
            updateCust(updatedList)
            reloadThis()
        tk.Button(changeWindow,text="X",relief="groove",command=changeWindow.destroy,cursor="hand2",width=4,height=1).place(relx=0.85,rely=0.86)
        tk.Button(changeWindow, font=v.fontSimple, bg="#429923",fg="#fff",text="Change",width=15,command=setChange).grid(columnspan=2,pady=(15,0))

    def delete_row(id):
        def conformDelete(id_):
            deleteRow("customer",id_)
            reloadThis()
        deleteWindow=tk.LabelFrame(menuWindow,text="Conform Delete !!!",background="#f00")
        deleteWindow.place(relx=0.825,rely=0.8)
        tk.Label(deleteWindow,text="Do You Really Want to Delete!!!", bg="#f00").grid(padx=15)
        tk.Label(deleteWindow,text="Customer - %s" %id,bg=v.c1,font=v.fontSimple).grid()
        tk.Button(deleteWindow,text="DELETE",bg="#962212", fg="#fff",cursor="hand2",width=20,command=lambda: conformDelete(id),).grid(pady=(5,0))
        tk.Button(deleteWindow,text='\u274C',relief="groove",command=deleteWindow.destroy,cursor="hand2",width=2,height=1).place(relx=0.88,rely=0.61)

    def customerRowGenerator(row_no,details):
        tk.Label(customerContent,text=details[0],font=v.fontCaption,width=10).grid(row=row_no,column=0,pady=5)  #id
        tk.Label(customerContent,text=details[1],anchor="center",font=v.fontCaption,width=20).grid(row=row_no,column=1,)  #Name
        tk.Label(customerContent,text=details[3],font=v.fontCaption,width=10).grid(row=row_no,column=2,)  #P.No
        tk.Label(customerContent,text=details[4],font=v.fontCaption,width=25).grid(row=row_no,column=3,)  #email
        tk.Label(customerContent,text=details[2],font=v.fontCaption,width=20).grid(row=row_no,column=4,)  #Address
        tk.Label(customerContent,text=details[5],font=v.fontCaption,width=10).grid(row=row_no,column=5,)  #pin
        tk.Button(customerContent,text="EDIT",bg=v.bgColor,font=v.fontCaption,width=5,cursor="hand2",command=lambda: editData(details)).grid(row=row_no,column=6,padx=(0,5))  #Edit
        tk.Button(customerContent,text="DELETE",bg=v.c6,fg=v.c1,font=v.fontCaption,width=10,cursor="hand2", command=lambda: delete_row(details[0])).grid(row=row_no,column=7)  #Delete
    for x in range(len(customerData)):
        customerRowGenerator(x,customerData[x])

    menuWindow.wm_attributes('-topmost',tk.TRUE)
    menuWindow.mainloop();
# customerManage()