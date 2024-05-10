def fibonacci(num):
    x , y = 0, 1
    z = x + y
    print(x)
    print(y)
    while z <= num:
        print(z)
        x, y =  y, x+y
        z = x + y
    return
    
n = int(input())
fibonacci(n)

"""
>>> %Run -c $EDITOR_CONTENT
100
0
1
1
2
3
5
8
13
21
34
55
89

"""
