import math as m
n = 5
def viralAdvertising(n):
    ret = 0
    x = 5
    for i in range(1, n+1):
        likes  = m.floor(x/2)
        x = likes * 3
        ret += likes 
    print(ret)
        
    

viralAdvertising(n)

"""
>>> %Run -c $EDITOR_CONTENT
24


"""
