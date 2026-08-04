#Import
import re

'''Syntax of re.match():
re.match(pattern, text)'''

text = "Python is awesome"

print(re.match("Python", text))

'''re.search()

Finds first occurrence.

re.search(pattern, text)
'''

text = "I love Python"

print(re.search("Python", text))

'''re.findall()
Returns all matches as a list.
syntax:
re.findall(pattern, text)'''

text = "Python Java Python C++ Python"

print(re.findall("Python", text))

'''
re.sub()
Replaces matched text.
syntax:
re.sub(pattern, replacement, text)'''

text = "I love Python"

print(re.sub("Python", "Java", text))