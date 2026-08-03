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