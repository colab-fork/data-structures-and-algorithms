# 5
# 3 2 5 1 7 - > 1 + 4

def increasing_array():
    n  = int(input())
    lis = list(map(int, input().split()))
    turns = 0
    for i in range(len(lis)-1):
        if lis[i] > lis[i+1]:
            turns += lis[i]-lis[i+1]
    print(turns)

increasing_array()

"""
>>> %Run -c $EDITOR_CONTENT
5
3 2 5 1 7
5
"""
