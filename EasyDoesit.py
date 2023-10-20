#############################################################################
# author: Alan Dreher
# date: September 20, 2023
# description: Gathers user's name and calculates their net income
#############################################################################

# A statement that prompts the user for their name
def name():
    name = input("Please enter your name:")
    return name

# Gets net Income of user
def netIncCalc(name):
    # Statements that prompt the user for their annual income and tax rate
    gross = float(input("Hello " + name + ", What is your gross annual income?"))
    tax = float(input("What is the percentage tax rate in your location?"))
    tax /= 100
    # Calculate the user's net income
    netIncome = gross - (gross * tax)
    return(netIncome)
    
# Gets name
user = name()

# Gets net income
usersalary = netIncCalc(user)

# Display the final output.
print("Well " + user + ", that means that your net income is $" + str(usersalary))
