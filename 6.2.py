n = int(input(": "))
stars = 1
while True:
    if n == 0:
        break
    print(' '*(n-1) + '*'*stars )
    n -= 1
    stars += 2
