#While Loop:
print("While Loop:")
count = 0
while count < 5:
    print(count, end=" ")
    count = count + 1
    print()

#while Loop with else:
print("While Loop with else:")
count = 0
while count < 5:
    print(count,sep="\n")
    count = count + 1
else:
    print(count)


#while Loop with break:
print("While Loop with break:")
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

#while Loop with continue:
print("While Loop with continue:")
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

#For Loop:
print("For Loop:")
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

#Using For loop on string:
print("Using For loop on string:")
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

#Using For loop on tuple:
print("Using For loop on tuple:")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

#For loop with dictionary:
print("For loop with dictionary:")
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

#Using For Loop in set:
print("Using For Loop in set:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

#Using For Loop with break:
print("Using For Loop with break:")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

#Using For Loop with continue:
print("Using For Loop with continue:")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

#Using For Loop with pass:
print("Using For Loop with pass:")
for number in range(6):
    pass