# A C G T
# longest repetition


def repetitions():
    s = input()
    lis = ['A', 'C', 'T', 'G']
    ls = []
    count = 0
    for i in range(len(s)):
        c = s[i]
        for j in range(i, len(s)):
            if s[j] == c:
                count += 1
            else:
                break
        ls.append(count)
        count = 0
    print(max(ls))

repetitions()
        
"""
>>> %Run -c $EDITOR_CONTENT
ATTCGGGA
3
>>> 
"""
