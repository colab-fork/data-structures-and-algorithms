n = 6
k =3
ar = [1, 3, 2, 6, 1, 2]
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[i] < ar[j] and (ar[i] + ar[j]) % k == 0:
                count += 1
    print(count)
divisibleSumPairs(n, k, ar)

"""
>>> %Run -c $EDITOR_CONTENT
5

"""
