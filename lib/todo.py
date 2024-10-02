# File: lib/todo.py

def todo(string, filename):
    # Open file and read lines into variable
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # See if 'string' is in any line
    for line in lines:
        if string in line:
            return True
    return False
