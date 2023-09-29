
def simpleSolution():
    def printTabularWithLists(nameList,HeightList):
        print("_________________")
        print(f"| {nameList[0]} | {HeightList[0]} |")
        print(f"| {nameList[1]} | {HeightList[1]} |")
        print(f"| {nameList[2]} | {HeightList[2]} |")
        print(f"| {nameList[3]} | {HeightList[3]} |")
        print(f"| {nameList[4]} | {HeightList[4]} |")
        print("═════════════════")
    
    mountainNameList = ["Galgen", "Gliden", "StoSka", "StoSty", "SkaSto"]
    mountainHeightList = [2469, 2452, 2405, 2387, 2373]

    printTabularWithLists(mountainNameList,mountainHeightList)

def hardSolution():
        def printTabularWithLists(nameList,HeightList):
        print("_________________")
        print(f"| {nameList[0]} | {HeightList[0]} |")
        print(f"| {nameList[1]} | {HeightList[1]} |")
        print(f"| {nameList[2]} | {HeightList[2]} |")
        print(f"| {nameList[3]} | {HeightList[3]} |")
        print(f"| {nameList[4]} | {HeightList[4]} |")
        print("═════════════════")
    
    mountainNameList = ["Galgen", "Gliden", "StoSka", "StoSty", "SkaSto"]
    mountainHeightList = [2469, 2452, 2405, 2387, 2373]

    printTabularWithLists(mountainNameList,mountainHeightList)



def harderSolution():
    def printTabularWithDict(dictToPrint):
        print("_________________")
        for key in dictToPrint:
            print(f"| {key} | {dictToPrint[key]} |")
        print("═════════════════")

    mountainDict = {"Galgen" : 2469,
                    "Gliden" : 2452,
                    "StoSka" : 2405,
                    "StoSty" : 2387,
                    "SkaSto" : 2373,}

    printTabularWithDict(mountainDict)

simpleSolution()