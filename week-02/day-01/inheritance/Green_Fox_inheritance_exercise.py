# person
# Create a Person class with the following fields:

# name: the name of the person
# age: the age of the person (whole number)
# gender: the gender of the person (male / female)
# And the following methods:

# introduce(): prints out "Hi, I'm name, a age year old gender."
# get_goal(): prints out "My goal is: Live for the moment!"
# And the following constructors:

# Person(name, age, gender)
# Person(): sets name to Jane Doe, age to 30, gender to female
# Student
# Create a Student class that has the same fields and methods as the Person class, and has the following additional

# fields:
# previous_organization: the name of the student’s previous company / school
# skipped_days: the number of days skipped from the course
# methods:
# get_goal(): prints out "Be a junior software developer."
# introduce(): "Hi, I'm name, a age year old gender from previous_organization who skipped skipped_days days from the course already."
# skip_days(number_of_days): increases skipped_days by number_of_days
# The Student class has the following constructors:

# Student(name, age, gender, previous_organization): beside the given parameters, it sets skipped_days to 0
# Student(): sets name to Jane Doe, age to 30, gender to female, previous_organization to The School of Life, skipped_days to 0
# Mentor
# Create a Mentor class that has the same fields and methods as the Person class, and has the following additional

# fields:
# level: the level of the mentor (junior / intermediate / senior)
# methods:
# get_goal(): prints out "Educate brilliant junior software developers."
# introduce(): "Hi, I'm name, a age year old gender level mentor."
# The Mentor class has the following constructors:

# Mentor(name, age, gender, level)
# Mentor(): sets name to Jane Doe, age to 30, gender to female, level to intermediate
# Sponsor
# Create a Sponsor class that has the same fields and methods as the Person class, and has the following additional

# fields:
# company: name of the company
# hired_students: number of students hired
# method:
# introduce(): "Hi, I'm name, a age year old gender who represents company and hired hired_students students so far."
# hire(): increase hired_students by 1
# get_goal(): prints out "Hire brilliant junior software developers."
# The Sponsor class has the following constructors:

# Sponsor(name, age, gender, company): beside the given parameters, it sets hired_students to 0
# Sponsor(): sets name to Jane Doe, age to 30, gender to female, company to Google and hired_students to 0
# Cohort
# Create a Cohort class that has the following

# fields:
# name: the name of the cohort
# students: a list of Students
# mentors: a list of Mentors
# methods:
# add_student(Student): adds the given Student to students list
# add_mentor(Mentor): adds the given Mentor to mentors list
# info(): prints out "The name cohort has len(students) students and len(mentors) mentors."
# The Cohort class has the following constructors:

# Cohort(name): beside the given parameter, it sets students and mentors as empty lists
# Test input
# people = []

# mark = Person('Mark', 46, 'male')
# people.append(mark)
# jane = Person()
# people.append(jane)
# john = Student('John Doe', 20, 'male', 'BME')
# people.append(john)
# student = Student()
# people.append(student)
# gandhi = Mentor('Gandhi', 148, 'male', 'senior')
# people.append(gandhi)
# mentor = Mentor()
# people.append(mentor)
# sponsor = Sponsor()
# elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
# people.append(elon)
# student.skip_days(3)

# for i in range(5):
#     elon.hire()

# for i in range(3):
#     sponsor.hire()

# for person in people:
#     person.introduce()
#     person.get_goal()

# awesome = LagopusClass('AWESOME')
# awesome.add_student(student);
# awesome.add_student(john);
# awesome.add_mentor(mentor);
# awesome.add_mentor(gandhi);
# awesome.info();
# Test output
# Hi, I'm Mark, a 46 year old male.
# My goal is: Live for the moment.
# Hi, I'm Jane Doe, a 30 year old female.
# My goal is: Live for the moment.
# Hi, I'm John Doe, a 20 year old male from BME who skipped 0 days from the course already.
# My goal is: Be a junior software developer.
# Hi, I'm Jane Doe, a 30 year old female from The School of Life who skipped 3 days from the course already.
# My goal is: Be a junior software developer.
# Hi, I'm Gandhi, a 148 year old male senior mentor.
# My goal is: Educate brilliant junior software developers.
# Hi, I'm Jane Doe, a 30 year old female intermediate mentor.
# My goal is: Educate brilliant junior software developers.
# Hi, I'm Jane Doe, a 30 year old female who represents Google and hired 3 students so far.
# My goal is: Hire brilliant junior software developers.
# Hi, I'm Elon Musk, a 46 year old male who represents SpaceX and hired 5 students so far.
# My goal is: Hire brilliant junior software developers.
# The AWESOME cohort has 2 students and 2 mentors.


class Person(object):
    def __init__(self,name = "Jane Doe",age = 30,gender = "female"):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, I\'m {self.name}, a {self.age} year old gender.")
    
    def get_goal(self):
        print("My goal is: Live for the moment!")

class Student(Person):
    def __init__(self,name = "Jane Doe",age=30,gender="female",pre_org="the school life",skipped_days=0):
        super().__init__(name,age,gender)
        self.pre_org = pre_org
        self.skipped_days = skipped_days
    
    def get_goal(self):
        print("Be a junior software developer.")
    
    def introduce(self): 
        print(f"Hi, I\'m {self.name}, a {self.age} year old {self.gender}")
        print(f"from {self.pre_org} who skipped {self.skipped_days} days")
        print("from the course already.")
    
    def skip_days(self,number_of_days): 
        self.skipped_days += number_of_days

class Mentor(Person):
    def __init__(self,name = "Jane Doe",age = 30,gender = "female",level = "intermediate"):
        super().__init__(name,age,gender)
        self.level = level

    def get_goal(self): 
        print("Educate brilliant junior software developers.")

    def introduce(self):
        print(f"Hi, I\'m {self.name}, a {self.age} year old {self.gender}")
        print(f"{self.level} mentor")

class Sponsor(Person):
    def __init__(self,name="Jane Doe",age=30,gender="female", company= "google", hired_students = 0):
        super().__init__(name,age,gender)
        self.company = company
        self.hired_students = hired_students
    
    def introduce(self):
        print(f"Hi, I\'m {self.name}, a {self.age} year old {self.gender}")
        print(f"who represents {self.company} and {self.hired_students} students so far.")
    
    def hire(self):
        self.hired_students += 1

    def get_goal(self):
        print("Hire brilliant junior software developers.")

class Cohort():
    def __init__(self,name,students= [],mentors = []):
        self.name = name
        self.students = students
        self.mentors = mentors
    
    def add_student(self,student):
        self.students.append(student)

    def add_mentor(self,mentor):
        self.mentors.append(mentor)

    def info(self):
        print(f"The {self.name} cohort has {len(self.students)} students and {len(self.mentors)} mentors.")

people = []
mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for person in people:
    person.introduce()
    person.get_goal()

awesome = Cohort('AWESOME')
awesome.add_student(student)
awesome.add_student(john)
awesome.add_mentor(mentor)
awesome.add_mentor(gandhi)
awesome.info()