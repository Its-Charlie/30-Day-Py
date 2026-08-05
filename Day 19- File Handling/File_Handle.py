'''
File Modes
r  # Read
w  # Write (overwrite)
a  # Append
x  # Create new file
t  # Text mode
b  # Binary mode
'''

#Read File
with open("file.txt", "r") as f:
    data = f.read()

#Read One Line
with open("file.txt") as f:
    print(f.readline())

#Read All Lines
with open("file.txt") as f:
    print(f.readlines())

#Write File
with open("file.txt", "w") as f:
    f.write("Hello")

#Append File
with open("file.txt", "a") as f:
    f.write("\nNew Line")

#Delete File
import os

if os.path.exists("file.txt"):
    os.remove("file.txt")

#JSON → Dictionary
import json

json_str = '{"name":"Charlie","age":22}'
data = json.loads(json_str)
print(data)

#Dictionary → JSON String
import json

person = {"name":"Charlie","age":22}
print(json.dumps(person, indent=4))

#Save Dictionary as JSON File
import json

person = {"name":"Charlie","age":22}

with open("person.json", "w") as f:
    json.dump(person, f, indent=4)