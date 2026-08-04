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