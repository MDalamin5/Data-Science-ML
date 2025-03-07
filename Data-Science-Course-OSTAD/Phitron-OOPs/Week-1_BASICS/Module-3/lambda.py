# sum function

def add(a, b):
    return a + b

# lambda functions

add = lambda a, b: a + b
print(add(4, 2))

double = lambda x : x * 2

numbers = [1, 2, 4, 5, 6, 7, 8, 9, 22, 44]

double_num = map(double, numbers)
print(numbers)
print(list(double_num))

sqr_numbers = map(lambda x : x**2 , numbers)
print(list(sqr_numbers))

# filter fun

person = [
    {'name' : 'Md Al AMin', 'age' : 23},
    {'name' : 'Aminul Islam', 'age' : 20},
    {'name' : 'shahin kahn', 'age' : 25},
    {'name' : 'Habibur rahaman', 'age' : 19},
    {'name' : 'Polok ahamed', 'age' : 24},
    {'name' : 'Shobuj ahamed', 'age' : 17}
]

new_person = filter(lambda men : men['age'] > 23, person)
print(list(new_person))