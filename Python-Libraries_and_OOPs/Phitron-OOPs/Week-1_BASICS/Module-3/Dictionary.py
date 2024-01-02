person = {'name' : 'Md AL Amin', 'age' : 23, 'uni' : "NSU"}
# print(person)

for key, value in person.items():
    print(key,": ", value)

print(person.keys())
print(person.values())

del person['name']

new_data = list(person.values())
print(new_data)

for i, item in enumerate(new_data):
    print(i, item)