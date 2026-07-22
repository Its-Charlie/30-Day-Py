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

#Remove an Element
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)

#Pop an Element
fruits = ["Apple", "Banana", "Mango"]
fruits.pop()
print(fruits)

#Pop by Index
fruits = ["Apple", "Banana", "Mango"]
fruits.pop(1)
print(fruits)

#Delete an Element
numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

#Clear the List
numbers = [10, 20, 30]
numbers.clear()
print(numbers)