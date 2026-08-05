'''
File Modes
r  # Read
w  # Write (overwrite)
a  # Append
x  # Create new file
t  # Text mode
b  # Binary mode
'''

#Read File
with open("file.txt", "r") as f:
    data = f.read()