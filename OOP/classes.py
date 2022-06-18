class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for i in self.students:
            value += i.get_grade()
        return value / len(self.students)


s1 = Student("Bill", 19, 95)
s2 = Student("Tim", 18, 75)
s3 = Student("Jill", 19, 65)

c1 = Course("Science", 2)
c1.add_student(s1)
c1.add_student(s2)

print(c1.students[0].name)
print(s1.name)
print(c1.get_average_grade())
