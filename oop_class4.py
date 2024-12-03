class Student:
    def check_pass_fail(self):
        if self.marks >= 50:
            return "Congratulations!!! You have passed!!"
        else:
            return "Sorry, You have failed!!"


student1 = Student()
student1.name = "Amos"
student1.marks = 50

did_pass=student1.check_pass_fail()
print(did_pass)

student2 = Student()
student2.name = "Robin"
student2.marks = 30

did_pass=student2.check_pass_fail()
print(did_pass)