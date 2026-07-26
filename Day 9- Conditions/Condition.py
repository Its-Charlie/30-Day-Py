#If condition:
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

##If-else condition:
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#If-elif-else condition:
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

##Nested if condition:
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

