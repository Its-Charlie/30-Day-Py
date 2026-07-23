#Creating a Tuple
from typing import List


fruits = ("Apple", "Banana", "Mango")
print(fruits)

#Tuple with Different Data Types
data = ("Siddhesh", 22, 75.5, True)
print(data)

#Accessing Tuple Elements
fruits = ("Apple", "Banana", "Mango")
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Tuple Slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

#Tuple Length
fruits = ("Apple", "Banana", "Mango")

print(len(fruits))

'Using Tuple Methods:'
#Count Occurrences
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))

#Find Index:
fruits = ("Apple", "Banana", "Mango")

print(fruits.index("Banana"))


#Tuple Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)

tuple3 = tuple1 + tuple2

print(tuple3)

#Tuple Repetition
numbers = (1, 2)

print(numbers * 3)

#Iterate Through a Tuple
fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)

#Tuple Packing
student = ("Siddhesh", 22, "AI & DS")

print(student)
#Tuple Unpacking
student = ("Siddhesh", 22, "AI & DS")

name, age, course = student

print(name)
print(age)
print(course)

#Convert List to Tuple
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)

#Convert Tuple to List
numbers = (10, 20, 30)

result = list(numbers)

print(result)