
import math

A = 0.00       # variable for amount to be received
repeat = False

#take user input from menu
# * while loop enable to repeat user input until user input correct option to continue the program
while repeat == False:
    print(''' investment  -  to calculate the amount of interest you'll earn on yours investment
     bond        -  to calculate the amount you'll have to pay on home loan ''')

    user_choice = input("\nEnter either 'investment or 'bond' from the menu above to proceed: ")

#confirm the valid input is entered else give error message
    valid_input = ["investment", "bond"]

    lowcase_input = user_choice.lower()
#print(lowcase_input)

    if lowcase_input not in valid_input:
        print("Please enter valid option from the menu")
    else:
        print(f"You have chosen option: {user_choice}")
        repeat = True 


#### ********if 'INVESTMENT' is chosen calculate amount they will get in retun *********
if lowcase_input == "investment":
   p = float(input("Enter the amount you want to deposit: "))
   r = float(input("Enter interest rate as a percentage: "))
   r = r / 100
   t = int(input("Enter number of years to invest your deposit: "))
   interest = input("Enter the type of interest Simple/Compound : ")
   interest = interest.lower()
   if interest not in ["simple", "compound"]:
      print("Please enter either 'Simple' or 'Compound' ")

   if interest == 'simple':                      #calculate and print ampount with simple interest 
      A = p * (1 + r * t)
      print(f"\nYou will get amount {A} in return after {t} years.")

   elif interest == 'compound':                 #calculate and print ampount with compound interest
      A = p * math.pow((1 + r), t)
      print(f"\nYou will get amount {A} in return after {t} years.")

#### *********if 'BOND' is chosen calculate the monthly repayment installment ***********
elif lowcase_input == 'bond':
    p = float(input("Enter present value of the house: "))
    r = float(input("Enter the interest rate of the loan: "))
    r = r / 100
    i = r / 12
    n = int(input("Enter number of months you plan to take to repay the bond: "))

    # formula for monthly repayment = (i * p) / (1 -(1+i)**-n)
     
    repayment = (i * p) / (1 - ( 1 + i )**(-n))

    print(f"\nYour monthly repayment for the bond will be {repayment}")
          

