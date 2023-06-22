n =5
p = 3
def pageCount(n, p):
    lis = []
    for i in range(0, n+1, 2):
        sublis = []
        for j in range(1):
            if i == n:
                sublis.append(i)
                break
            else:
                sublis.append(i)
                sublis.append(i+1)
        lis.append(sublis)
        ret = []
    for i in range(len(lis)):
        if p in lis[i]:
            ret.append(i)
            ret.append(len(lis)-1-i)
    print(min(ret))
pageCount(n, p)


"""
>>> %Run -c $EDITOR_CONTENT
1
>>> 
"""
