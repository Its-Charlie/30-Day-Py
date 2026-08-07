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