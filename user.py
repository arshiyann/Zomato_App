def checkPresent(n):
    p = open("hotel.txt","r")
    r = p.readlines()
    p.close()
    for one in r:
        ls = one.split(",")
        if ls[1].upper() == n.upper():
            return True,ls[1]
        
def viewMenu():
    p = open("hotel.txt","r")
    hr = p.readlines()
    p.close()
    print("|ID | Hotel Name  \t| City \t\t|\t Contact |")
    for one_hotel in hr:
        ls = one_hotel.split(",")
        
        print(" ",ls[0],"\t",ls[1],"      \t",ls[2],"     \t\t",ls[3],sep="",end="")
    
        
    print("Menu Of Which Hotel? Enter ID: ",end="")
    id_hot = int(input())
    f = open("Menu.txt","r")
    r = f.readlines()
    i=1
    print("\t------------MENU----------")
    print("|No.    | Dish  \t| Hotel \t| Price \t| Rating|")
    for one_h in r:
        ls = one_h.split(",")
        if int(ls[0]) == id_hot :
            print("",i,"\t",ls[2],"      \t",ls[1],"     \t",ls[3],"\t\t",ls[4],sep="|")
            
            i+=1
   
    f.close()
    
def sDish():
    f = open("Menu.txt","r")
    r = f.readlines()
    i=1
    f.close()

    print("Enter Dish Name To Search: ",end="")
    dname = input()
    flag = False
    for one in r:
        ls = one.split(",")
        if ls[2].upper() == dname.upper():
            print("Dish is Available!")
            print("|No.|  \t|  Hotel   | \t|   Dish  | \t| Price |")
            print("|",i,"|\t|",ls[1]," | \t|",ls[2],"| \t|",ls[3])
            flag = True
            i+=1
    if flag == False:
        print("Dish Not Available!!")
    
def pOrder():
    viewMenu()
    print("Enter Dish Name Here to Order: ",end="")
    dish_N = input()
    flag = False
    f = open("Menu.txt","r")
    r = f.readlines()
    f.close()
    for oneD in r:
        ls = oneD.split(",")
        if ls[2].upper() == dish_N.upper():
            print("---> Dish",ls[2],"Ordered Successfully!!**")
            flag = True
    if flag == False:
        print("**Order Declined**")        
    
def rDish():
    viewMenu()
    print("Enter Dish Name Here to Rate: ",end="")
    dish_N = input()
    flag = False
    f = open("Menu.txt","r")
    r = f.readlines()
    f.close()

    d = open("Menu.txt","w")
    for onemenu in r:
        ls1 = onemenu.split(",")
        if ls1[2].upper() == dish_N.upper():
            print("Enter Rating: ",end ="")
            up = input()
            print("Rating Updated Successfully!!")
            ls1[4] = up + "\n"
            ls1 = ",".join(ls1)
            d.writelines(ls1)
            flag = True
            
        if ls1[2].upper() != dish_N.upper() and flag == False:
                
            ls1 = ",".join(ls1)
            d.writelines(ls1)   
            flag = False
        flag = False
    d.close() 

def vRcommd():
    print("Enter Hotel Name To See Recommendation: ",end="")
    name = input()
    flag=0
    g,hname = checkPresent(name)
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

    pass




while True:
    print("1 - View Menu")
    print("2 - Search Dish")
    print("3 - Place Order")
    print("4 - Rate Dish")
    print("5 - View Recommendation's")
    print("6 - Exit")
    print("Enter Here: ",end = "")
    ch = int(input())
    if ch == 1:
        viewMenu()
    if ch == 2:
        sDish()
    if ch == 3:
        pOrder()
    if ch == 4:
        rDish()
    if ch == 5:
        vRcommd()
    if ch == 6:
        exit(0)            