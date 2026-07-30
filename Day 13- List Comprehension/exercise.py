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

#Flatten Countries
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

result = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]

print(result)

#Countries to Dictionary
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

result = [
    {
        "country": country.upper(),
        "city": city.upper()
    }
    for [(country, city)] in countries
]

print(result)

#Concatenate Names
names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]

result = [
    first + " " + last
    for [(first, last)] in names
]

print(result)

#Lambda for Slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

print(slope(2, 3, 5, 9))

#Lambda for y-intercept
y_intercept = lambda m, x, y: y - m * x

print(y_intercept(2, 3, 7))