fullName = input("You'r name: ")
email = input("You'r email: ")

if "@" in fullName:
    print("Некорректный логин")
elif "@" in email:
    print("OK")
else:
    print("Некорректный адрес")

