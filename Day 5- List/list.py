#Creating a List
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

#Accessing List Elements
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Negative Indexing
fruits = ["Apple", "Banana", "Mango"]
print(fruits[-1])
print(fruits[-2])

#List Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

#modifying List Elements:

fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)

fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

'Different List Methods:'
#Insert an Element
fruits = ["Apple", "Mango"]
fruits.insert(1, "Banana")
print(fruits)

#Extend a List
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)