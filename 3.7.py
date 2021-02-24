number = int(input("Введите трехзначное число\n"))
if len(str(number)) > 3:
    print("Слишком длинное число")
    exit(1)
digit = [number % 10, (number // 10) % 10, number // 100]
digit = sorted(digit)
if (digit[0] + digit[2]) / 2 == digit[1]:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")
