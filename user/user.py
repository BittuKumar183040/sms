import tkinter as tk
import sys
sys.path.append('./')
import variables as v
window=tk.Tk()
window.geometry("880x600+100+20")
window.title("Gen_Galexy Store")


options_list = ["All Customer", "Employee", "Subscribed"]
entryWidth=25
totalSection=[0,0] # items, total price,

mainTopFrame=tk.LabelFrame(window, text="")
mainTopFrame.pack()

# bill details
billFrame=tk.LabelFrame(mainTopFrame, text="Bill Details")
billFrame.grid(row=0,column=0)

billLeft=tk.Frame(billFrame)
billLeft.grid(row=0,column=0, padx=60, pady=20)
l1=tk.Label(billLeft,text="Bill No")
e1=tk.Entry(billLeft)
l2=tk.Label(billLeft,text="Bill Date")
e2=tk.Entry(billLeft)
l1.grid(row=0,column=0, sticky=tk.W)
e1.grid(row=0,column=1,pady=10)
l2.grid(row=1,column=0, sticky=tk.W)
e2.grid(row=1,column=1)

billRight=tk.Frame(billFrame)
billRight.grid(row=0,column=1, padx=(0,60))

l3=tk.Label(billRight,text="Customer")
value_inside = tk.StringVar(billRight)
value_inside.set(options_list[0])
e3 = tk.OptionMenu(billRight, value_inside, *options_list)
l4=tk.Label(billRight,text="Address")
e4=tk.Entry(billRight)
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
itemFrame=tk.LabelFrame(mainTopFrame, text="")
itemFrame.grid(row=1,column=0)

def add(e):
    print("Added")
    itemAdded("535","Prestige Presure Cooker",36)

itemNo_Label=tk.Label(itemFrame, text="Item No")
itemNo_Entry=tk.Entry(itemFrame)
itemNo_Entry.bind('<Return>',add)

itemName=tk.Label(itemFrame, text="Item Name")
itemName_Entry=tk.Entry(itemFrame)
itemName_Entry.config(state='disabled')
itemStock=tk.Label(itemFrame, text="Stock")
itemStock_Entry=tk.Entry(itemFrame)
itemStock_Entry.config(state='disabled')
itemPrice=tk.Label(itemFrame, text="Price (pic/kg)")
itemPrice_Entry=tk.Entry(itemFrame)
itemPrice_Entry.config(state='disabled')
itemNo_Label.grid(row=0,column=0)
itemNo_Entry.grid(row=0,column=1,padx=3)
itemName.grid(row=0,column=2)
itemName_Entry.grid(row=0,column=3,padx=3)
itemStock.grid(row=0,column=4)
itemStock_Entry.grid(row=0,column=5,padx=3)
itemPrice.grid(row=0,column=6)
itemPrice_Entry.grid(row=0,column=7,padx=3)

itemNo_Entry.config(width=10)
itemStock_Entry.config(width=10)
itemPrice_Entry.config(width=15)


addButton=tk.Button(mainTopFrame,text="ADD", bg=v.c4, fg=v.c1 ,width=15, font=v.fontCaption, cursor="hand2")
addButton.grid(row=2,pady=5)
addButton.bind('<Button>',add)
#Item Purchest List
listFrame=tk.LabelFrame(mainTopFrame, text="Purchased Items")
listFrame.grid(row=3,column=0,pady=(10,0))
listFrame.config(borderwidth=3)
billHeading=tk.Label(listFrame,text="S.No.", background=v.bgColor,width=5).grid(row=0,column=0)
billHeading=tk.Label(listFrame,text="Item No", background=v.bgColor,width=10).grid(row=0,column=1)
billHeading=tk.Label(listFrame,text="Item Name", background=v.bgColor, width=25).grid(row=0,column=2)
billHeading=tk.Label(listFrame,text="MRP", background=v.bgColor, width=10).grid(row=0,column=3)
billHeading=tk.Label(listFrame,text="Rate", background=v.bgColor, width=5).grid(row=0,column=4)
billHeading=tk.Label(listFrame,text="Qty", background=v.bgColor, width=9).grid(row=0,column=5)
billHeading=tk.Label(listFrame,text="Amount", background=v.bgColor, width=15).grid(row=0,column=6)


