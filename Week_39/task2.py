def simpleSolution():
    def Greetings():
        userName = str(input("What is your name? "))
        print(f"Oh, Hello {userName}")

    def notationCheckerOfNumber():
        numberFromUser = float(input("Give me a number and I can tell you its properties: "))

        if (numberFromUser > 0):
            print(f"{numberFromUser} is a positive number")
        elif (numberFromUser < 0):
            print(f"{numberFromUser} is a negative number")
        else:
            print(f"{numberFromUser} is 0 as in zero")

    def doubleOfNumber():
        numberFromUser = float(input("Give me a number and I can double its value "))
        print(f"The double of {numberFromUser} is {numberFromUser*2}")

    def reverseString():
        stringFromUser = str(input("Write a sentence or word you want to reverse")) [::-1]
        print(stringFromUser)


    Greetings()
    notationCheckerOfNumber()
    doubleOfNumber()
    reverseString()

simpleSolution()