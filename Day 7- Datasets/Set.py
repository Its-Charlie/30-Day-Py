#Create a set of data:
# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Using len() to determine the length of the set:
print(len(it_companies))  # Output: 7

#add ing an element to the set:
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies
it_companies.update(["Intel", "Tesla", "Adobe"])
print(it_companies)

#Remove one company
it_companies.remove("IBM")
print(it_companies)

#Difference between remove() and discard()
# remove() gives an error if the item is not found
# discard() does not give an error if the item is not found

fruits = {"Apple", "Banana"}

fruits.discard("Orange")   # No Error

# fruits.remove("Orange")  # Error

#Join A & B
print(A | B)

#Find A intersection B
print(A & B)