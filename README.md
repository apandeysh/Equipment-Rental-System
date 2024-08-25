# Equipment-Rental-System
# Introduction
In this project, a system was made to keep record of rent and return in an Event Equipment Rental Shop. The shop has equipment with its brand, price to rent and quantity. The rent is for 5 days and if the customer fails to return it fine must be paid upon a per-day basis.
The system has basically 2 tasks. One to record the renting and another to record the returning. The information like the name of the equipment, its brand, price, and quantity available in the store is recorded in .txt file. As a record is made in the system the .txt file also updates its record. 
At first the system shows the welcome message with its store’s name, address, and phone number. Then the user is asked the task they want to do (rent or return or exit). When the user chooses to rent, they are asked the equipment they want to rent and its quantity. Then their name and phone number for printing the bill. Then the bill is printed as well as .txt file is created as a bill. In returning, the process is similar. Firstly, the user is asked with the equipment that they want to return and their personal information like name and phone number along with the date they rent those items. Then, the bill is printed with all details including the fine if they fail to return within 5 days. Along with that, a .txt file is also created as bill which can be printed. 
# Goal
Develop programs for a system that manages equipment rentals and returns, generate bills/invoice, and maintain accurate records for stocks for an Event Equipment Rental Shop.
# Objectives
-To create a system that records the accurate records of the stocks (Equipment)
-To generate invoice/bill with name, phone number, shop details, products details, etc and create .txt file to save it 
-To calculate the total price automatically and add fine if necessary 

#Algorithm
Step 1: Start
Step 2: Print Welcome Message
Step 3: Input for Rent, Return or Exit
Step 4: If Input=Rent go to Step5, else if Input=Return go to Step 11 else if Input=Exit go to Step 19 (STOP)
Step 5: Print the items list
Step 6: Input of values of equipment and quantity user wants to rent
Step 7: Input to Continue or not?
Step 8: If input=yes then go to step 6 else if input =no go to step 9
Step 9: Input name and phone number of the user
Step 10: Print the bill/invoice with name, phone number, date, items list and total cost. Create .txt file for bill and go to step 3
Step 11: Print the items list
Step 12: Input of item and quantity users want to return
Step 13: Input to continue or not
Step 14: If Input=yes go to Step 12 else if Input = no go to Step 15
Step 15:  Input name and phone number of the user
Step 16: Input the Date of Rent
Step 17: Calculate the days it took to return and calculate the charge
Step 18: Print the bill/invoice with name, phone number, date of rent, date of return, items list and total cost. Create .txt file for bill and go to step 3
Step 19: STOP

# Conclusion
A system for an Event Equipment Rental shop has been successfully created. This system is used to make Invoice/bills and update the data in the items list. The user can enter the things to rent or return and automatically get the total amount with bill printed as well as the file of the items list is automatically updated. 
The development process was hard at first but slowly the concepts were cleared with the help of teachers and internet. The project was a success at last.
I have learnt many things including the array, list, creating text file, deleting text file, changing the text file, and many more things related to python. I have also used libraries such as Datetime and random for finding the date and random numbers. I also learnt about the report writing skills and making flowchart which is an important skill in every field of IT. At last, I also learned about testing the program and debugging it. 
There are thousands of limitation of the project implementation but to name few it is mostly UI, data collection and Bill printing. UI of this system is not that great because it is opened in shell and not an actual GUI. Data collection is poorly managed in this project because the data is saved in text file rather than in some database like SQL which would be more efficient to store the data and its management. Bill is also not printed which is required because the customer expect to have a bill.
The solution to the problem is to update the program and add more function like UI, SQL for data management and bill printing program. Firstly, a UI should be created for this project. It can be created using the Swing Java or any other alternatives. Then SQL should be used for its data base management system. And program should be added for it to automatically print the hard copy of the bill generated. 
