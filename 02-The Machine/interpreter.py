# This will import set_file() and read_byte() functions
# To read a file you must first call set_file("name_of_file"),
# Then you can call read_byte() to get the bytes of the file 1 by 1
from readfile import *

### The Protocol ###
# The first 4 bytes should be (in hex) 31 41 FA CE
# The next 2 bytes say how many operations will be in the file
# the next 1 byte contains the operations to perform

### Operations ###
# 0000 0001 - Addition
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
### 0000 0010 - Subtraction
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
# 0000 0011 - Multiplication
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
### 0000 0100 - Division
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
### 0000 0101 - Print
# The string starts immediately after the operation byte
# It ends when the the byte that codes for an ASCII newline is found (e.g. ‘\n’, ‘\x0a’)

### Result ###
# Create a list with the results from the operations in the order they are run
# For all math ops, push a number into the list
# For the "Print" op, push the ASCII string coded by the bytes into the list

# Put helper functions here, one type of function you may find useful
# is a lambda function, this can be defined by:
# dup_str = lambda str, p: str * p
# usage:
# dup_str("Hi", 4) -> "HiHiHiHi"
# Dictionaries may also be useful, and are defined by key value pairs:
# my_dict = {key1 : value1, key2  : value2,...}
# usage:
# my_dict[key1] -> value1
# keys and values can be anything even a function


# Write a function to open and then execute a program file formatted for "The Machine"
# program_file will be a string of the file to open
# As the program executes you should store a list of the results
# At the end return the list
def execute(program_file):
    result = []
    # set file
    # read header
    # get number of operations
    # for num of operations:
    ### get operation code
    ### run operation
    ### push result to list
    return result


# if you run `python interpreter.py`
# then the execute function will get run with program1
# however this line does not run when this file
# is imported by another .py file (like grader.py)
if __name__ == "__main__":
    execute("programs/program1")
