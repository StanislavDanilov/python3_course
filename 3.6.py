number = input(": ")
if number.isdigit():
    if len(number) > 3 or len(number) < 3:
        print("Error pincode")
    else:
        if number[0] == number[1] and number[0] == number[2] and number[1] == number[2]:
            print("В числе все цифры одинаковые.")
        elif number[0] == number[1] or number[1] == number[2] or number[0] == number[2]:
            print("В числе две одинаковые цифры")
        else:
            print("OK")
else:
    print("Error")

