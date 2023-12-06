# set is a unique collections

numbers = [12, 56, 98, 1, 3, 4, 5, 2, 3, 4, 6]
num_set = set(numbers)
print(num_set)
# name = 'Md al amin'
# print(set(name))

num_set.add(44)
print(num_set)

num_set.remove(2)
print(num_set)

for item in num_set:
    print(item)

if 98 in num_set:
    print('Haa')
else:
    print('Na')

A = {1, 3, 5}
B = {1, 2, 3, 4, 5}

print(A & B)
print(A | B)