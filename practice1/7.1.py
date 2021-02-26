stringI = int(input(": "))
i = 0
while stringI != 0:
    inputWhile = input(": ")
    if "Кот" in inputWhile or "кот" in inputWhile:
        i = 1
    stringI -= 1
if i == 1:
    print("МЯУ")
else:
    print("НЕТ")
