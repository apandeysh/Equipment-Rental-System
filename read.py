from datetime import date
import datetime
import random
from write import billHead

def openItemsFile():
    print("Welcome to renting!! Rent our the products in massive discount !")
    print("S.N.            ItemName             \tCompany Name         \tPrice          \tQuantity")
    f = open('items.txt', 'r')
    content = f.read()
    print(content)
    f.close()

PersonelInfoList=[]
price=0
billinglist=[]
itemsDictionary=[]

def reads(a, i):
    file= open("items.txt",'r')
    itemsList=[]
    global totalPrice
    totalPrice= 0
    global Check
    Check=True
    for line in file:
        itemsList = line.strip().split(',')
        del itemsList[0]
        Quantity=int(itemsList[4])
        if Quantity>i and line==(a-1):
            Check=False
        elif Quantity<=i and line==(a-1):
            Check=True
        itemsList.pop()
        itemsDictionary.append(itemsList)
    b="\t\t"+str(i)
    itemsDictionary[a-1].append(b)
    if  Check:
        totalPrice+=(int(itemsDictionary[a-1][3])*int(itemsDictionary[a-1][4]))
        billinglist.append(itemsDictionary[a-1])
        PersonelInfoList.append(billinglist[-1])
    else:
        print("Warning!! Please enter available quantity of the items")


def chooseItemsToRent():
    StillBuy=True
    while StillBuy==True:
        try:
            InputFromUser=int(input("Enter the S.N. of item that you want to rent-"))
            if InputFromUser<6 and InputFromUser>0:
                try:
                    NumberOfItems=int(input("Enter the numbers of item that you want to rent-"))
                    reads(InputFromUser, NumberOfItems)
                    changeItemFile(InputFromUser, NumberOfItems)
                    global price
                    price+=totalPrice
                    Continue=str(input("Do you want to Continue? Type yes or no! "))
                    if Continue=="no":
                        StillBuy=False
                    
                except ValueError:
                    print("INCORRECT INPUT!! Please enter a number ")
            elif InputFromUser<0 or InputFromUser>6:
                print("Please enter correct integer!")

        except ValueError:
            print("INCORRECT INPUT!! Please enter a number")
    billing()



ToChangeFile=[]
def changeItemFile(ID, NumOfItems):
    file= open("items.txt",'r')
    for line in file:
        itemsList = line.strip().split(',')
        ToChangeFile.append(itemsList)
    ToChangeValue=int(ToChangeFile[ID-1][5])-NumOfItems
    ToChangeFile[ID-1][5]="\t\t\t"+str(ToChangeValue)
    open('items.txt', 'w').close()
    fileHandle = open("items.txt","w")
    fileHandle.write(array_to_string(ToChangeFile))
    fileHandle.close()
    ToChangeFile.clear()


