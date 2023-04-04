import time
#gd character goes around
#2 height and 3.6 length per jump
#Also,around 10 blocks per second
#with 5x bigger icons, that's 50 fps.
#speed is 1.5 * more than height
#here
from msvcrt import getch, kbhit
screen = []
#functions
def supersplit(string):
    lst = []
    for i in range(len(string)-1):
        lst.append(string[i])
    return lst
def levelsplit(level):
    customlevel = []
    lines = level.split("\n")
    for i in range(1,len(lines)-1):
        customlevel.append(supersplit(lines[i]))
    return customlevel
#constants
framewait = 3
befframes = 25
aftframes = 50
#yourlevel
playerx = 15 #unchangeable
playery = 25 #unchangeable
customlevel = []
yourlevel = """
                                                                                |
                                                                                |
                                                                                |
                                                                                |
                                                  ^           OOO               |
                                 ^         ^   ^OOO       ^                     |
                        O OOOOOOOOOOOOOOOOOOOOOOO O  OOOOOOOOOOO                |
                     O  O O  O  O  O  O  O  O  O  O   O  O  O  O  O      O     O|
    ^O^   ^O^     O  O  O O  O  O  O  O  O  O  O  O^^^O  O  O  O^^^^^O^^^^^^O^^O|
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
"""
#fill your level in here
customlevel = levelsplit(yourlevel)
cuslength = 80 #length of level
#level1 preset
playerx = 15
playery = 25

level1 = """
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                   O|
  ^    OOO   ^^OOOOO|
OOOOOOOOOOOOOOOOOOOO|
"""
id1 = levelsplit(level1)
length1 = 20
#end of init
while True:
    print("IDs:")
    print("ID 0: Loaded custom level")
    print("ID 1: Trial 1")
    t = input("Type the id for the level you want to play.")
    if t == "0":
        length = cuslength
        level = customlevel
        break
    if t == "1":
        length = length1
        level = id1
        break
#menu end
for i in range(10):
    listline = []
    listline2 = []
    listline3 = []
    for k in range(befframes):
        if i == 9:
            listline.append("O")
            listline.append(" ")
            listline.append("O")
            listline.append(" ")
            listline.append("O")
            listline2.append("O")
            listline2.append(" ")
            listline2.append("O")
            listline2.append(" ")
            listline2.append("O")
            listline3.append("O")
            listline3.append(" ")
            listline3.append("O")
            listline3.append(" ")
            listline3.append("O")
        else:
            listline.append(" ")
            listline2.append(" ")
            listline3.append(" ")
    for j in range(length):
        if level[i][j] == "O":
            listline.append("O")
            listline.append(" ")
            listline.append("O")
            listline.append(" ")
            listline.append("O")
            listline2.append("O")
            listline2.append(" ")
            listline2.append("O")
            listline2.append(" ")
            listline2.append("O")
            listline3.append("O")
            listline3.append(" ")
            listline3.append("O")
            listline3.append(" ")
            listline3.append("O")
        elif level[i][j] == "^":
            listline.append(" ")
            listline.append(" ")
            listline.append("^")
            listline.append(" ")
            listline.append(" ")
            listline2.append(" ")
            listline2.append("/")
            listline2.append("O")
            listline2.append("\\")
            listline2.append(" ")
            listline3.append("<")
            listline3.append("O")
            listline3.append("O")
            listline3.append("O")
            listline3.append(">")
        else:
            listline.append(" ")
            listline.append(" ")
            listline.append(" ")
            listline.append(" ")
            listline.append(" ")
            listline2.append(" ")
            listline2.append(" ")
            listline2.append(" ")
            listline2.append(" ")
            listline2.append(" ")
            listline3.append(" ")
            listline3.append(" ")
            listline3.append(" ")
            listline3.append(" ")
            listline3.append(" ")
    for k in range(aftframes):
        listline.append(" ")
        listline.append(" ")
        listline.append(" ")
        listline.append(" ")
        listline.append(" ")
        listline2.append(" ")
        listline2.append(" ")
        listline2.append(" ")
        listline2.append(" ")
        listline2.append(" ")
        listline3.append(" ")
        listline3.append(" ")
        listline3.append(" ")
        listline3.append(" ")
        listline3.append(" ")
    screen.append(listline)
    screen.append(listline2)
    screen.append(listline3)
line = ""
for j in range(100):
    line += "-"
print(line)
for i in range(30):
    line = ""
    for j in range(100):
        if (i <= (playery + 1) and (playery - 1) <= i) and (j <= (playerx + 2) and (playerx - 2) <= j):
            line += "#"
        else:
            line += screen[i][j]
    print(line)
line = ""
for j in range(100):
    line += "-"
print(line)
input()
t = time.time()
jumptimer = 0
falltimer = 0
before = False
jumpingup = False
for fr in range(length * 5 + befframes + aftframes - 50):
    hit = False
    fallingup = True
    line = ""
    for j in range(100):
        line += "-"
    print(line)
    for i in range(30):
        line = ""
        for j in range(100):
            if (i <= (playery + 1) and (playery - 1) <= i) and (j <= (playerx + 2) and (playerx - 2) <= j):
                if screen[i][j+fr] != " ":
                    hit = True
                line += "#"
            else:
                line += screen[i][j+fr]
            for krmal in range(7):
                if screen[playery + 2][playerx+krmal-3+fr] == "O":
                    fallingup = False
                    
        print(line)
    line = ""
    for j in range(100):
        line += "-"
    print(line)

    if kbhit():
        o = ord(getch())
        if (o ==  13 or o ==32) and fallingup == False:
            jumpingup = True
    if hit:
        print("oof")
        break
    if jumpingup == True:
        if jumptimer == 8:
            fallingup = True
            jumpingup = False
        else:
            if (jumptimer % 3) != 1:
                playery -= 1
            jumptimer += 1
            fallingup = False
    else:
        jumptimer = 0
    if fallingup == True:
        if (falltimer % 3) != 1:
            playery += 1
        falltimer += 1
    else:
        falltimer = 0
    time.sleep(framewait / 50)
input()

