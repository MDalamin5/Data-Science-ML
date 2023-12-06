numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)

print(numbers[:])
numbers.insert(4, 99)
print(numbers)

numbers.remove(99)
numbers.remove(11)

print(numbers)

numbers.clear()
del numbers[:]
print(numbers)

num = [3, 4, 1, 57, 6]
num.sort()
print(num)

if 57 in num:
    num.remove(57)
    print('Data Remove done')

index = numbers.index(7)
print(index)