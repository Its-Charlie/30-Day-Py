#Specific Exceptions
try:
    # code
    pass
except TypeError:
    print("Type Error")
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Division by Zero")

'else => Runs only if no exception occurs.'

try:
    x = 10 / 2
except:
    print("Error")
else: 
    print("Success")

'finally => Runs every time.'

try:
    x = 10 / 2
except:
    print("Error")
finally:
    print("Always runs")

#Exception as Variable
try:
    x = 10 + "5"
except Exception as e:
    print(e)

'Packing & Unpacking'

#Unpacking List
def add(a, b, c):
    return a + b + c

lst = [1, 2, 3]

print(add(*lst))

#Unpacking Dictionary
def info(name, age):
    print(name, age)

d = {
    "name": "Charlie",
    "age": 22
}

info(**d)

#Packing (*args)
def total(*args):
    print(args)

total(1,2,3,4)