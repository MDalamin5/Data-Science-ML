i = 0
while i <= 10:
    if i % 2 == 0 and i != 0 and i != 10:
        print(i)
    i += 1
    if i == 6:
        # break
        continue