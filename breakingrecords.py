scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

def breakingRecords(scores):
    # Write your code here
    mi = scores[0]
    ma = scores[0]
    count = [0, 0]
    for i in scores:
        if i < mi:
            count[1] +=1
            mi = i
        elif i > ma:
            count[0] += 1
            ma = i
            print(mi)
            print(count)
    return count

breakingRecords(scores)
"""
[4, 0]
"""
