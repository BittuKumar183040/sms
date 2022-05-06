import os
def printData(shop,list,total,customer,dis):
    f=open("createFileToPrint.txt","w+")
    f.write("------------- %s -------------\n" %(shop[0]))
    f.write("             ( %s Shop)\n"%shop[5])
    f.write("%s         -       %s\n" %(shop[3],shop[4]))
    f.write("Add.: Raisen Road, Bhopal - 462023\n")
    f.write("--------------------------------------\n")
    f.write("Name - %s           |    %s\n"%(customer[1],customer[3]))
    f.write("ID - %s\n"%customer[0])
    f.write("Bill No. - %s\n"%customer[0])
    f.write("--------------------------------------\n")
    for x in list:
        f.write("%s\t\t - \t\t %s \n" %(x[1],x[2]))
    f.write("--------------------------------------\n")
    if not(dis[0]):
        f.write(" Give Cust. ID to get Add. 2% Dis\n")
    else:
        f.write("                        Discount - %d %%\n" %dis[0])
    f.write("--------------------------------------\n")
    f.write("Total\t\t - \t\t %s \n" %total[1])
    f.write("--------------------------------------\n")
    f.write("------ Thanks You For Shopping  ------\n")

    f.close()
    # to open file
    file="createFileToPrint.txt"
    os.system(file)
    # ----------------------------
    
