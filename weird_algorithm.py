# 3 - 10 - 5 - 16 - 8 - 4 - 2 - 1
ls =[]
def weird_algorithm(num):
    if num % 2 != 0 and num != 1:
        ls.append(num)
        num = num * 3 + 1
        weird_algorithm(num)
    elif num % 2 == 0 and num != 1:
        ls.append(num)
        num //= 2
        weird_algorithm(num)
    else:
        ls.append(1)
    return ls

num = int(input())
ans = print(weird_algorithm(num))

"""
>>> %Run main.py
3
[3, 10, 5, 16, 8, 4, 2, 1]
>>> 
"""
