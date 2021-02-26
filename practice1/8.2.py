stringY = int(input(": "))
deffY = stringY
stringX = int(input(": "))
deffX = stringX
mass = input(": ")
while stringY > 0:
    if stringY == deffY:
        print((mass) * deffX)
    elif stringY == 1:
        print((mass) * deffX)
    elif stringY < deffY:
        print((mass)+" "* (deffX - 2) + mass)
    stringY -=1
