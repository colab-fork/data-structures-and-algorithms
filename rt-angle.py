def find_angle(ab,bc):
    import math
    angle = math.degrees(math.atan2(ab,bc))
    deg = chr(176)
    ans = str(round(angle)) + deg
    print(ans)
ab = int(input())
bc = int(input())


find_angle(ab,bc)
 
"""
>>> %Run -c $EDITOR_CONTENT
10 10
45°

"""
