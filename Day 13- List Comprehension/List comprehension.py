numbers = [x for x in range(6)]
print(numbers)

#List Comprehension with if
even = [x for x in range(11) if x % 2 == 0]
print(even)

#Mathematical Operations
square = [x**2 for x in range(6)]
print(square)

#Lambda Function
square = lambda x: x*x
print(square(5))

#Lambda Returning Lambda
def power(x):
    return lambda y: x ** y

cube = power(2)

print(cube(3))