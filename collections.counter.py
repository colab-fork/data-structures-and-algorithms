from collections import Counter
X = int(input())
sizes = list(map(int,input().split()))
profit = []
N = int(input())
for i in range(N):
    s, x = map(int, input().split())
    if s in sizes:
        if Counter(sizes).get(s) > 0:
            profit.append(x)
            sizes.remove(s)
    else:
        continue
print(sum(profit))
 """
 >>> %Run -c $EDITOR_CONTENT
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
200
>>> 
 
 """
