# Reverse a string without using reversed function 

def reverse_string(s):
    reversed=''
    for i in range(len(s)-1, -1, -1):
        reversed += s[i]
    print(reversed)


reverse_string('Shahid')


"""

>>> python t.py
dihahS

"""
