year = int(input("year: "))
if (year % 4 and year % 100) or (year % 400 == 0):
    print("Високосный")
else:
    print("Не Високосный")
