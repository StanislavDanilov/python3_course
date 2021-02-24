day = int(input(": "))
m = int(input(": "))
year = int(input(": "))

c = year/100

print((day + ((13*m -1) //5) + year + year + (year //4 + c//4 - 2*c + 777)) // 7 )

