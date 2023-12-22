# dynamic programming -> used to solve optimization promblems by breaking them down into smaller subproblems. 

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(10))
        
"""
>>> %Run -c $EDITOR_CONTENT
[0, 1, 1, 2, 3, 5]
>>> 
"""
