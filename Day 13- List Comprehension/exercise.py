#Filter Negative Numbers and Zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = [x for x in numbers if x <= 0]
print(result)