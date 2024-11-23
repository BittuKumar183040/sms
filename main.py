from tkinter import *
from admin import adminLoginPanel
from userLoginPanel import userLoginPanel
from PIL import Image, ImageTk
import time

window=Tk()
res=(1000,563)
window.geometry("%sx%s+40+10" %res)
img_copy=Image.open('./mainWall.jpg')
img_c=img_copy.resize(res, Image.ANTIALIAS)
bgImage=ImageTk.PhotoImage(img_c)
adminLogo=PhotoImage(file="./asset/store.png")
storeLogo=PhotoImage(file="./asset/loggedIcon.png")

background=Label(window,image=bgImage,bd=0)
background.place(x=0,y=0)

topFrame=LabelFrame(window)
topFrame.pack()
timeArea=Label(window,text="",fg="white",bg="black",font="Arial 25")
timeArea.place(relx = 0.5, y = 45, anchor = CENTER)
# -----------------------------
# TIME ONLINE
def clock_digital():
    timeArea["text"]=time.strftime("%H:%M:%S", time.localtime())
    window.after(1000,clock_digital)
clock_digital()
# -----------------------------
midFrame=Frame(window)
midFrame.pack(side=TOP,expand=YES)

def adminLogin():
    window.destroy()    
    adminLoginPanel()
def shopLogin():
    window.destroy()
    userLoginPanel()

adminBtn=Button(midFrame,text="Admin",width=120,height=120,border=2,image=storeLogo,compound=TOP,command=adminLogin,cursor="hand2")
adminBtn.grid(column=1,row=0)

shopBtn=Button(midFrame,text="Billing System",width=120,height=120,border=2,image=adminLogo,compound=TOP, command=shopLogin,cursor="hand2")
shopBtn.grid(column=2,row=0)

bottomFrame=Frame(window)
bottomFrame.pack()
window.minsize(400,300)
window.maxsize(res[0],res[1])
window.mainloop()