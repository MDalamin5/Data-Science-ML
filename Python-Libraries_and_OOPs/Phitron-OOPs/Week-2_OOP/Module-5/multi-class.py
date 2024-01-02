class Student:
    def __init__(self, full_name, curn_calss, id) -> None:
        self.name = full_name
        self.cur_class = curn_calss
        self.id = id

    def __repr__(self) -> str:
        return f"The name of the student: {self.name}, class : {self.cur_class}, id: {self.id}"
    

# Teacher class

class Teacher:
    def __init__(self, name, id, subject) -> None:
        self.name = name
        self.id = id
        self.subject = subject

    def __repr__(self) -> str:
        return f"Teacher name: {self.name} and ID: {self.id}"
    

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teacher = []
        self.student = []


    def add_teacher(self, name, subject):
        id = len(self.teacher) + 1001
        teacher = Teacher(name, id, subject)
        self.teacher.append(teacher)


    def enroll_student(self, name, fees):
        if fees < 6500:
            print(f"{name} can not enroll b/c you need more {abs(6500 - fees)} Taka\n")
        else:
            id = len(self.student) + 1
            stu = Student(name, 'C', id)
            self.student.append(stu)
            print(f"Congrsulation {name} enroll Sussfully and your remain amount: {fees - 6500}")


    def __repr__(self) -> str:
        print(f"""*************Our Teacher**************""")
        for tech in self.teacher:
            print(tech)
        print('**************Our Student**************')
        for stu in self.student:
            print(stu)

        return f"All Done"
        

# alamin = Student('Md AL Amin', 10, 1811904)
# print(alamin)
phitron = School('Phitron')
phitron.add_teacher('MD AL AMin', 'DS')
phitron.add_teacher('Rahim Khan', 'DSA')
phitron.add_teacher('Kharim Khan', 'Algo')

phitron.enroll_student('Aminul', 6400)
phitron.enroll_student('Niloy', 6900)
phitron.enroll_student('Habib', 6400)
phitron.enroll_student('RAhim', 8400)

print(phitron)