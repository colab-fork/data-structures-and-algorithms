"""
1 2 3
4 5 6
6 9 8

"""
# 2d infinite matrix
#s = [[1, 3, 4, 5], [3, 5, 6, 7], [2, 4, 5, 6], [4, 5, 6, 6]] 

def number_spiral(s):
    t = int(input())
    for i in range(t):
        y, x = list(map(int(input().split()))) # 4 , 5
        row = y
        col = x
        for i in range(row+1):
            for j in range(col+1):
                if i == row and j == col:
                    print(s[i][j])
number_spiral(s)

"""
>>> %Run -c $EDITOR_CONTENT
2 3
6  // for each test case
>>> 

"""
