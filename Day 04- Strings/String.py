#Creating Strings:
first_name = "Siddhesh"
last_name = "Yadav"

print(first_name)
print(last_name)

#String Concatenation:
first_name = "Siddhesh"
last_name = "Yadav"

full_name = first_name + " " + last_name
print(full_name)

#String Repetition:
word = "Python "
print(word * 3)

#String Length:
text = "Artificial Intelligence"
print(len(text))

#Character Indexing:
language = "Python"

print(language[0])
print(language[1])
print(language[5])

print(language[-1])
print(language[-2])
print(language[-6])

#Convert to Uppercase
text = "python programming"
print(text.upper())

#Convert to Lowercase
text = "PYTHON PROGRAMMING"
print(text.lower())


'Different String Methods:'
#Find a Word
text = "Python Programming"
print(text.find("Programming"))

#Count Characters
text = "banana"
print(text.count("a"))

#Check Starts With
text = "Python Programming"
print(text.startswith("Python"))

#Check Ends With
text = "Python Programming"
print(text.endswith("Programming"))