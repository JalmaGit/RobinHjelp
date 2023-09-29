import math

def calculateCircuitLength(radius, lengthOfStraight):
    return round(2 * math.pi * radius + lengthOfStraight * 2, 2)

def convertKmhToMS(speedInKmh):
    return round(speedInKmh/3.6, 2)

def calculateTimeOnTenNumberOfRounds(speedInMs,lengthOfCircuit):
    return round((lengthOfCircuit / speedInMs) * 10, 2) 

def simpleSolution():
    lengthOfStraight = 100 #meter
    radius = 31.83 #meter
    averageSpeed = 50 #km/h
    
    print(f"The length of the Circuit is {calculateCircuitLength(radius,lengthOfStraight)}")
    
    print(f"The average speed converted from km/h to m/s is {convertKmhToMS(averageSpeed)}")

    print(f"IT took Anne {calculateTimeOnTenNumberOfRounds(convertKmhToMS(averageSpeed),calculateCircuitLength(radius,lengthOfStraight))} seconds to complete 10 rounds")

simpleSolution()\

