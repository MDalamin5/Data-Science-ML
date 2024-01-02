class Family:
    def __init__(self, name, father_name) -> None:
        self.name = name
        self.father_name = father_name

    def __repr__(self) -> str:
        return f"Father name: {self.father_name}, Name: {self.name}"
    

class Student():
    def __init__(self,cur_class) -> None:
        self.cur_class = cur_class


class Sports:
    def __init__(self, game) -> None:
        self.game = game


class Person(Family, Student, Sports):
    def __init__(self, name, father_name, cur_class, game) -> None:
        super().__init__(name, father_name)
        Student.__init__(self, cur_class)
        Sports.__init__(self, game)



alamin = Person('Md Al Amin', 'Md Badrul Islam', 'UG', 'Cricket')
print(alamin)