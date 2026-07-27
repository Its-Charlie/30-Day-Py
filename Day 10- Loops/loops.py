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