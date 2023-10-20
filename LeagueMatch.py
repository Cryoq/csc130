####################################################################
# author: Alan dreher
# date: October 13 2023
# description: Caculates number of Matches
####################################################################
# A function to prompt the user for the number of teams in a league. It
# does not take any arguments and returns the result to the calling
# statement.
def numOfTeams():
    return int(input("How many teams are in this league?"))
# A function that calculates the number of matches in a league. It
# receives a single numerical argument representing the number of teams
# in the league, and uses RECURSION to calculate the minimum number of
# matches required. It then returns the result to the calling statement.
total = 0
def numOfMatches(teams):
    global total
    if teams > 0:
        total +=  (teams - 1)
        teams -= 1
        return numOfMatches(teams)
    return total
# A function that prints out the final results. It receives two
# arguments that represent the number of teams and matches.
def result(teams, matches):
    print(f"A league of {teams} teams would require at lease {matches} matches")

############################ MAIN #################################
# get the number of teams
totalTeams = numOfTeams()
# calculate the number of matches
matches = numOfMatches(totalTeams)
# print the results to the screen.
result(totalTeams, matches)
#return int(.5 * teams * (teams - 1))
