firstCouch = int(input(": "))
twoCouch = int(input(": "))
while True:
    if firstCouch == 0 and twoCouch == 0:
        break
    oneAnswer = int(input(": "))
    twoAnswer = int(input(": "))
    if oneAnswer == 1:
        firstCouch = firstCouch - twoAnswer
    elif oneAnswer == 2:
        twoCouch = twoCouch - twoAnswer
    print(f"{firstCouch} {twoCouch}")
    
