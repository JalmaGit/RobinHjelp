
def simplestSolution():
    print("__________________")
    print("| Galgen | 2469m |")
    print("| Gliden | 2452m |")
    print("| StoSka | 2405m |")
    print("| StoSty | 2387m |")
    print("| SkaSto | 2373m |")
    print("══════════════════")



#-----------------------------------------------------------------------------------
#   This solution is using two lists and printing each value
#-----------------------------------------------------------------------------------
def simpleSolution():
    def printTabularWithLists(nameList,HeightList):
        print("__________________")
        print(f"| {nameList[0]} | {HeightList[0]}m |")
        print(f"| {nameList[1]} | {HeightList[1]}m |")
        print(f"| {nameList[2]} | {HeightList[2]}m |")
        print(f"| {nameList[3]} | {HeightList[3]}m |")
        print(f"| {nameList[4]} | {HeightList[4]}m |")
        print("══════════════════")
    
    mountainNameList = ["Galgen", "Gliden", "StoSka", "StoSty", "SkaSto"]
    mountainHeightList = [2469, 2452, 2405, 2387, 2373]

    printTabularWithLists(mountainNameList,mountainHeightList)


#-----------------------------------------------------------------------------------
#   This solution is uses a 2 dimentional list and then iterating through list to print out each value
#-----------------------------------------------------------------------------------
def hardSolution():
    def printTabularWithLists(mountainList):
        print("__________________")

        for i in range (0,len(mountainList)):
            print(f"| {mountainList[i][0]} | {mountainList[i][1]}m |")
        print("══════════════════")
    
    mountainTop5List = [["Galgen",2469], ["Gliden", 2452], ["StoSka", 2405], ["StoSty", 2387], ["SkaSto", 2373]]

    printTabularWithLists(mountainTop5List)



#-----------------------------------------------------------------------------------
#   This solution utilizes something called a dictonary. It then iterates through the dictonary
#   A dictonary has a keyvalue, in this case the name of the mountain and value that is mapped to the keyvalue,
#   which is the hight of the mountain
#-----------------------------------------------------------------------------------
def harderSolution():
    def printTabularWithDict(dictToPrint):
        print("__________________")
        for key in dictToPrint:
            print(f"| {key} | {dictToPrint[key]}m |")
        print("══════════════════")

    mountainDict = {"Galgen" : 2469,
                    "Gliden" : 2452,
                    "StoSka" : 2405,
                    "StoSty" : 2387,
                    "SkaSto" : 2373,}

    printTabularWithDict(mountainDict)

#-----------------------------------------------------------------------------------
#   This solution utilizes something called a dictonary. It then iterates through that dictonary
#   A dictonary has a keyvalue with data attached to it. In our case the name of the mountain, with
#   it's height and denominator attached to it. Since the denominator is attached rahter than
#   being hard written into print(...), it makes it possible for us to change the value and denominator with
#   just some small bits of extra code. Another nice thing with dictonaries is that they make it easy for us
#   to expand with more info, like adding more mountains
#-----------------------------------------------------------------------------------
def hardestSolution():
    def printTabularWithDict(dictToPrint):
        print("__________________")
        for key in dictToPrint:
            print(f"| {key} | {dictToPrint[key][0]}{dictToPrint[key][1]} |")
        print("══════════════════")

    mountainDict = {"Galgen" : [2469,"m"],
                    "Gliden" : [2452,"m"],
                    "StoSka" : [2405,"m"],
                    "StoSty" : [2387,"m"],
                    "SkaSto" : [2373,"m"],}

    printTabularWithDict(mountainDict)

simplestSolution()