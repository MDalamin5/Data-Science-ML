# in, not, not in, is, is not
a = 4
if a > 5:
    print(f'5 er besi')
elif a > 3:
    print(f"Halka boro")
elif a == 2:
    print(f'Equal to 2')
else:
    print(f'Hello sir you are in else part')


boss = False

if boss is True:
    print(f"i'm comming with taler box")
else:
    print(f"lunch ar por asen")

# nested condition
coin = 'tail'

if boss == True:
    print(f'Boss is god')
    if coin == 'tail':
        print(f'Bolling')
    else:
        print(f'bating')
else:
    print('Boss is loss')
    if coin == 'tail' and 5 % 2 != 2:
        print(f'boling')