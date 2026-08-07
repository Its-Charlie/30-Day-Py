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