import os
from time import sleep
print("A képernyő 3 másodperc múlva frissülni fog!")
sleep(3)
os.system('cls')

global f
f = 0

def varos():
    print("Üdvözlöm a cinema city jegyfogaló oldalán! ")
    print("Melyik városba szeretne jegyet foglalni?:")
    print("1: Pécs")
    print("2: Székesfehérvár ")
    print("3: Szeged")
    hely = int(input("Válassza ki a várost: "))
    if hely == 1:
        mozivalaszto()
    elif hely == 2:
        mozivalaszto()
    elif hely == 3:
        mozivalaszto()
    else:
        print("Hibás választás")

def mozivalaszto():
    print("Melyik moziban szeretné megtekinteni? ")
    print("1: Cinema city Pécs")
    print("2: Cinema city Székesfehérvár")
    print("3: Cinema city Szeged")
    print("4: Vissza a város választóhoz!")
    a = int(input("Válassza ki a mozit: "))
    film(a)
    return 0
def film(mozi):
    if mozi == 1:
        t_film()
    elif mozi == 2:
        t_film()
    elif mozi == 3:
        t_film()
    elif mozi == 4:
        varos()
    else:
        print("Hibás választás")


def t_film():
    global f
    f = f + 1
    print("Melyik filmet szeretné megnézni?")
    print("1: Beugró a paradicsomba")
    print("2: Fekete párduc 2")
    print("3: Rosszul vagyok magamtól")
    print("4: Vissza a moziválasztóhoz!")
    film = int(input("Válassza ki a filmet: "))
    if film == 4:
        mozivalaszto()
        mozi()
        return 0
    if f == 1:
        mozi()

def mozi():
    print("Melyik teremben szeretné nézni a filmet?")
    print("1: VIP terem")
    print("2: 4DX terem")
    print("3: ScreenX")
    a = int(input("Válassza ki a termet: "))
    ticket = int(input("Hány jegyet szeretne vásárolni? "))
    idopont(a)

def idopont(a):
    ido1 = {
        "1": "10.00-13.00",
        "2": "13.10-15.10",
        "3": "15.20-17.20",
        "4": "18.30-20.30"
    }
    ido2 = {
        "1": "10.15-13.15",
        "2": "13.25-15.25",
        "3": "15.35-17.35",
        "4": "18.45-20.45"
    }
    ido3 = {
        "1": "10.30-13.30",
        "2": "13.40-15.40",
        "3": "15.50-17.50",
        "4": "18.00-20.45"
    }
    if a == 1:
        print("Melyik időpontban szeretné megnézni?")
        print(ido1)
        t = input("Válassza ki az időpontot:")
        x = ido1[t]
        print("Sikeres foglalás, jó szórakozást! ")
    elif a == 2:
        print("Melyik időpontban szeretné megnézni?")
        print(ido2)
        t = input("Válassza ki az időpontot:")
        x = ido2[t]
        print("Sikeres foglalás, jó szórakozást!")
    elif a == 3:
        print("Melyik időpontban szeretné megnézni?")
        print(ido3)
        t = input("Válassza ki az időpontot:")
        x = ido3[t]
        print("Sikeres foglalás, jó szórakozást!")
    return 0

varos()