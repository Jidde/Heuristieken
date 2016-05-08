# test2.py

import random
import sys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

sys.setrecursionlimit(10000)

amountHouses = int(sys.argv[1])
tarEGW = 60*amountHouses/100
tarBUN = 25*amountHouses/100
tarMAI = 15*amountHouses/100

class housetype:
    def __init__(self, name):
        self.name = name
        if name == "EGW":
            self.value = 285000
            self.clear = 4
            self.width = 16
            self.height = 16
        elif name == "BUN":
            self.value = 399000
            self.clear = 6
            self.width = 20
            self.height = 15
        elif name == "MAI":
            self.value = 610000
            self.clear = 12
            self.width = 22
            self.height = 21
        # total dimensions = width | height + clear

class map:
    """Map class which contains the houses"""
    houses = []
    width = 320
    height = 300

    requiredWater = 9600
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

def run():
    # coordinaten voor huizen op de map 0-160 voor breedte, 0-150 voor hoogte
    # random rechtsboven coordinaat voor huis toewijzen en dan linksonder uitrekenen
    # opslaan in een array van huizen
    # nieuw huis met random weer (en dan dus controleren of die niet op zelfde plek staat)
    for i in range(tarEGW):
        # newEGW = house("EGW")
        # coordinate = genrand()
        # newEGW.x = coordinate[0]
        # newEGW.y = coordinate[1]
        # map.houses.append(newEGW)
        genhouse("EGW")
    for i in range(tarBUN):
        genhouse("BUN")
    for i in range(tarMAI):
        genhouse("MAI")
    check()
    plotmap()

def check():
    housecount = 0
    for houseinmap in map.houses:
        housecount = housecount + 1
        if houseinmap.kind == "EGW":
            for i in map.houses:
                if(i.x >= houseinmap.x <= (i.x + 16)):
                    print("noooohooo")
                if(i.y >= houseinmap.y <= (i.y + 16)):
                    print("y = wrong")
        if houseinmap.kind == "BUN":
            for i in map.houses:
                if(i.x >= houseinmap.x <= (i.x + 20)):
                    print("noooohooo")
                if(i.y >= houseinmap.y <= (i.y + 15)):
                    print("y = wrong")
        if houseinmap.kind == "MAI":
            for i in map.houses:
                if(i.x >= houseinmap.x <= (i.x + 22)):
                    print("noooohooo")
                if(i.y >= houseinmap.y <= (i.y + 21)):
                    print("y = wrong")
    print(housecount)

def genhouse(type):
    def __init__(self, type):
        self.type = type
    newhouse = house(type)
    coordinate = genrand()
    newhouse.x = coordinate[0]
    newhouse.y = coordinate[1]
    map.houses.append(newhouse)

def genrand():
    # generate a random coordinate to place a house on the map
    x = random.randint(0,320)
    y = random.randint(0,300)
    coordinate = [x, y]
    # print(coordinate)
    return coordinate

def plotmap():
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect ='equal')
    for house in map.houses:
        # color = "#%06x" % random.randint(0, 0xFFFFFF)
        if house.kind == "EGW":
            newrect = matplotlib.patches.Rectangle((house.x, house.y-16), 
                house.properties.width, house.properties.height, color='blue')
        elif house.kind == "BUN":
            newrect = matplotlib.patches.Rectangle((house.x, house.y-15), 
                house.properties.width, house.properties.height, color='red')
        elif house.kind == "MAI":
            newrect = matplotlib.patches.Rectangle((house.x, house.y-21), 
                house.properties.width, house.properties.height, color='purple')
        ax.add_patch(newrect)
    plt.xlim([-10, 350])
    plt.ylim([-30, 330])
    plt.show()
    fig.savefig('map.png', dpi=240, bbox_inches='tight')

run()