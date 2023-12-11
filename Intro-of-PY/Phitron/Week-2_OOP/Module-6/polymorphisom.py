from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    @abstractmethod
    def make_scound(self):
        pass



class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_scound(self):
        print("Gaw gawwwwww gawwwww")

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)


    def make_scound(self):
        print('bhaaaaaaa bhaaaaaaa')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_scound(self):
        print('Mawwwwww massseeeeewwwww')



doggy = Dog('BD Kutta')
sagol = Goat('Patha')
cattt = Cat('Hulu Makur')

all_animal = [doggy, sagol, cattt]

for item in all_animal:
    item.make_scound()
