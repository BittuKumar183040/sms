import tkinter as tk
import variables as v

def dashBoard():
    menuWindow=tk.Tk()
    menuWindow.geometry("%dx%d+%d+%d" %(1360-195,768-80,195,80))
    menuWindow.title("DashBoard | SBSOFT")
    bigFrame=tk.Label(menuWindow, background=v.c2)
    bigFrame.grid()
    menuHeading=tk.Label(bigFrame, text="Dashboard", font=v.fontSimple, background=v.c2)
    menuHeading.grid(row=0, column=0, sticky="W")
    subHeading=tk.Label(bigFrame, text="Welcome to Supermart", font=v.fontCaption, background=v.c2, foreground=v.c4)
    subHeading.grid(row=2, column=0, sticky="W")

    # brief Area with small boxes
    brief=tk.Frame(bigFrame, width=150, background=v.c2)
    brief.grid()
    menuName=(
    ("Customers","3253","#ff8b8b")
    , ("Today Purchases","8005","#6284ff")
    , ("Payment Received","Rs. 86855","#ff62f9")
    , ("Recent","94885","#40ACEA")
    )

    def briefFrame(name,numbers,color,col):
        brief_1frame=tk.Frame(brief,width=211, height=100, background=color, cursor="hand2")
        brief_1frame.grid(row=0, column=col, padx=(0,50))
        headline1=tk.Label(brief_1frame,text=name,font=v.fontCaption ,background=color,foreground=v.c1)
        headline1.place(relx=0.05, rely=0.1)
        headline_Number=tk.Label(brief_1frame,text=numbers,font=v.fontHeading ,background=color,foreground=v.c1)
        headline_Number.place(relx=0.05, rely=0.4)

    for x in range(len(menuName)):
        count=0
        briefFrame(menuName[x][count],menuName[x][count+1],menuName[x][count+2],x)
    menuWindow.wm_attributes('-topmost',tk.TRUE)
    menuWindow.mainloop()
