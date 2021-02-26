i = 0;
while i < 17:
    number = int(input(": "))
    if i == 0:
        print(str(i) + str(number) + "= Yes")
    elif i % number == 0:
        print("Yes")
    else:
        print("No")
    i+=1
