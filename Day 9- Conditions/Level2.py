'''Write a code which gives grade to students according to theirs scores:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```'''
score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
else:
    print("Grade F")