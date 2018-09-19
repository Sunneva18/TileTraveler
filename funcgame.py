#1. Which implementation was easier and why?
#       To me, the first implementation was easier to write, simply because I am not familiar
#   with functions. Putting together the second implementation was hard work and I honestly
#   thought that I could not do it, but in the end I proved myself wrong.
#   The second implementation is however much easier to read.
#2. Which implementation is more readable and why?
#       The second implementation is much easier to read. It isn't as long and repetitive as the
#   first one which makes it a lot better to read. The functions have descriptive names that tell
#   what they do and such.
#3. Which problems in the first implementations were you able to solve with the latter implementation?
#       The main problem solved is that it was long, repetitive and not an easy read. The functions
#   help to make it way more readable and simple.

#https://github.com/Sunneva18/TileTraveler

def printtravel(z, t):
    if z == (1, 1):
        t = tile1
    elif z == (1, 2):
        t = tile2
    elif z == (1, 3):
        t = tile3
    elif z == (2, 1):
        t = tile4
    elif z == (2, 2):
        t = tile5
    elif z == (2, 3):
        t = tile6
    elif z == (3, 1):
        t = tile7
    elif z == (3, 2):
        t = tile8
    elif z == (3, 3):
        t = tile9
    print("You can travel:",t)
def way():
    way = input("Direction: ")
    way = way.lower()
    return way
def notvalid():
    print("Not a valid direction!")
def move(a, b, c):
    if a == "n":
        b = b
        c = c + 1
    elif a == "s":
        b = b
        c = c - 1
    elif a == "e":
        c = c
        b = b + 1
    elif a == "w":
        c = c
        b = b - 1
    return b, c
def validmove(p):
    if p == (1, 1):
        valid = "n"
    elif p == (1, 2):
        valid = "nes"
    elif p == (1, 3):
        valid = "es"
    elif p == (2, 1):
        valid = "n"
    elif p == (2, 2):
        valid = "sw"
    elif p == (2, 3):
        valid = "ew"
    elif p == (3, 2):
        valid = "ns"
    elif p == (3, 3):
        valid = "sw"
    return valid
        

x = 1
y = 1
pos = (x, y)
valid = ""

tile1 = "(N)orth."
tile2 = "(N)orth or (E)ast or (S)outh."
tile3 = "(E)ast or (S)outh."
tile4 = "(N)orth."
tile5 = "(S)outh or (W)est."
tile6 = "(E)ast or (W)est."
tile7 = "victory!"
tile8 = "(N)orth or (S)outh."
tile9 = "(S)outh or (W)est."
tile = ""

while pos != (3, 1):
    printtravel(pos, tile)
    while True:
        direction = way()
        if direction in validmove(pos):
            x, y = move(direction, x, y)
            pos = (x, y)
            break
        else:
            notvalid()
print("Victory!")