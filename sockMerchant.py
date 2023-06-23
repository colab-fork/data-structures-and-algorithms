n =9
ar  = [1, 2, 1, 2, 1, 3, 2]

def sockMerchant(n ,ar):
  from collections import Counter
    counts = Counter(ar)
    lis = []
    j = 0
    for key, value in counts.items():
        lis.appenåd(value)
    for i in lis:
        if i > 1:
            j += i // 2
    return j
    
    
sockMerchant(n, ar)



"""
>>> %Run -c $EDITOR_CONTENT
2
"""
