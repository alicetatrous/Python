##################################################################################
# Change.py: This is lesson #05, which continues to use math statements while    # 
#        processing input data into output information, and displaying results.  #
#        It also introduces decision structures in python, which are also known  #
#        as selection structures. Specifically, we will be using Binary Bypass   #
#        decisions, which use the python if statement, as well as false path     #
#        multiple choice decisions, which use the python elif statement.         #
# Authored by: Alice Tatrous                                                     #
# CMP131-83122: Fundamentals of Programming (Python)                             #
# FALL 2024                                                                      #
# Professor Tirrito                                                              #
# County College of Morris                                                       #
# Date Last Modified: 10/16/2024                                                 #
##################################################################################

def main():
    ### VARIABLES INITIALIZATION AREA ###
    quarters = 0.0
    dimes = 0.0
    nickles = 0.0
    pennies = 0.0
    yourMoney = 0.0
    fee = 0.0
    percentage = 0.0
    topBorder = ""
    bottomBorder = ""
    isTier1 = False
    isTier2 = False
    isTier3 = False
    isTier4 = False
    
    ### DISPLAYING OPENING PROGRAM INFORMATION ###
    
    for i in range(60):
        topBorder += "$"
        
    bottomBorder = topBorder
    
    ### WELCOME BANNER ###
    print(topBorder)
    print("@" + f"{'Welcome to the Change Counter App v. 1.0':^58}" + "@")
    print("@" + f"{'Adapted from change.py Example published in Chapter 3 of':^58}" + "@")
    print("@" + f"{'the Python Programming: An Introduction to Computer':^58}" + "@")
    print("@" + f"{'Science, by John Zelle.':^58}" + "@")
    print("@" + f"{'Typed and Edited by: Professor Tirrito & the Students of':^58}" + "@")
    print("@" + f"{'CMP131-83122 FA2024: Fundamentals of Programming (Python)':^58}" + "@")
    print("@" + f"{'Date Modified: 10/16/2024':^58}" + "@")
    print("@" + f"{' ':^58}" + "@")
    print("@" + f"{'You will be asked to enter the number of each type of':<58}" + "@")
    print("@" + f"{'coin you have in your possession, starting with quarters':<58}" + "@")
    print("@" + f"{'down through pennies. This exercise mimics how the':<58}" + "@")
    print("@" + f"{'popular CoinStar Machine would calculate how much money':<58}" + "@")
    print("@" + f"{'to give you when you dump all you change into it. There':<58}" + "@")
    print("@" + f"{'is one caveat... we will charge a fee for this service':<58}" + "@")
    print("@" + f"{'based on the amount of money we are converting.':<58}" + "@")
    print(bottomBorder)
    
    ### PAUSING FOR PHASE 1 TESTING - SMALL STAGE DESIGN ###
#main()
    
    ### COLLECTING USER DATA VIA INPUT ###
    
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickels = int(input("How many nickels do you have? "))
    pennies = int(input("How many pennies do you have? "))
    
    ### CALCULATING THE TOTAL MONEY DEPOSIT INTO THE MACHINE ###
    yourMoney = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    
    ### DETERMINING THE MULTI-TIERED FEE STATUS ###
    if yourMoney >= 100.0:
        isTier1 = True
    elif yourMoney >= 50.0:
        isTier2 = True
    elif yourMoney >= 25.0:
        isTier3 = True
    else:
        isTier4 = True
        
    ### PAUSING FOR PHASE 2 TESTING - SMALL STAGE DESIGN ###
    #print("Test Quarters: " + str(quarters))
    #print("Test Dimes: " + str(dimes))
    #print("Test Nickels: " + str(nickels))
    #print("Test Pennies: " + str(pennies))
    #print("Test yourMoney: " + str(yourMoney))
    #print("Test Tier1: " + str(isTier1))
    #print("Test Tier2: " + str(isTier2))
    #print("Test Tier3: " + str(isTier3))
    #print("Test Tier4: " + str(isTier4))
    
#main()
    
    ### DETERMINING THE FEE PERCENTAGE ###
    if isTier1:
        percentage = 0.15
        
    if isTier2:
        percentage = 0.10
        
    if isTier3:
        percentage = 0.05
    
    if isTier4:
        percentage = 0.01
    
    ### CALCULATE THE FEE AMOUNT ###
    
    fee = round(yourMoney * percentage, 2)
    
    ### PAUSING THE PROGRAM ###
    print()
    input("Press Any Key to Continue ==>")
    print()
    
    ### DISPLAYING ALL THE RESULTS ###
    print("The application has now finished sorting and counting your change...\n")
    
    print("We collected the following amount of money from you as coins ==> $" + str(yourMoney))
    print()
    
    print("We charge a fee that is a percentage of your money, based on a " + 
          "multi-tier approach. Based on the tier you align with, your fee" +
          " percentage in ==> " + str(percentage * 100) + "%\n")
    
    print("Your deducted fee ==> $" + str(round(fee, 2)))
    print()
    
    print("After our fee, we owe you ==> $" + str(yourMoney - fee))
    print()
    
    ### DISPLAYING THE CLOSING BANNER ###
    
    print(topBorder)
    print("@" + f"{'Thank you for Using the Change Counter App v. 1.0':^58}" + "@")
    print("@" + f"{'Adapted from change.py Example published in Chapter 3 of':^58}" + "@")
    print("@" + f"{'the Python Programming: An Introduction to Computer':^58}" + "@")
    print("@" + f"{'Science, by John Zelle.':^58}" + "@")
    print("@" + f"{'Typed and Edited by: Professor Tirrito & the Students of':^58}" + "@")
    print("@" + f"{'CMP131-83122 FA2024: Fundamentals of Programming (Python)':^58}" + "@")
    print("@" + f"{'Date Modified: 10/16/2024':^58}" + "@")
    print(bottomBorder)
    
    ### CALLING MAIN TO START THE PROGRAM ###
main()
    
    
    
    
    
    
        
    
   
