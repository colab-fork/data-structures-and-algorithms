# CSESS Permutation
# 5
# 4 2 5 3 1
# 1 3 5 4 2
# 3
# NO SOLUTION
def permutation():
    n = int(input())
    lis = []
    ls1 = []
    ls2 = []
    for i in range(1, n+1):
        lis.append(i)
    for i in range(len(lis)):
        if lis[i] % 2 == 0:
            ls1.append(lis[i])
        else:
            ls2.append(lis[i])
    lis = ls1 + ls2
    for i in range(len(lis)-1):
        c = abs(lis[i]- lis[i+1])
        if c < 2:
            ans = 'NO SOLUTION'
            break
        else:
            ans = lis
    print(ans)
permutation()


  """
>>> %Run -c $EDITOR_CONTENT
10
[2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

>>> %Run -c $EDITOR_CONTENT
3
NO SOLUTION
>>> 

  """
