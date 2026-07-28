#Create Dictionary
student = {
    "name": "Charlie",
    "age": 22,
    "city": "Kamothe"
}

#Create Dictionary
students = {
    "name": "Charlie",
    "age": 22,
    "city": "Kamothe"
}

print(student)

#Empty Dictionary examples:
d = {}
d = dict()

#Length function:
print(len(student))

#Access Values single key:
print(student["name"])

#Access Values multiple keys:
person = {
    "address": {
        "city": "Mumbai"
    }
}
print(person["address"]["city"])

#Add New Item
student["college"] = "ABC College"
print(student)

#Modify Value
student["age"] = 23

#Check Key
print("age" in student)
True

#Remove and Delete Items 
student.pop("age")

del student["city"]

#delete student dictionary
del student

#To get all keys in a dictionary, use the keys() method:
print(students.keys())

#To get all values in a dictionary, use the values() method:
print(students.values())

#To get all key-value pairs in a dictionary, use the items() method:
print(students.items())

#copy()
new_students = students.copy()

#clear()
students.clear()