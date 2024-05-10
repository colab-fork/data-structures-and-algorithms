def primeNotprime(t):
    lis = []
    for i in range(1,t+1):
        if t%i == 0:
            lis.append(i)
    if len(lis) > 2:
        print('Not Prime')
        
    else:
        print('Prime')
        
        
        
t = int(input())
primeNotprime(t)

"""
>>> %Run -c $EDITOR_CONTENT
97
Prime

"""
