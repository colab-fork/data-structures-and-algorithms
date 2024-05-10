def missing_number():
    n = int(input())
    lis = list(map(int, input().split()))
    lis = sorted(lis)
    for i in range(len(lis)-1):
        if lis[i] + 1 != lis[i+1]:
            print(lis[i]+1)

missing_number()
        
"""
>>> %Run -c $EDITOR_CONTENT
5
2 3 1 5
4

"""
