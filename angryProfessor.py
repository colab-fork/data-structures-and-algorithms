n = 4
k = 3
a = [-1, -3, 4, 2]
def angryProfessor(k, a):
    lis = []
    for i in a:
        if i <= 0:
            lis.append(i)
    if len(lis) < k:
        print('YES')
    else:
        print('NO')
angryProfessor(k,a)


"""
>>> %Run -c $EDITOR_CONTENT
YES
>>> 

"""
