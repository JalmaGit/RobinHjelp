
def addition(tallA, tallB):
    return tallA + tallB

def subtraction(tallA, tallB):
    return tallA - tallB

def multiplication(tallA, tallB):
    return tallA * tallB

def divition(tallA, tallB):
    return tallB/tallA

tall1,tall2 = float(input("Write in your first number: ")), float(input("Write in your second number: "))

print (f"Your numbers are {tall1} and {tall2}")

additionSum = addition(tall1,tall2)
print(f"The added sum of your two numbers are {additionSum}")

subtractionSum = subtraction(tall1,tall2)
print(f"The subtracked sum of your two numbers are {subtractionSum}")

multiplicationSum = multiplication(tall1,tall2)
print(f"The multiplication sum of your two numbers are {multiplicationSum}")

divitionSum = divition(tall1,tall2)
print(f"The devided of tall1 / tall2 are {divitionSum}")









