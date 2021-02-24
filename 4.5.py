number = int(input(": "))
i = 0;
while True:
    if number == 1:
        break
    elif number % 2 == 0:
        number = number / 2
    elif number % 2 != 0:
        number = 3 * number + 1
    i+= 1
print(i)
