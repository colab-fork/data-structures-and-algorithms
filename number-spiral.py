# first 5 rows and columns of the infinite matrix
s = [[1, 2, 9, 10, 25], [4, 3, 8, 11, 24], [5, 6, 7, 12, 23], [16, 15, 14, 13, 22], [17, 18, 19, 20, 21]]
def number_spiral(s):
    lis = []
    t = int(input())
    while t > 0:
        y, x = map(int, input().split())# 2 , 3
        row = y
        col = x
        for i in range(len(s)):
            for j in range(len(s[i])):
                if i == row and j == col:
                    lis.append(s[row-1][col-1])
        t -= 1
    for i in lis:
        print(i)
number_spiral(s)



"""
>>> %Run -c $EDITOR_CONTENT
3
2 3
1 1
4 2
8
1
15
>>> 
"""
