things = 'pen', 'pencel', 'book', 'paper', 'phone', 'laptop', 'pc'

print(things)
print(things[:4])
print(things[: : -1])

if 'book' in things:
    print('Yes')
else:
    print("Naa")

for item in things:
    print(item)

# nasted tupple
print(len(things))

# value change in tupple

mega = ([1, 3, 5, 5], [3, 5, 6, 7])
print(type(mega))
mega[1][0] = 99
print(mega[1])

mega[1][2] = 00
print(mega)