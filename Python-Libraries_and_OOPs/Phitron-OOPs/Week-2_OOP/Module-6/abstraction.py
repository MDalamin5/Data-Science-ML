from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def speed(self):
        pass



class Dog(Animal):
    def __init__(self, name, age, food_name) -> None:
        super().__init__(name, age)
        self.food = food_name

    def eat(self):
        print(f"{self.name} is eating {self.food}")

    
    def speed(self, speed):
        print(f"{self.name} top speed is {speed}")
    

    


buck = Dog('Buck', 3, 'Beef')
buck.eat()
buck.speed(233)
