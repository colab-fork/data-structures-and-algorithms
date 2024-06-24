"""
Check if pair with the given Sum exists in Array:
 Given an array, determine if there is a pair of elements that sum up to a 
 specific target value.
"""

def CheckSumExists(array, check):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] + array[j] == check:
                return True
    return False

print(CheckSumExists(array, check))
