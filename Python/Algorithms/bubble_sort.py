def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 35, 55, 11, 2, 4]))

"""
>>> %Run main.py
[2, 4, 11, 35, 55, 64]

"""