def array_to_string(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0  # Assuming all rows have the same length
    
    # Iterate through the array and build the string representation
    result = ""
    for i in range(rows):
        for j in range(cols):
            result += str(arr[i][j])
            if j != 5:
                result+= "," 
        result += "\n"  # Move to the next row
    
    return result


def billing():
    name=input("Enter your name ! ")
    phoneNumber=input("Enter your phone number ! ")
    DateForRenting=date.today()
    PersonelInfoList.append(DateForRenting)
    PersonelInfoList.append(name)
    PersonelInfoList.append(phoneNumber)
    billHead()
    print("Name = " ,name)
    print("Phone Number = ", phoneNumber)
    print("Date of Renting = ", DateForRenting)
    print("\n")
    print("            ItemName             \tCompany Name      \tPrice   \tQuantity")
    print(array_to_string(billinglist))
    print("\n")
    print("Total Amount = ", price)
    print('Rent for 5 days')
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("Note: In case of return after 5 days, fine will be charged\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("\n\n")



    length = random.randint(1,1000)
    bill="Bill_ID"+str(length)+".txt"
    f = open(bill, "x")
    f.write("\n")
    f.write("\t \t \t \t \t \t \t \t \t Mero Pasal")
    f.write("\n")
    f.write("\t \t \t \t \t \t \t Budhanilkantha, Kathmandu || Phone-9803987499")
    f.write("\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("This is your Bill before returning\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Have a nice day ahead..\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Name = %s\n" % name)
    f.write("Phone Number = %s\n"% phoneNumber)
    f.write("Date of Renting = %s\n"%DateForRenting)
    f.write("\n")
    f.write("            ItemName             \tCompany Name      \tPrice   \tQuantity\n")
    f.write(array_to_string(billinglist))
    f.write("\n")
    f.write("Total Amount = %s\n"% price)
    f.write('Rent for 5 days\n')
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Note: Fine cost will be added to the grand total in case of delay\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("\n\n")


priceForReturn=0
billinglistReturn=[]
itemsDictionaryForReturn=[]
def readForReturn(a, i):
    file= open("items.txt",'r')
    itemsList=[]
    global TotalPriceForReturn
    TotalPriceForReturn= 0
    for line in file:
        itemsList = line.strip().split(',')
        del itemsList[0]
        itemsList.pop()
        itemsDictionaryForReturn.append(itemsList)
    b="\t\t"+str(i)
    itemsDictionaryForReturn[a-1].append(b)
    TotalPriceForReturn+=(int(itemsDictionaryForReturn[a-1][3])*int(itemsDictionaryForReturn[a-1][4]))
    billinglistReturn.append(itemsDictionaryForReturn[a-1])


def chooseItemsToReturn():
    StillBuy=True
    global priceForReturn
    while StillBuy==True:
        try:
            InputFromUser=int(input("Enter the S.N. of item that you want to return-"))
            if InputFromUser<6 and InputFromUser>0:
                try:
                    NumberOfItems=int(input("Enter the numbers of item that you want to return-"))
                    readForReturn(InputFromUser, NumberOfItems)
                    changeItemFileFromReturn(InputFromUser, NumberOfItems)
                    priceForReturn+=TotalPriceForReturn
                    Continue=str(input("Do you want to Continue? Type yes or no! "))
                    if Continue=="no":
                        StillBuy=False
                except ValueError:
                    print("INCORRECT INPUT!! Please enter a number ")
            elif InputFromUser<0 or InputFromUser>6:
                print("Please enter correct integer!")

        except ValueError:
            print("INCORRECT INPUT!! Please enter a number")
    billingForReturn()



ToChangeFileFromReturn=[]
def changeItemFileFromReturn(ID, NumOfItems):
    file= open("items.txt",'r')
    for line in file:
        itemsList = line.strip().split(',')
        ToChangeFileFromReturn.append(itemsList)
    ToChangeValue=int(ToChangeFileFromReturn[ID-1][5])+NumOfItems
    ToChangeFileFromReturn[ID-1][5]="\t\t\t"+str(ToChangeValue)
    open('items.txt', 'w').close()
    fileHandle = open("items.txt","w")
    fileHandle.write(array_to_string(ToChangeFileFromReturn))
    fileHandle.close()
    ToChangeFileFromReturn.clear()


def getting_Date():
    while True:
        try:
            dateString= input("Enter a date of renting and enter in YYYY-MM-DD format: ")
            year, month, day = map(int, dateString.split('-'))
            requiredDate = datetime.date(year, month, day)
            return requiredDate
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_difference(startdate, enddate):
    difference = enddate - startdate
    return difference.days

def getPrice(i):
    return i


def billingForReturn():
    name=input("Enter your name ! ")
    phoneNumber=input("Enter your phone number ! ")
    DateOfRenting=getting_Date()
    DateForReturn=date.today()
    RentedDays=get_difference(DateOfRenting, DateForReturn)
    forRentedDaysInTxt=str(RentedDays)
    fine=0
    if(int(RentedDays)>5):
        for i in range(RentedDays-5):
            fine+=5
    global finalPrice
    finalPrice=priceForReturn+fine
    billHead()
    print("Name = " ,name)
    print("Phone Number = ", phoneNumber)
    print("Date of Renting = ",DateOfRenting)
    print("Date of Return = ", DateForReturn)
    print("These items were rented for ",RentedDays," Days.")
    print("\n")
    print("            ItemName             \tCompany Name      \tPrice   \tQuantity")
    print(array_to_string(billinglistReturn))
    print("\n")
    print("Total Amount = ", finalPrice)
    print('Rent for 5 days')
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("Note: In case of return after 5 days, fine will be charged\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("\n\n")



    length = random.randint(1,1000)
    bill="Bill_ID_Return"+str(length)+".txt"
    f = open(bill, "x")
    f.write("\n")
    f.write("\t \t \t \t \t \t \t \t \t Mero Pasal")
    f.write("\n")
    f.write("\t \t \t \t \t \t \t Budhanilkantha, Kathmandu || Phone-9803987499")
    f.write("\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("This is your Bill before returning\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Have a nice day ahead..\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Name = %s\n" % name)
    f.write("Phone Number = %s\n"% phoneNumber)
    f.write("Date of Renting = %s\n"% DateOfRenting)
    f.write("Date of Return = %s\n"% DateForReturn)
    f.write("These items were rented for days %s\n"% forRentedDaysInTxt )
    f.write("\n")
    f.write("            ItemName             \tCompany Name      \tPrice   \tQuantity\n")
    f.write(array_to_string(billinglistReturn))
    f.write("\n")
    f.write("Total Amount = %s\n"% priceForReturn)
    f.write('Rent for 5 days\n')
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Note: Fine cost will be added to the grand total in case of delay\n")
    f.write("---------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("\n\n")