def itemAdded(no="",name="",mrp=0,rate=1,qty=1):
    totalSection[0]+=1 # count the items in the cart section
    listItemsAdded=tk.Label(listFrame,text=totalSection[0], background=v.c3,width=5).grid(row=totalSection[0],column=0)
    listItemsAdded=tk.Label(listFrame,text=no, background=v.c1,width=10).grid(row=totalSection[0],column=1)
    listItemsAdded=tk.Label(listFrame,text=name, background=v.c2, width=25).grid(row=totalSection[0],column=2)
    listItemsAdded=tk.Label(listFrame,text=mrp, background=v.c1, width=10).grid(row=totalSection[0],column=3)
    listItemsAdded=tk.Label(listFrame,text=rate, background=v.c1, width=5).grid(row=totalSection[0],column=4)
    listItemsAdded=tk.Label(listFrame,text=qty, background=v.c1, width=9).grid(row=totalSection[0],column=5)
    amount=int(mrp)*int(qty)*rate
    listItemsAdded=tk.Label(listFrame,text=amount, background=v.c5,width=15).grid(row=totalSection[0],column=6)
    totalSection[1]=totalSection[1]+amount
    
def total():
    listItemsAdded=tk.Label(totalFrame,width=5,text=totalSection[0],bg=v.c3).grid(row=0,column=0)
    listItemsAdded=tk.Label(totalFrame,width=10,bg=v.c3).grid(row=0,column=1)
    listItemsAdded=tk.Label(totalFrame,width=25,bg=v.c3).grid(row=0,column=2)
    listItemsAdded=tk.Label(totalFrame,width=10,bg=v.c3).grid(row=0,column=3)
    listItemsAdded=tk.Label(totalFrame,width=5,bg=v.c3).grid(row=0,column=4)
    listItemsAdded=tk.Label(totalFrame,width=9,bg=v.c1,text="Total").grid(row=0,column=5)
    listItemsAdded=tk.Label(totalFrame,width=12,bg=v.c6,text=totalSection[1],fg=v.c1, font=v.fontCaption).grid(row=0,column=6)

listItemsFrame=tk.Frame(listFrame)
listItemsFrame.grid(row=0,column=0, sticky=tk.NW,pady=(30,0))
listItemsFrame.config(background="red")

itemAdded("34","Washing Powder Nirma",75)
itemAdded("26sf","Ron Capra",186)
itemAdded("263","Shipa T-Shirt",86)
itemAdded("263","Shipa T-Shirt",86)
itemAdded("26sf","Ron Capra",186)
itemAdded("26sf","Ron Capra",186)
itemAdded("26sf","Ron Capra",186)
itemAdded("26sf","Ron Capra",186)
itemAdded("26sf","Ron Capra",186)
itemAdded("26sf","Extra sous",234)


totalFrame=tk.Frame(mainTopFrame)
totalFrame.grid(row=4,column=0)
total()

#payment
p_modeOption=["Cash","Online"]
paymentFrame=tk.LabelFrame(mainTopFrame, text="")
paymentFrame.grid(row=1,column=1,rowspan=3)

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
p_name=tk.Entry(paymentFrame,width=40).grid(pady=(22,0))
tk.Label(paymentFrame,text="Name").place(relx=0.02,y=64)

p_address=tk.Entry(paymentFrame,width=40).grid(pady=(22,0))
tk.Label(paymentFrame,text="Address").place(relx=0.02,y=105)

p_contact=tk.Entry(paymentFrame,width=40).grid(pady=(22,0))
tk.Label(paymentFrame,text="Contact").place(relx=0.02,y=146)

p_email=tk.Entry(paymentFrame,width=40).grid(pady=(22,0))
tk.Label(paymentFrame,text="Email").place(relx=0.02,y=187)

p_pinCode=tk.Entry(paymentFrame,width=40).grid(pady=(22,0))
tk.Label(paymentFrame,text="PinCode").place(relx=0.02,y=228)

p_desc=tk.Entry(paymentFrame,width=40).grid(pady=(22,0))
tk.Label(paymentFrame,text="Description").place(relx=0.02,y=269)

# p_actionBtn=tk.Entry(payment_mode).grid()

payment_mode=tk.Frame(paymentFrame)
payment_mode.grid(pady=20)
p_payLater=tk.Button(payment_mode,text="Pay Later")
p_payLater.grid(row=0,column=0,padx=5)
p_payNow=tk.Button(payment_mode,text="Pay")
p_payNow.grid(row=0,column=1,padx=5)
p_payLater["width"]=p_payNow["width"]=14


#Status Bar
TotalCustomer=9582135787
sales=5484123
statusFrame=tk.LabelFrame(window, text="")
statusFrame.pack(fill="both", side=tk.BOTTOM)

cust=tk.Label(statusFrame, text="Customer Visited - %d" %TotalCustomer).grid(row=0,column=0)
todaySale=tk.Label(statusFrame, text=" Sale Rs. %d" %sales).grid(row=0,column=1)


window.mainloop()