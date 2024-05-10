from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for i, el in enumerate(a, 1):
    d[el].append(i)
for el in b:
    print(' '.join(map(str, d[el])) if d[el] else '-1')


"""
5 2
a
a
b
a
b
a
b


Expected Output
1 2 4
3 5

"""
