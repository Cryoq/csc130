####################################################################
# author: Alan Dreher
# date: October 16, 2023
# description: Documents store inventory and info
####################################################################

# A function to print out the introduction to the program. It does not
# take any arguments or return any results.
def intro():
    for i in range(60):
        print('-', end="")
    print("\nWelcome to Cyber Groceries (v2)")
    for i in range(60):
        print('-', end='')
    print('')


# A function that prompts the user for the number of items that the
# store carries. It does not take any arguments but it returns the
# number of items to the calling statement.
def numOfItems_():
    return int(input("How many items does the store carry? "))

# A function that creates a list of item names by repeatedly prompting
# the user for item names. It takes an argument representing the
# number of items, and returns a single list containing the item
# names.
def item_(num):
    items = []
    for i in range(num):
        customerItem = input(f"What is item number {i+1}? ")
        items.append(customerItem)
    return items

# A function that creates a list of prices by repeatedly prompting the
# user for the prices for different items. It takes the list of
# item names as a single argument, and then returns a single list
# containing the prices for each of the items.
def cost_(items):
    itemCosts = []
    for i in items:
        price = float(input(f"What is the price of {i}? "))
        itemCosts.append(price)
    return itemCosts

# A function that creates a list that contains the number of units that
# were sold of each of the items in the store. It takes a single
# argument i.e. the list of item names, and after repeatedly asking the
# user for item amounts, returns the list of item units that were sold.
def units_(items):
    sold = []
    for i in items:
        num = int(input(f"How many units of {i} were sold today? "))
        sold.append(num)
    return sold

# A function that prints out the summary table. It takes 3 arguments
# i.e. the list containing the item names, the list containing the item
# prices, and the list containing the item amounts. It uses these 3
# arguments to create a 4 column table that contains the name, unit
# price, number of units sold, and total amount made from that unit for
# each item. It does not return any arguments.
def summary(item, prices, units):
    for i in range(60):
        print('-', end="")
    print("\nItem\t Unit Price\t Number\t Total Cost")
    for i in range(60):
        print('-', end='')
    print('')
    for i in range(len(item)):
        total = units[i] * prices[i]
        print(f"{item[i]}\t ${prices[i]}\t\t {units[i]}\t ${round(total,2)}")
    
######################### MAIN #####################################
# In the space below, use the functions defined above to solve the
# outlined problem.
###############################################s#####################

# print out the introduction
intro()

# Prompt the user for the appropriate information
numberOfItems = numOfItems_()
items = item_(numberOfItems)
costs = cost_(items)
units = units_(items)
# Print out items and their costs.
summary(items, costs, units)