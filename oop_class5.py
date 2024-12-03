class Student:
    def check_pass_fail(self):
        if self.marks >= 50:
            return f"Congratulations {self.name}!!! You have passed!!"
        else:
            return f"Sorry {self.name}, You have failed!!"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Janet", 30)
student2 = Student("Amos", 69)

did_pass = student1.check_pass_fail()
print(did_pass)

did_pass = student2.check_pass_fail()
print(did_pass)
