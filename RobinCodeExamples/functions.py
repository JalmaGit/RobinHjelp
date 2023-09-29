
# Here we are defining the a function named "moneyThatPeopleOwnRobin" which we define to require these paramters "cash1" and "cash2" which does some calculations and then returns the "totalCash" owned.
def moneyThatPeopleOwnRobin(cash1,cash2):
    interest = 1.25
    totalCash = cash1 + cash2
    withInterest = totalCash * interest
    return withInterest

NoahOwnsCash = 100
DuckOwnCash = 50

#Here we call the "moneyThatPeopleOwnRobin"
print(moneyThatPeopleOwnRobin(NoahOwnCash,DuckOwnCash))
