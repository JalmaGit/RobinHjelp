
def findMonth(selectedMonth):

    maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"

    selectedMonth = selectedMonth - 1

    return maaneder[selectedMonth*3:selectedMonth*3+3:]

def simpleSolution():

    selectedMonth = int(input("Write in your month as a number: "))

    print(findMonth(selectedMonth))
