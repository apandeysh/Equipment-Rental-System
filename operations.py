from read import *

def operations():
    #for running the program until user type exit
    runLoop=True
    while runLoop==True:
        print("Enter 1 for Rent.")
        print("Enter 2 for Return.")
        print("Enter 3 for Exit.")
        try:
            InputFromUser=int(input("Enter the option you want to continue- "))
            if InputFromUser==1:
                openItemsFile()
                chooseItemsToRent()


            elif InputFromUser==2:
                print("Welcome to returning!! I hope you liked our product !")
                openItemsFile()
                chooseItemsToReturn()

            elif InputFromUser==3:
                print("BYE BYE!! Hope you will have a great day ahead!!")
                runLoop=False

            elif not InputFromUser==1 or InputFromUser==2 or InputFromUser==3:
                print("Please enter 1, 2 or 3!! Don't enter any other integer !")

        except ValueError:
            print("Error!! Incorrect input! Please enter correct value!")