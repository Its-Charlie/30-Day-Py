#Create Dictionary
student = {
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