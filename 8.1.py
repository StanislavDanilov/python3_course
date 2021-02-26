stringY = float(input(": "))
stringX = float(input(": "))
deffX = stringX
deffprintX = []
deffprintY = []
i = 1
while stringX > 0:
    l = i / deffX
    deffprintX.append(float(i))
    deffprintY.append(l)
    stringX -= 1
    i += 1
deffprintY.append(i / deffX)
deffX += 1
deffprintX.append(deffX)
print(*deffprintX, sep='\t')
print(*deffprintY, sep='\t')
