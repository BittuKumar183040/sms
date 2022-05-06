import tkinter as tk
from tkinter import *
import variables as v
from dbConnect import adminLogout
# menus
from dashboard import dashBoard
from customermanage import customerManage
from storemanage import storeManage
from purchasemanager import purchaseManage
from salesmanager import salesManager
from paymentmanager import paymentManager

def admin_loginLayout(user):
    window=tk.Tk()
    window.title("SBS Dashboard, Welcome %s" %(user))
    window.geometry("1300x768+0+0")
    window.config(bg=v.c2)
    # photo Section 
    userIcon=tk.PhotoImage(file="./asset/loggedIcon.png")
    # exit=tk.PhotoImage(file="./asset/exit.png")

    logo=tk.PhotoImage(file="./asset/logo.png")
    dashboard=tk.PhotoImage(file="./asset/dashboard.png")
    customer=tk.PhotoImage(file="./asset/customer.png")
    store=tk.PhotoImage(file="./asset/store.png")
    purchase=tk.PhotoImage(file="./asset/purchase.png")
    sales=tk.PhotoImage(file="./asset/sales.png")
    payment=tk.PhotoImage(file="./asset/payment.png")
    report=tk.PhotoImage(file="./asset/report.png")
    # --------------------
    # Left Menus 
    LeftMain=tk.Frame(window, width=250, background=v.c1)
    LeftMain.pack(side=tk.LEFT, fill="y")
    Left_Main=tk.Frame(window, width=2, background=v.c4)
    Left_Main.pack(side=tk.LEFT, fill="y")
    
    def menuItems(name, pic,btnAction): #create menu Items
        menuFrame=tk.Button(LeftMain,text = name, image=pic,compound = LEFT,relief="groove", cursor="hand2",height=45,command=btnAction)
        menuFrame.pack(fill="x",side=tk.TOP)

    activeMenu=tk.Canvas(LeftMain,width=5,bd=0, relief='ridge',height=50,background=v.c5)
    activeMenu.place(x=-2,y=10)
    
    softName=tk.Frame(LeftMain,background=v.c1)
    softName.pack(fill="x")
    menuIcon=tk.Label(softName,image=logo, background=v.c1)
    menuIcon.grid(row=0,column=0, padx=(45,15), pady=10)
    menuName=tk.Label(softName,text='SBSoft', foreground=v.c6,background=v.c1, font="Mistral 25")
    menuName.grid(row=0,column=1, padx=(0,30))

    #        (MenuText, image, bacgroundColor, foregroundColor 
    menuItemsContent=(
        ('Dashboard', dashboard, dashBoard),
        ('Manage Customer', customer, customerManage),
        ('Store Manager', store, storeManage),
        ('Purchase Manager', purchase, purchaseManage),
        ('Sales Manager', sales, salesManager),
        ('Payment Manager', payment, paymentManager),
        ('Report', report, dashBoard)
    )
    for x in range(len(menuItemsContent)):
        count=0
        menuItems(menuItemsContent[x][count],menuItemsContent[x][count+1],menuItemsContent[x][count+2])

    # Nav Bar
    navBar=tk.Frame(window,height=80, background=v.c2,borderwidth=0, relief="solid")
    navBar.pack(side=tk.TOP, fill="x") 
    back=tk.Frame(window,height=2,background=v.c4)
    back.pack(side=tk.TOP, fill="x")

    def log_Out(e):
        adminLogout(user)
        window.destroy()

    loginContainer=tk.Frame(navBar, bg=v.c1, cursor="hand2")
    loginContainer.pack(side=tk.RIGHT,padx=5, pady=5)

    loginName=tk.Label(loginContainer, text=user, font=v.fontCaption, background=v.c1)
    loginName.grid(row=0, column=0, padx=(15,40))
    loginIcon=tk.Label(loginContainer, image=userIcon, background=v.c1)
    loginIcon.grid(row=0, column=1)
    loginContainer.bind('<Button>',log_Out)
    loginName.bind('<Button>',log_Out)
    loginIcon.bind('<Button>',log_Out)
    # ---------------------------------------------
    def removeMsg(area):
        area.destroy()

    def messageBox(statement,color):
        box=tk.Frame(window)
        box.place(relx=0.01,rely=0.95)
        tk.Label(box,text=statement,bg=v.c1,font=v.fontSimple,fg=color).grid()
        window.after(2000, lambda: removeMsg(box))

    messageBox("This is working","red")
    window.wm_attributes("-fullscreen", "false")
    window.state('zoomed')
    window.mainloop()
    
    
admin_loginLayout("Bittu")