# T12: Compulsory Task 1

"""
This program allows the user to access two different financial calculators:
   An investment calculator 
            and
A home loan repayment calculator
"""

# Importing math library to use the math.pow() function
import math

# Print the instructions for user
print('''
Choose either "investment" or "bond" from the menu below to proceed:

investment   =>   to calculate the amount of interest you'll earn on your investment
bond         =>   to calculate the amount you'll have to pay on a home loan
''')

# Getting user input and "clean" it to ensure it is recognised as a valid entry
user_input = input("> ").strip().casefold()

if user_input == "investment":
    # If user inputs investment, get further inputs on deposit, interest rate and time investment is made for.
    initial_deposit = float(input("\nPlease enter the amount you would like to deposit (numbers only):\n> "))
    interest_rate = float(input("Please enter the interest rate (numbers only):\n> "))
    invest_time = float(input("Please enter the number of years you plan on investing (numbers only):\n> "))

    # Get input on the type of investment (simple or compound) and "clean it up"
    interest = input('Choose either "simple" or "compound" interest:\n> ').strip().casefold()
    if interest == "simple":
        # If interest input is simple, calculate the total amount for a simple investment and print the results
        total = initial_deposit * (1 + (interest_rate / 100) * invest_time)
        print(f"""
      ----------------------------------------
         SIMPLE INVESTMENT

         Initial investment:     {initial_deposit}
         Interest rate:          {interest_rate}%
         Investment period:      {invest_time} years
         Final total amount:     {total}
      ----------------------------------------
      """)
    elif interest == "compound":
        # Else if interest input is compound, calculate the total amount for a compound investment and print the results
        total = initial_deposit * math.pow((1 + (interest_rate / 100)), invest_time)
        print(f"""
      ----------------------------------------
         COMPOUND INVESTMENT

         Initial investment:     {initial_deposit}
         Interest rate:          {interest_rate}%
         Investment period:      {invest_time} years
         Final total amount:     {round(total, 2)}
      ----------------------------------------
      """)
        print("compound interest")
    else:
        # Else (if interest input is different to simple or compound), print an error message
        print(f'\nSorry, the "{interest}" option is not recognised. \nPlease start again.\n')

elif user_input == "bond":
    # Else if user's input is bond,get further input on house value, yearly interest rate and months to repay
    house_value = float(input("\nPlease enter the present value of the house (numbers only):\n> "))
    yearly_interest_rate = float(input("Please enter the interest rate (numbers only):\n> "))
    months_to_repay = int(
        input("Please enter the number of months you plan to take to repay the bond (numbers only):\n> "))

    # Calculate monthly interest rate and repayment amount and print the results
    monthly_interest_rate = (yearly_interest_rate / 12) / 100
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-months_to_repay))
    print(f"""
      ----------------------------------------
         BOND REPAYMENT

         House value:                {house_value}
         Monthly interest rate:      {round(monthly_interest_rate, 3)}%
         Months taken to repay:      {months_to_repay} months
         Repayment amount:           {round(repayment, 2)}
      ----------------------------------------
      """)
else:
    # Else (if user's input is different to investment or bond), print an error message
    print(
        f'\nSorry, the "{user_input}" option is not recognised. \nPlease start again and choose either "investment" '
        f'or "bond".\n')
