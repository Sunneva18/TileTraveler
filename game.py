"""Byrjar í reit 1,1 og færð upp valmöguleika um hvert má fara
svo er þá tjekkað hvort þú mátt fara í þitt val með if og while
Lokareitur er 3,1 og prentast þá út "Victory!
https://github.com/Sunneva18/TileTraveler"""

tile1 = "(N)orth"
tile2 = "(N)orth or (E)ast or (S)outh"
tile3 = "(E)ast or (S)outh"
tile4 = "(N)orth"
tile5 = "(S)outh or (W)est"
tile6 = "(E)ast or (W)est"
tile7 = "victory!"
tile8 = "(N)orth or (S)outh"
tile9 = "(S)outh or (W)est"
tile = tile1
x = 1
y = 1

while tile != tile7:
    if x == 1 and y == 1:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "N" or way == "n":
                y = 2
                tile = tile2
                break
            else:
                print("Not a valid direction!")

    if x == 1 and y == 2:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "N" or way == "n":
                y = 3
                tile = tile3
                break
            elif way == "E" or way == "e":
                x = 2
                tile = tile5
                break
            elif way == "S" or way == "s":
                y = 1
                tile = tile1
                break
            else:
                print("Not a valid direction!")

    if x == 1 and y == 3:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "E" or way == "e":
                x = 2
                tile = tile6
                break
            elif way == "S" or way == "s":
                y = 2
                tile = tile2
                break
            else:
                print("Not a valid direction!")

    if x == 2 and y == 1:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "n" or way == "N":
                y = 2
                tile = tile5
                break
            else:
                print("Not a valid direction!")

    if x == 2 and y == 2:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "W" or way == "w":
                x = 1
                tile = tile2
                break
            elif way == "S" or way == "s":
                y = 1
                tile = tile4
                break
            else:
                print("Not a valid direction!")

    if x == 2 and y == 3:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "E" or way == "e":
                x = 3
                tile = tile9
                break
            elif way == "W" or way == "w":
                x = 1
                tile = tile3
                break
            else:
                print("Not a valid direction!")

    if x == 3 and y == 1:
        tile = tile7

    if x == 3 and y == 2:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "N" or way == "n":
                y = 3
                tile = tile9
                break
            elif way == "S" or way == "s":
                y = 1
                tile = tile7
                break
            else:
                print("Not a valid direction!")

    if x == 3 and y == 3:
        print("You can travel:",tile)
        while True:
            way = input("Direction: ")
            if way == "S" or way == "s":
                y = 2
                tile = tile8
                break
            elif way == "W" or way == "w":
                x = 2
                tile = tile6
                break
            else:
                print("Not a valid direction!")
print("Victory!")