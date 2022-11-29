import os
from time import sleep
print("A képernyő 4 másodperc múlva frissülni fog!")
sleep(4)
os.system('cls')

global f
f = 0


def city():
    print("Üdvözlöm a cinema city jegyfogaló oldalán! ")
    print("Melyik városba szeretne jegyet foglalni?:")
    print("1: Pécs")
    print("2: Székesfehérvár ")
    print("3: Szeged")
    place = int(input("Válassza ki a várost: "))
    if place == 1:
        center()
    elif place == 2:
        center()
    elif place == 3:
        center()
    else:
        print("Hibás választás")

def center():
    print("Melyik moziban szeretné megtekinteni? ")
    print("1: Cinema city Pécs")
    print("2: Cinema city Székesfehérvár")
    print("3: Cinema city Szeged")
    print("4: Vissza a város választóhoz!")
    a = int(input("Válassza ki a mozit: "))
    movie(a)
    return 0
def movie(cinema):
    if cinema == 1:
        t_movie()
    elif cinema == 2:
        t_movie()
    elif cinema == 3:
        t_movie()
    elif cinema == 4:
        city()
    else:
        print("Hibás választás")


def t_movie():
    global f
    f = f+ 1
    print("Melyik filmet szeretné megnézni?")
    print("1: Beugró a paradicsomba")
    print("2: Fekete párduc 2")
    print("3: Rosszul vagyok magamtól")
    print("4: Vissza a moziválasztóhoz!")
    movie = int(input("Válassza ki a filmet: "))
    if movie == 4:
        center()
        cinema()
        return 0
    if f == 1:
        cinema()

def cinema():
    print("Melyik teremben szeretné nézni a filmet?")
    print("1: VIP terem")
    print("2: 4DX terem")
    print("3: ScreenX")
    a = int(input("Válassza ki a termet: "))
    ticket = int(input("Hány jegyet szeretne vásárolni? "))
    timing(a)

def timing(a):
    time1 = {
        "1": "10.00-13.00",
        "2": "13.10-15.10",
        "3": "15.20-17.20",
        "4": "18.30-20.30"
    }
    time2 = {
        "1": "10.15-13.15",
        "2": "13.25-15.25",
        "3": "15.35-17.35",
        "4": "18.45-20.45"
    }
    time3 = {
        "1": "10.30-13.30",
        "2": "13.40-15.40",
        "3": "15.50-17.50",
        "4": "18.00-20.45"
    }
    if a == 1:
        print("Melyik időpontban szeretné megnézni?")
        print(time1)
        t = input("Válassza ki az időpontot:")
        x = time1[t]
        print("Sikeres foglalás, jó szórakozást! ")
    elif a == 2:
        print("Melyik időpontban szeretné megnézni?")
        print(time2)
        t = input("Válassza ki az időpontot:")
        x = time2[t]
        print("Sikeres foglalás, jó szórakozást!")
    elif a == 3:
        print("Melyik időpontban szeretné megnézni?")
        print(time3)
        t = input("Válassza ki az időpontot:")
        x = time3[t]
        print("Sikeres foglalás, jó szórakozást!")
    return 0

city()