rules = "\n\n!!!!Выберите тунель исходя из порядкового номера\n Пример: Вы дошли до развилки, перед вами два тунеля направо или прямо\n Чтоб пойти прямо отправьте кнопку '2'!!!!\n"
print(f"Вы находитесь в пещере на развилке. Вы можете пойти налево, направо или прямо.{rules}")
while True:
    i = input(": ")
    if i == "1":
        i = input(f"Вы дошли до развилки, перед вами два тунеля направо или прямо\n{rules}: ")
        if i == "2":
            print("Вы упали в пропасть ")
            break
        elif i == "3":
            print("Вы выжили")
            break
        else:
            print("Error input")
            break
    elif i == "2":
        i = input(f"Вы дошли до развилки, перед вами два тунеля направо или прямо\n{rules}: ")
        if i == "3":
            print("Вы вышли в лес")
            break
        elif i == "1":
            print("Вы утонули")
            break
        else:
            print("Error input")
            break
    elif i == "3":
        print("Вас съел крокодил")
        break
    else:
        print("Error input")
        break
