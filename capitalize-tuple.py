# Given a tuple return a tuple of capital letters of each string's first word from the tuple 
def tuple2capitalize(tup):
    return tuple(x[0].capitalize() for x in tup)

print(tuple2capitalize(("John", "rabss", "krabs")))

"""
>>> %Run -c $EDITOR_CONTENT
('J', 'R', 'K')
>>> 
"""
