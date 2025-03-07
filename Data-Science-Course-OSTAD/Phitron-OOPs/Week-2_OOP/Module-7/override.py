class Person:
    def __init__(self, name, age, weight, height) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self):
        raise NotImplementedError
    
    def __repr__(self) -> str:
        return f"Name: {self.name} age: {self.age}"
    

class Cricketer(Person):
    def __init__(self, name, age, weight, height, team_name) -> None:
        super().__init__(name, age, weight, height)
        self.team_name = team_name

    def eat(self): # over-riding Method
        print(self.name, 'are eating healty Food')

    # method Overloading

    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.weight * other.weight
    
    def __gt__(self, other):
        return self.age > other.age

    


sakib = Cricketer('Sakib Al Hasan', 33, 70, 65, 'BD-National')
sabbir = Cricketer('Sabbir', 30, 71, 64, 'Sporting Club')

print(sakib + sabbir)
print(sakib > sabbir)
print(sabbir * sakib)

