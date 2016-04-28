# test.py

class housetype:

    def __init__(self, name):
        self.name = name
        if name == "EGW":
            self.value = 285000
            self.clear = 2
            self.width = 8
            self.height = 8
        elif name == "BUN":
            self.value = 399000
            self.clear = 3
            self.width = 10
            self.height = 7.5
        elif name == "MAI":
            self.value = 610000
            self.clear = 6
            self.width = 11
            self.height = 10.5
            # total dimensions = width | height + clear

class map:
    """Map class which contains the houses"""
    houses = []
    width = 160
    height = 150

    requiredWater = 4800
    maxWaterbodies = 4

class house:
    """House class defining the properties of a single house to be placed in the map array"""
    kind = ""
    def __init__(self, kind):
        self.kind = kind
        self.properties = housetype(kind)
    free = 0
    x = 0
    y = 0

def run(arg amountHouses):
    # coordinaten voor huizen op de map 0-160 voor breedte, 0-150 voor hoogte
    # random rechtsboven coordinaat voor huis toewijzen en dan linksonder uitrekenen
    # opslaan in een array van huizen
    # nieuw huis met random weer (en dan dus controleren of die niet op zelfde plek staat)
    coordinate = random()

def reset(arg):
    # zet alle waarden weer op nul na het printen zodat je
    # opnieuw de code kan runnen

def printValues():
    # print de waardes (en visualisatie?) zodat je deze kan zien
    # maar alleen als het enigzins klopt, anders meteen reset
    # dus check of de percentages van aanwezige huizen kloppen
    if():
        print
    else:
        reset()

def random():
    # generate a random coordinate to place a house on the map
    import random

    width = random.randint(0,160)
    height = random.randint(0,150)
    coordinate = [width, height]
    print(coordinate)

    return coordinate
