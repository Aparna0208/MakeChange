# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Aparna Subramaniam
# Section:      461 
# Assignment:   Make Change
# Date:         09/06/2024

from math import*

#This program will determine which coins will be used for remaining change

#asking user how much money they paid and how much was the actual price of what was bought
paid=float(input("How much did you pay? "))
print("")
actual_cost=float(input("How much did it cost? "))
print("")
#This next line of code determines how much money should be given back to the customer
rem_change=paid-actual_cost
print(f'You received ${rem_change:.2f} in change. That is...')

#these next few lines of code will determine the type of coin using float division and modulus functions
if rem_change>.25:
    quarters=rem_change//.25
    rem_change=rem_change-(quarters*.25)
    if quarters>1:
        print(f'{quarters:.0f} quarters')
    elif quarters==1:
        print(f'{quarters:.0f} quarter')
        
if rem_change>.10:
    dimes=rem_change//.10
    rem_change=rem_change-(dimes*.10)
    if dimes>1:
        print(f'{dimes:.0f} dimes')
    elif dimes==1:
        print(f'{dimes:.0f} dime')
        
if rem_change>.05:
    nickels=rem_change//.05
    rem_change=rem_change-(nickels*.05)
    if nickels>1:
        print(f'{nickels:.0f} nickels')
    elif nickels==1:
        print(f'{nickels:.0f} nickel')
        
pennies=(round(rem_change,ndigits=3))/.01
if pennies==1.0:
    print("1 penny")
elif pennies>1:
    print(f'{pennies:.0f} pennies')

