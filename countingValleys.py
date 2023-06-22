path = 'DDUUDDUDUUUD'
steps= len(path)
def countingValleys(steps, path):
    base = 0
    lis = []
    for i in path:
        if i == 'U':
            base += 1
        else:
            base -= 1
        lis.append(base)
    count = 0
    for i in range(len(lis)- 1):
        if lis[i] == -1 and lis[i+1] == 0:
            for j in range(i, len(lis)):
                if lis[j] == 0:
                    count += 1
                    break
    print(count)
countingValleys(steps, path)

"""
_/\      _
   \    /
    \/\/
>>> %Run -c $EDITOR_CONTENT
2
>>> 
"""
