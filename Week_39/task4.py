
def simpleSolution():

    maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"

    selectedMonth = int(input("Write in your month as a number: "))

    selectedMonth = selectedMonth - 1

    print(maaneder[selectedMonth*3:selectedMonth*3+3:])