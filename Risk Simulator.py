from random import *

attinput = input("Number of armies of attacker: ")
definput = input("Number of armies of defender: ")

attarmies = int(attinput)
defarmies = int(definput)

print("========================================")

while attarmies>1 and defarmies>0:
    attdie = [0,0,0]
    defdie = [0,0,0]
    attdice = attarmies - 1
    defdice = defarmies
    if attdice>3:
        attdice = 3
    if defdice>3:
        defdice = 3
    for i in range(attdice):
        attdie[i] = randint(1,6)
    for i in range(defdice):
        defdie[i] = randint(1,6)
    if attdie[0]<attdie[1]:
        s = attdie[1]
        attdie[1] = attdie[0]
        attdie[0] = s
    if attdie[1]<attdie[2]:
        s = attdie[2]
        attdie[2] = attdie[1]
        attdie[1] = s
    if attdie[0]<attdie[1]:
        s = attdie[1]
        attdie[1] = attdie[0]
        attdie[0] = s
    if defdie[0]<defdie[1]:
        s = defdie[1]
        defdie[1] = defdie[0]
        defdie[0] = s
    if defdie[1]<defdie[2]:
        s = defdie[2]
        defdie[2] = defdie[1]
        defdie[1] = s
    if defdie[0]<defdie[1]:
        s = defdie[1]
        defdie[1] = defdie[0]
        defdie[0] = s
    if attdice<defdice:
        comp = attdice
    else:
        comp = defdice
    for i in range(comp):
        if attdie[i]>defdie[i]:
            defarmies = defarmies - 1
        else:
            attarmies = attarmies - 1
    print("----------------------------------------")
    print("Attacker rolled:",attdie)
    print("Defender rolled:",defdie)
    print("Attacker has",attarmies,"armies")
    print("Defender has",defarmies,"armies")
