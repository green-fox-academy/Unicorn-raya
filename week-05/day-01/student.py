from collections import namedtuple
Person = namedtuple('Person','name age gender grades')
p1  = Person(name = "John", age = 16, gender = "male", grades = [5, 5, 4, 2])
p2  = Person(name = "Jane", age = 15, gender = "female", grades = [4, 3, 4, 4, 5])
p3  = Person(name = "Bob", age = 17, gender = "female", grades = [100, 5, 5, 1])
p4  = Person(name = "Bb", age = 27, gender = "male", grades = [2, 2])


p0 = [p1,p2,p3,p4]

def isTypeMale(person_type):
    return person_type.gender == "male"
def __str__(person_type):
    return " ".join([ person_type.name,str(person_type.age),person_type.gender," ".join([str(i) for i in person_type.grade]) ])


male_list = filter(isTypeMale,p0)
j_name = filter(lambda x: x.name[0] == 'J',p0)
girl_list = filter(lambda x: x.gender == 'female',p0)
four_above_people = filter(lambda x: max(x.grades) > 4, p0)
j_boy = filter(lambda x:x.gender == "male" and x.name[0] == "J",p0)
female_avg4 = filter(lambda x:x.gender == "female" and sum(x.grades)/len(x.grades) > 4,p0)
# Create a new list that only includes who's at least two 5s
db5 = filter(lambda x:x.grades.count(5) >= 2,p0)
# Create a new list that only includes who's grade average is above 4 and at at least got two 5s
task8 = filter(lambda x:x.grades.count(5) >= 2 and sum(x.grades)/len(x.grades) > 4,p0)


for i in task8:
    print(i)





