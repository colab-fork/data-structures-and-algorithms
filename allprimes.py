def allprimes(num):
    lis = []
    print(1)
    for i in range(0, num+1):
        for j in range(1, i+1):
            if i % j == 0:
                lis.append(j)
        if len(lis) == 2:
            print(j)
        lis = []
            
num = int(input())
allprimes(num)


"""

>>> %Run -c $EDITOR_CONTENT
100
1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

"""
