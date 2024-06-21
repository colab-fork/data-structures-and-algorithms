# Reverse a string without using reversed function 

def reverse_string(s):
    reversed=''
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    print(reversed_string)

# Alternate method using stacks.

def revered_string_stack(s):
    stack= []
    for i in s:
       stack.append(i)
    reversed_string = '' 
    while stack:
        reversed_string += stack.pop()
    print(reversed_string)


string = 'Shahid'

reversed_string_stack(string)
reversed_string_stack(string)


"""

>>> python t.py
dihahS
dihahS
"""
