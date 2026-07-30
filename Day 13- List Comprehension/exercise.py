#Filter Negative Numbers and Zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = [x for x in numbers if x <= 0]
print(result)

#Flatten List
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
result = [num for row in list_of_lists for num in row]
print(result)

#List of Tuples
result = [
    (x, x**0, x**1, x**2, x**3, x**4, x**5)
    for x in range(11)
]

print(result)