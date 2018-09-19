def travel(x):
    print("You can travel:", x)
def tileone():
    while True:
        way = input("Direction: ")
        if way.lower() == "n":
            y = 2
            tile = tile2
            break
        else:
            print("Not a valid direction!")
    return x, y, tile
def tiletwo():
    while True:
        way = input("Direction: ")
        if way.lower() == "n":
            y = 3
            tile = tile3
            break
        elif way.lower() == "e":
            x = 2
            tile = tile5
            break
        elif way.lower() == "s":
            y = 1
            tile = tile1
            break
        else:
            print("Not a valid direction!")
    return x, y, tile
def tilethree():
    while True:
        way = input("Direction: ")
        if way.lower() == "e":
            x = 2
            tile = tile6
            break
        elif way.lower() == "s":
            y = 2
            tile = tile2
            break
        else:
            print("Not a valid direction!")
    return x, y, tile
def tilefour():
    while True:
        way = input("Direction: ")
        if way.lower() == "n":
            y = 2
            tile = tile5
            break
        else:
            print("Not a valid direction!")
    return x, y, tile
def tilefive():
    while True:
        way = input("Direction: ")
        if way.lower() == "w":
            x = 1
            tile = tile2
            break
        elif way.lower() == "s":
            y = 1
            tile = tile4
            break
        else:
            print("Not a valid direction!")
    return x, y, tile
def tilesix():
    while True:
        way = input("Direction: ")
        if way.lower() == "e":
            x = 3
            tile = tile9
            break
        elif way.lower() == "w":
            x = 1
            tile = tile3
            break
        else:
            print("Not a valid direction!")
    return x, y, tile
def tileseven():
    tile = tile7
def tileeight():
    while True:
        way = input("Direction: ")
        if way.lower() == "n":
            y = 3
            tile = tile9
            break
        elif way.lower == "s":
            y = 1
            tile = tile7
            break
        else:
            print("Not a valid direction!")
    return x, y, tile
def tilenine():
    while True:
        way = input("Direction: ")
        if way.lower() == "s":
            y = 2
            tile = tile8
            break
        elif way.lower() == "w":
            x = 2
            tile = tile6
            break
        else:
            print("Not a valid direction!")
    return x, y, tile

tile1 = "(N)orth"
tile2 = "(N)orth or (E)ast or (S)outh"
tile3 = "(E)ast or (S)outh"
tile4 = "(N)orth"
tile5 = "(S)outh or (W)est"
tile6 = "(E)ast or (W)est"
tile7 = "victory!"
tile8 = "(N)orth or (S)outh"
tile9 = "(S)outh or (W)est"
x = 1
y = 1
tile = tile1

while tile != tile7:
    if x == 1 and y == 1:
        travel(tile)
        print(tileone())
        print(x, y, tile)
    elif x == 1 and y == 2:
        travel(tile)
        tiletwo()
    elif x == 1 and y == 3:
        travel(tile)
        tilethree()
    elif x == 2 and y == 1:
        travel(tile)
        tilefour()
    elif x == 2 and y == 2:
        travel(tile)
        tilefive()
    elif x == 2 and y == 3:
        travel(tile)
        tilesix()
    elif x == 3 and y == 1:
        tileseven()
    elif x == 3 and y == 2:
        travel(tile)
        tileeight()
    elif x == 3 and y == 3:
        travel(tile)
        tilenine()