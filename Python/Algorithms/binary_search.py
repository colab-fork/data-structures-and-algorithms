# Searching algorithm that operates on a sorted array.
# We divide the search interval in half, until the value is found or the interval is empty.

def binary_search(arr, target):
    low = 0
    high  = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 5))

"""
 %Run main.py
2
>>> 

"""
