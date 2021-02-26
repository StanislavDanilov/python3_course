number = input(": ")
i = 1
while True:
    if (str(2 ** i) == str(number)):
        print(i)
        break
    else:
        i =  i + 1
