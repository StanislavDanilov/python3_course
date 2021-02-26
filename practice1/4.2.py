dicti =[]
l = ""
finish = int()
i = -299
while True:
    l = input(": ")
    if float(l) < i:
        break
    else:
        finish += float(l)
        dicti.append(l)
    finish = float(finish/len(dicti))
print("%.2f" % finish)
