# Teacher Student
# Create Student and Teacher classes
# Student
# learn()
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer()

class Teacher(object):
    def teach(self,student):
        student.learn()
        
    def answer(self):
        return "wtf u learn so far"
        

class Student(object):
    def learn(self):
        return "learning..."
    
    def question(self,teacher):
        return teacher.answer()

teacher = Teacher()
student = Student()

print(teacher.answer())
print(student.question(teacher))