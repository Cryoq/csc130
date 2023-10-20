####################################################################
# name:Alan Dreher
# date: September 27, 2023
# description: Calculates annual compound interest
####################################################################
class income:
    def __init__(self, principle = 0, annualRate = 0, years = 0):
        self.name = input("Please enter your name: ")
        self.principle = principle
        self.annualRate = annualRate
        self.years = years
        
    def data(self):
        self.principle = float(input("Please enter the principle: "))
        self.annualRate = float(input("Plase enter the annual percentage rate: "))
        self.years = int(input("Please enter the number of years: "))
        
    def calculateFinalAmmount(self):
        self.compoundInterest = self.principle * ((1 + (self.annualRate / 100)) ** self.years)
        print(f"Hello {self.name}, the final amount after {self.years} years at {self.annualRate}% is ${self.compoundInterest}")
    
        

user = income()
user.data()
user.calculateFinalAmmount()

