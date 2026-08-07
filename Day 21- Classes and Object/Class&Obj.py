#Create a Class
class Person:
    pass

#Create Object

p = Person()

#Constructor (__init__)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Charlie", 22)

print(p.name)
print(p.age)

#Create a Class with Methods

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p = Person("Charlie")
p.greet()

#Default Constructor Values
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p = Person()

print(p.name)
print(p.age)

#Modifying Object
class Student:
    def __init__(self):
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

s = Student()

s.add_skill("Python")
s.add_skill("SQL")

print(s.skills)

#Inheritance
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    pass

s = Student()

s.greet()