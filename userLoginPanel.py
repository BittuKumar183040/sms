import tkinter as tk
from dbConnect import shopCheck
from billing import shopBilling
import variables as v

def userLoginPanel():
    user_window=tk.Tk()
    user_window.title("Show Login | Welcome")
    user_window.geometry('400x500+500+100')
    user_window.config(background=v.bgColor)
    def messageHide(edit):
        edit["background"]=v.bgColor
        edit["text"]="" # Empty Text
    def login():
        messageForeground = "#FE7E6D"
        messagebackground = "#FEECE9"
        user=entry1.get()
        password=entry2.get()
        if user=="":
            message=tk.Label(user_window,foreground=messageForeground,background=messagebackground,text="Hay! How you forgot to put username")
            message.place(relwidth=0.8, relx=0.5, rely=0.9, anchor=tk.CENTER)
            user_window.after(2000, lambda: messageHide(message))
        else:
            valu=shopCheck(user, password)
            if valu:
                user_window.destroy()
                shopBilling(user,password)
            else:
                message=tk.Label(user_window,foreground=messageForeground,background=messagebackground,text="Wrong Username or Password, %s!" %user)
                message.place(relwidth=0.8, relx=0.5, rely=0.9, anchor=tk.CENTER)
                user_window.after(2000, lambda: messageHide(message))
        
    # frameTop
    heading_Frame=tk.Frame(user_window).pack(pady=20)
    tk.Label(heading_Frame, text="Welcome to SuperMart", background=v.bgColor, foreground=v.c1, font=v.fontHeading).pack()

    # frame Middle
    mid_Frame=tk.Frame(user_window).pack(pady=0)
    tk.Label(mid_Frame,text="B I L L I N G  S Y S T E M\n\nL O G I N", width=80, height=3, font=v.fontSimple, background=v.c6, foreground="#AEFEFF").pack(pady=(10,30))

    def hand(e):
        login()
    user_window.bind('<Return>',hand)

    userBox=tk.Frame(mid_Frame)
    userBox.pack()
    entry1=tk.Entry(userBox, width=35, borderwidth=0)
    entry1.grid(row=0,column=1,pady=(20,2),padx=5)
    entry1.config({"background":v.defaultEntryColor})
    uName1=tk.Label(userBox,text="Username ",cursor="xterm",font=v.fontLittle, background=v.defaultEntryColor, foreground=v.c4)
    uName1.place(x=0.5,y=0)

    # Input box password
    passBox=tk.Frame(mid_Frame)
    passBox.pack(pady=15)
    entry2=tk.Entry(passBox, width=35, borderwidth=0)
    entry2.grid(row=0,column=1,pady=(20,2),padx=5)
    entry2.config({"background":v.defaultEntryColor})
    uPass=tk.Label(passBox,text="Password ",cursor="xterm", font=v.fontLittle, background=v.defaultEntryColor, foreground=v.c4)
    uPass.place(x=0.5,y=0)

    # Login Button
    def entered(e):
        btn["background"]="#000"
        btn["foreground"]="#fff"
    def exited(e):
        btn["foreground"]="#000"
        btn["background"]="#fff"

    btn=tk.Button(mid_Frame, text="Log In", background=v.c1 ,border=0, cursor="hand2" ,font=v.fontSimple,width=15, height=2, command=login)
    btn.bind("<Enter>", entered)
    btn.bind("<Leave>", exited)
    btn.pack(pady=10)

    forgot_link=tk.Label(mid_Frame, text="forgor password", foreground=v.linkColor, cursor="hand2", background=v.bgColor)
    forgot_link.pack()
    # ========================================

    user_window.attributes('-alpha', 0.98)
    user_window.mainloop()