number = input(": ")
summ_min = int(number[0]) + int(number[1])
summ_max = int(number[1])+int(number[2])
minimum = min(summ_min, summ_max)
maximum = max(summ_max, summ_min)
print(f"{maximum}{minimum}")
