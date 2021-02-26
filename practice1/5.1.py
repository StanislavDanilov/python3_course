day = int(input(": "))
m = int(input(": "))
year = int(input(": "))

if m == 2:
    m = 12
elif m == 1:
    m = 11
else:
    m -= 2
c = year%100

print((day + ((13*m -1) //5) + year + year + (year //4 + c//4 - 2*c + 777)) % 7 )

#not job !!!!
