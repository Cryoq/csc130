####################################################################
# author: Alan Dreher
# date: October 16, 2023
# description: Calculates min, max, and total costs
####################################################################\
    
# A function to print out the introduction to the program. It does not
# take any arguments or return any results.
def intro():
    print("-" * 60)
    print("\nWelcome to Cyber Groceries")
    print("-" * 60)

# A function that prompts the user for the number of items that the
# customer is buying. It does not take any arguments but it returns the
# number of items being bought to the calling statement.
def numOfItems_():
    return int(input("How many items is the customer buying? "))

# A function that creates a list of item names by repeatedly prompting
# the user for product names. It takes an argument representing the
# number of items, and returns a single list containing the product
# names.
def item_(num):
    items = []
    for i in range(num):
        customerItem = input(f"What is item number {i+1}? ")
        items.append(customerItem)
    return items

# A function that creates a list of prices by repeatedly prompting the
# user for the prices for different products. It takes the list of
# product names as a single argument, and then returns a single list
# containing the prices for each of the products.
def cost_(items):
    itemCosts = []
    for i in items:
        price = float(input(f"What is the price of {i}? "))
        itemCosts.append(price)
    return itemCosts

######################### MAIN #####################################
# In the space below, use the functions defined above to solve the
# outlined problem.
####################################################################
# print out the introduction
intro()
# Prompt the user for the appropriate information
numberOfItems = numOfItems_()
items = item_(numberOfItems)
costs = cost_(items)
# Print out items and their costs.
print("-" * 60)
print(f"Items = {items}")
print(f"Prices = {costs}")
print("-" * 60)
# Figure out what the cheapest and most expensive items are as well as
# what the total cost would be.
lowest = costs.index(min(costs))
highest = costs.index(max(costs))
total = sum(costs)

# Print out the information on cheapest, most expensive and total cost.
print(f"The cheepest item is {items[lowest]}")
print(f"The most expensive item is {items[highest]}")
print(f"The total cost is {total}")
print("-" * 60)
print("-" * 60)
