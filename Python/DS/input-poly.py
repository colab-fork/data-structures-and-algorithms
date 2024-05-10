x, k = map(int, input().split())
poly = input()
result = eval(poly.replace('x', str(x)))
print(result == k)
