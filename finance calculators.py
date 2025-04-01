# Capstone Project 1 - Varaibles and Control Structures

# Pseudocode:
# Present user with the definitions of investment and bond
# Determine whether the user want to calculate an investment or a bond

# If the user wants to calculate their investment
#   Get the user's deposit and store in variable P
#   Get the user's interest rate and store in variable r
#   Get the amount of years the user wants to invest the money and store in variable t

#   Calculate the interest rate in percentage using the equation r = r/100

#   Determine whether the user wants to use simple interest or compound interest
#   If the user wants to use simple interest
#       Calculate the simple interest using the equation  A = P(1 + r × t)
#       Print the result of A

#   If the user wants to use compound interest
#       Calculate the compound interest using the equation A = P(1 + r)^t
#       Print the result of A

#   If the user's answer does not correspond to simple or compound interest
#       Print a message to ask them to re-enter their anwer

# If the user want to calculate their bond
#   Get the present value of the user's house and store in variable P
#   Get the interest rate and store in variable i
#   Get the number of months the user will be paying their bond and store in variable n

#Calculate the annual interest rate in percentage using the equation i = (i/100)/12
  
#   Calculate the monthly payment using the equation  A = (i * P)/(1 - (1 + i)**(-n))
#   Print the result of A

# If the user's answer does not correspond to bond or investment
#   Print a message to ask them to re-enter their answer


import math

# Define investment and bond
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a homeloan.")

# Ask if the user wants to calculate an investment or a bond
user_entry = input("Enter either “investment” or “bond” from the menu above to proceed: ")

# If the user wants to calculate their investment
if user_entry.lower() == "investment":
    # Ask the user to enter the information regarding their investment and store in the appropriate variables
    P = float(input("Please enter the amount of money you are depositing: ")) #Determine the deposit amount
    r = float(input("Please enter the interest rate in percentage (%): ")) #Determine the interest rate
    t = int(input("Please enter the number of years you are planning on investing: ")) #Determine the number of years the user will be investing
    interest = input("Please enter whether you want simple or compound interest: ") #Determine whether the user wants simple or compound interest
    
    r = r/100 #Calculate interest rate

    #If the user wants to use simple interest
    if interest.lower() == "simple": 
        A = round(P * (1 + r * t), 2) #Calculate total investment for simple interest
        print(f"Your investment will be R{A} in {t} years!" ) #Return investment amount

    #If the user wants to use compound interest
    elif interest.lower() == "compound": 
        A = round( P * math.pow((1 + r),t), 2) #Calculate total investment for compound interest
        print(f"Your investment will be R{A} in {t} years!" ) #Return investment amount
    
    #If the user's answer does not correspond to simple or compound interest
    else:
        #Ask the user to re-enter their answer
        print("Your answer does not match the given options. Please rerun the code and enter if you want simple or compound interest")

# If the user wants to calculate their bond
elif user_entry.lower() == "bond":
    P = float(input("Please enter the present value of your house: ")) #Determine the present value of the user's house
    i = float(input("Please enter the interest rate in percentage (%): ")) #Determine the interest rate
    n = int(input("Please enter the number of months you plan to take to repay the bond: ")) #Determine the number of months the user will pay their bond

    i = (i/100)/12 #Calculate annual interest rate in percentage

    A = round((i * P)/(1 - (1 + i) ** (-n)),2) #Calculate monthly payments

    print(f"You will have to pay R{A} for {n} months.") #Return the monthly payments

# If the user's answer does not correspond to bond or investment
else:
    #Ask the user to re-enter their answer
    print("Your answer does not match the given options. Please rerun the program and enter if you want to calculate your investment or bond")