##########################################################################
# name: Alan Dreher
# date: October 23 2023
# description: Calculates Population growth of 2 countries
#########################################################################

# A function that prints out the introduction to the program. It doesn't
# take any arguments and does not return any results.
def intro():
    print("This program will compare the populations of two different countries over time")

# A function that prompts the user for the name of the country. It takes
# in a number that is used in the prompt as an argument. It then returns
# the name of the country.
def country(num):
    return input(f"What is the name of Country #{num}: ")

# A function that prompts the user for the current population of a
# country. It takes the name of the country as an argument, and then
# returns the resulting population. The function also carries out range
# checking to make sure the value inputed by the user is valid (i.e. not
# negative)
def population(country):
    pop = int(input(f"What is the current populations of {country}? "))
    if pop < 0:
        print("That doesn't seem right. Please enter a positive number")
        population(country)
    return pop

# A function that prompts the user for the population growth rate of a
# country. It takes in the name of the country as an argument and then
# returns a value growth rate. It also carries out range checking to
# make sure that the result is not an unrealistic growth rate i.e. rate
# should be between -5 and 10 inclusive.
def growthRate(country):
    rate = float(input(f"What is the annual population growth rate of {country}? "))
    if rate < -5.0 or rate > 10.0:
        print("That doesn't seem right. Please enter a value in the range [-5,10]")
        growthRate(country)
    return rate
        
# A function that prompts the user for the number of years to show in
# the resulting table. The function doesn't take any arguments but
# returns a result. It is also in charge of range checking to make sure
# that the number of years is not less than 1.
def years_():
    years = int(input("How many years of comparison should the table show? "))
    if years < 1:
        print("That doesn't seem right. Please enter a value >= 1")
        years_()
    return years
    
# A function that prompts the user for the duration of the interval in
# the table i.e. how many years between each successive row of the
# resulting table. It doesn't take any arguments and does range checking
# to make sure that the user doesn't enter a value less than 1.
def interval_():
    interval = int(input("How many years should the intervals be? "))
    if interval < 1:
        print("That doesnt seem right. Please enter a value >= 1")
        interval_()
    return interval

# A function that calculates the population given an intial population,
# a growth rate, and the time. It takes 3 arguments (population, growth
# rate and time) and returns the resulting population.
def calculatePopulation(p, r, t):
    pop = int(p * (1 + (r/100)) ** t)
    return '{:,}'.format(pop)

# A functiont to print out the header of the table. It takes two
# arguments i.e. the country names, and then prints out the formatting
# lines as well as the first row seen at the top of the table.
def header(country1, country2):
    for i in range(50):
        print("-", end="")
    print(f"\n Years\t    {country1}\t\t {country2}")
    for i in range(50):
        print("-", end="")
    print("")
    

# A function to pzint out the rest of the table row by row. It receives
# 6 arguments: both country populations, both country rates, the
# duration of the analysis and the interval between each row. It then
# relies on calculate population function to calculate the population
# values for each row and print them out in order.
def table(pop1, pop2, rate1, rate2, years, interval):
    currentYear = 0
    while years >= currentYear:
        print(f"{currentYear}\t {calculatePopulation(pop1, rate1, currentYear)}\t{calculatePopulation(pop2, rate2, currentYear)}")
        currentYear += interval
    for i in range(50):
        print("-", end="")
    pass

############### MAIN ##################################
# print the introduction
intro()

# Get the country names
countries = []
countries.append(country(1))
countries.append(country(2))

# Get the country initial populations
cPopulation = []
cPopulation.append(population(countries[0]))
cPopulation.append(population(countries[1]))

# get the country population growth rates
cRate = []
cRate.append(growthRate(countries[0]))
cRate.append(growthRate(countries[1]))

# get the analysis detais e.g. the duration and the interval
years = years_()
interval = interval_()

# Print out the table
header(countries[0], countries[1])
table(cPopulation[0], cPopulation[1], cRate[0], cRate[1], years, interval)
