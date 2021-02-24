passOne = input(": ")
passTwo = input(": ")
if len(passOne) < 8:
    print("Короткий!")
elif "123" in passOne:
    print("Простой!")
elif passOne == passTwo:
    print("OK")
else:
    print("Различатся.")
