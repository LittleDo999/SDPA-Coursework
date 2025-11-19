# main.py starts

# import variables and functions
from version import *
from bouquet import *

print (f"Version = {version}")
print (f"bouquet1 = {bouquet1.name}")
print (f"Max_Revenue = {bouquet1.demand * bouquet1.price}")


print (f"Welcome to the Flower Shop Simulator Version {version}!\r")
print ("How many months would you like to run the game for?")
month = int(input())
if month <= 0:
    print ("Please enter an integer greater than 0.")
    
else:
    for month in range(month):
        print (f"\n--- Month {month+1} ---")
        print ("Before the month starts, there are some owner actions for you to carry out. First, review the number of staff, then decide how many bouquets to sell.")
        print ("How many florist would you like to hire?")
        staff = input()
        
