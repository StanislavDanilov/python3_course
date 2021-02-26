stringI = input(": ")
i = 1
numerfind = 0
while True:
    i+=1;
    inputWhile = input(": ")
    if "Кот" in inputWhile or "кот" in inputWhile:
        numerfind = i
    elif inputWhile == "СТОП":
        break
if numerfind > 0:
    print(numerfind)
else:
    print("НЕТ")
