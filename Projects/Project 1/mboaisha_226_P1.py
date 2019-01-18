#mboaisha_226_P1.py

#-------------------------------------------------------------------------------
# Name: Mohammad H. BoaISHA.
# G#: G00901310.
# Project 1
# Lab Section 226
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: list any lecture slides, text book pages, any other (allowed)
# resources you've used.
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

# A quick ref. for the dollar currency and it's denominations
# 1 Dollar = 100 cents
# half-dollar = 50 cents
# Quarter = 25 cents
# Dime = 10 cents
# Nickel = 5 cents
# Penny = one 1 cent 

print("Welcome to the School Supplies Store!")
# Ask the user for their name and store it to the var. "name" as a string
name = input("What is your name?")

# Ask user for input, define as integer and store to var. "pencils"
pencils = int(input("How many 29-cent pencils do you want?"))

# Ask user for input, define as integer and store to var. "sheafs"
sheafs = int(input("How many 200-cent of sheafs of graph paper do you want?"))

# Ask user for input, define as integer and store to var. "scantrons"
scantrons = int(input("How many 45-cent scantrons do you want?"))

# Compute the total cost by multiplying the quanities inputted with the price in cents
# price*item
totalQuantityWithPrice = 29*pencils + 200*sheafs + 45*scantrons

# Print the total cost, first initialize the value as a string then print to concatenate
print("Total Cost:" + str(totalQuantityWithPrice) + "cents")

# Take how many cents the user supplies
paymentInCents = int(input("How many cents are you paying with? "))
# Compute the change
change = paymentInCents - totalQuantityWithPrice

# Compute the change to the dollar denominations
# Compute the change, initialize as string and print
print("Your change is " + str(change) + ":")


dollars = change // 100
change = change - (dollars * 100)
print("Dollar: " + str(dollars))

quarters = change // 25
change = change - (quarters * 25)
print("Quarter: " + str(quarters))

dimes = change // 10
change = change - (dimes * 10)
print("Dime: " + str(dimes))

nickels = change // 5
change = change - (nickels * 5)
print("Nickel: " + str(nickels))

pennies = change // 1
change = change - (pennies * 1)
print("Penny: " + str(pennies))


