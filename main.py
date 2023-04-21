class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    mark = 1
    hunger = 10
    def __init__(self,name):
        super().__init__(name, 15)

class Teacher(Person):
    def __init__(self,name):
        super().__init__(name,25)

    def give_mark (self,student):
        print('Teacher give grade to', student.name)
        student.mark = 12

class Mom(Person):
    def __init__(self,name):
        super().__init__(name,25)
    def feed(self,student):
        student.hunger -= 1

good_student1 = Student("Sasha")
good_student2 = Student("Slavik")
teacher = Teacher("Kiril")

print(good_student1.mark)
teacher.give_mark(good_student1)
teacher.give_mark(good_student2)
print(good_student1.mark)

