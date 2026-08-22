class Student:
    def __init__(self, student_id, name, gender, department, year, semester, age):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.department = department
        self.year = year
        self.semester = semester
        self.age = age

    def display(self):
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Year       :", self.year)
        print("Semester   :", self.semester)

    def to_dict(self):
        return self.__dict__.copy()
