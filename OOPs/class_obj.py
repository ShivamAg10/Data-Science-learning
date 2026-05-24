class Student:
    # Properties/ features of class(Student)
    subject = "Python" # Class attribute
    college = "ABC"
    year = 4
    
    def __init__(self, fullName, cgpa): # parameterized constructor
        print(self)
        print("This is Constructor")
        self.name = fullName # instance attribute
        self.cgpa = cgpa
    
    def get_cgpa(self): # default constructor
        return self.cgpa

# stu1 = Student()
# stu2 = Student()
# print(stu1)
# print(stu1.subject, stu1.college, stu1.year)

# name = input("Enter your name: ")
# stu1 = Student(name, 9.0)
# print(stu1.get_cgpa(), stu1.college)