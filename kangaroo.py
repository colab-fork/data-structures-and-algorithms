x1 = 0
v1 = 3
x2 = 4
v2 = 2
def kangaroo(x1, v1, x2, v2):
    result = False
    for i in range(1000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            result = True
            break
    if result == True:
        return 'YES'
    else:
        return 'NO'
kangaroo(x1, v1, x2, v2)

""""
Faster Approach
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        # If the velocities are the same, they can't meet
        return 'NO'
    elif (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        # If the difference in positions is divisible evenly by the difference in velocities,
        # and the quotient is non-negative, they will meet at some point
        return 'YES'
    else:
        # Otherwise, they won't meet
        return 'NO'

""""
