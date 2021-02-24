limit_min = 1
linit_max = 1000
while limit_min < linit_max:
    num = int((linit_max + limit_min) / 2)
    print(num)
    output = input(": ")
    if output == "<":
        linit_max = num
    elif output == ">":
        limit_min = num
    elif output == "=":
        limit_min = linit_max
