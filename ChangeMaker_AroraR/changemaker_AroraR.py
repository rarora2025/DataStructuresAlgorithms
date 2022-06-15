"""
Change Maker Template
Create a simple Cashier system that asks the user to enter an amount being paid 
and gives back correct change based on the initial cost, and displays the different 
denominations that were used to give back the change.
"""
import random

#Ask for users first and last name seperately.
fname =input("First Name (place quotes around answer): ")
lname = input("Last Name (place quotes around answer): ")

#Print a greeting.
print("Welcome " + fname + " " + lname)
"""
Randomly generated number for the amount to be paid.
This value is in PENNIES
DO NOT ALTER
"""
amount_to_be_paid = int(100.00 + (random.random() * (10000.00 - 100.00)))
print("Total: $" + str(amount_to_be_paid/100.00))
#Ask for users payment amount. This should be stored in a variable as dollars.
try:
    dollars = float(input("Payment amount: $")) * 100
except:
    print("Invalid, try again.")
    dollars = float(input("Payment amount: $")) * 100
while dollars < amount_to_be_paid:
    print("NOT ENOUGH, try again.")
    dollars = float(input("Payment amount: $")) * 100
change =  dollars - amount_to_be_paid

#Calculate amount of change that should tendered.
print("Your change is: $" + str(change/100))


#Calculate amount of every denomination that should be given
twenties = 0
tens = 0
fives = 0
ones = 0
twentyfivecents = 0
tencents = 0
fivecents = 0
onecents = 0

while change != 0:
    twenties = int(change / 2000) #You should just use integer division.
    change = change % 2000

    tens = int(change / 1000)
    change = change % 1000

    fives = int(change / 500)
    change = change % 500

    ones = int(change / 100)
    change = change % 100

    twentyfivecents = int(change / 25)
    change = change % 25

    tencents = int(change / 10)
    change = change % 10

    fivecents = int(change / 5)
    change = change % 5

    onecents = int(change / 1)
    change = change % 1
 


    
#Print all information in a meaningful, readable manner.
print("I paid you with:")
print("\t $20s: " + str(twenties))
print("\t $10s: " + str(tens))
print("\t $5s: " + str(fives))
print("\t $1s: " + str(ones))
print("\t Quarters: " + str(twentyfivecents))
print("\t Dimes: " + str(tencents))
print("\t Nickels: " + str(fivecents))
print("\t Pennies: " + str(onecents))

print("GOODBYE!")
