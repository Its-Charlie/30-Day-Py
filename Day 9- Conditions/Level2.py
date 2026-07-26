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

'''Get the month from user input then check if the season is Autumn, Winter, Spring or
Summer. If the user input is: September, October or November, the season is Autumn.
December, January or February, the season is Winter. March, April or May, the season is
Spring June, July or August, the season is Summer'''
month = input("Enter month: ").lower()

if month in ["september", "october", "november"]:
    print("Autumn")
elif month in ["december", "january", "february"]:
    print("Winter")
elif month in ["march", "april", "may"]:
    print("Spring")
elif month in ["june", "july", "august"]:
    print("Summer")
else:
    print("Invalid month")