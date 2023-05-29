lst = [2,1, 5, 3, 4]
def BubbleSort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
    
"""
>>> BubbleSort(lst)
[1, 2, 3, 4, 5]
>>>  
    
"""
