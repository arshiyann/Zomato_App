def checkPresent(n):
    p = open("hotel.txt","r")
    r = p.readlines()
    p.close()
    for one in r:
        ls = one.split(",")
        if ls[1].upper() == n.upper():
            return True,ls[1],ls[0]
        
def addNewHot():
    f = open("hotel.txt","r")
    r = f.readlines()
    f.close()
    for one_hotel in r:
        ls = one_hotel.split(",")
        
    id = int(ls[0]) + 1
    id = str(id)
    f = open("hotel.txt","a")
    print("Enter Hotel Name: ",end="")
    n = input()
    print("Enter Hotel City: ",end="")
    c = input()
    print("Enter Hotel Contact: ",end="")
    hn = input()
    
    f.write(id + "," +n + "," + c + ","+ hn +"\n" )
    print("Hotel added successfully!")
    f.close()

def removeHot():
    print("Enter Hotel ID to Remove: ",end="")
    idh = input()
    f = open("hotel.txt","r")
    r = f.readlines()
    f.close()
    f = open("hotel.txt","w")
    for one_H in r:
        ls = one_H.split(",")
        
        if ls[0] == idh:
           ls = None
           print("Hotel Removed Successfully!!")
        else:
          f.write(one_H)
    f.close() 
   

def addNewDish():

    print("Enter Hotel Name To Add Dish: ",end="")
    name = input()
    g,l,hid = checkPresent(name)
    if g is True:
        f = open("Menu.txt","a")
        print("Enter Dish Name: ",end="")
        d = input()
        print("Enter Dish Price: ",end="")
        p = input()
        print("Enter Dish Rating: ",end="")
        nd = input()
        f.write(hid +","+l + ","+ d + "," + p +","+ nd +"\n")
        print("Dish Added Successfully")
    else:
        print("Hotel Not Present!!!!")
    
    
def addRecomm():
    print("Enter Hotel Name To See Recommendation: ",end="")
    name = input()
    flag=0
    g,hname,l = checkPresent(name)
    
    if g == True:
      f=open("Menu.txt","r")
      r = f.readlines()
      f.close()
      print("| Recommended Dishes Below: |")
      for one_h in r:
        ls = one_h.split(",")
        
        if int(ls[4]) > 3 and hname == ls[1]:
            print("**",ls[2],"From",ls[1],"Restaurant In Just",ls[3],"Rupees!!!!**")
            flag +=1
        
      if flag == 0:
        print("--**No Dishes To Recommend**--")  
            
def updateDish():
    print("Enter Hotel Name To Update Dish Price: ",end="")
    name = input()
    i=1
    flag = False
    g,hname,l = checkPresent(name)
    if g == True:
        f = open("Menu.txt","r")
        r = f.readlines()
        
        
        f.close()
        print(hname,"HOTEL MENU")
        for one_menu in r:
            ls = one_menu.split(",")
            
            if ls[1] == hname:
               print(i,"-",ls[2],"=",ls[3])
               
               i+=1
               
        print("Which Dish Price Do you Want to Update? : ",end="")       
        ch  = input() 
        p = r
        d = open("Menu.txt","w")
        for onemenu in p:
            ls1 = onemenu.split(",")
            if ls1[2].upper() == ch.upper():
                print("Enter Updated Price: ",end ="")
                up = input()
                print("Price Updated Successfully!!")
                ls1[2] = up
                ls1 = ",".join(ls1)
                d.writelines(ls1)
                flag = True
            
            if ls1[1].upper() != ch.upper() and flag == False:
                
                ls1 = ",".join(ls1)
                d.writelines(ls1)   
                flag = False
            flag = False
        d.close()
   
def showAll():
    f = open("hotel.txt","r")
    r = f.readlines()
    f.close()
    print("|ID | Hotel Name  \t| City \t\t|\t Contact |")
    for one_hotel in r:
        ls = one_hotel.split(",")
        
        print(" ",ls[0],"\t",ls[1],"      \t",ls[2],"     \t\t",ls[3],sep="",end="")
    

while True:
    print("|---------------------ADMIN USER------------------------|")
    print("1 - Add New Hotel")
    print("2 - Remove Hotel")
    print("3 - Add New Dish ")
    print("4 - Add Recommendations")
    print("5 - Update Dish Price")
    print("6 - Show All Hotels")
    print("7 - Exit ")
    print("Enter Here: ",end="")
    ch = int(input())
   
    if ch == 1:
        addNewHot()
    elif ch == 2:
        removeHot()
    elif ch == 3:
        addNewDish()
    elif ch == 4:
        addRecomm()
    elif ch == 5:
        updateDish()
    elif ch == 6:
        showAll()         
    elif ch == 7:
        exit(0)        
      
