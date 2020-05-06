"""
Binary Search

1.  Look for the mid of the array
    Mid = Floor(Low + (High - Low) / 2)
2.  a. If mid matches the target,
        return mid
    b. If target < mid,
        High = mid - 1
    c. If target > mid,
        Low = mid + 1
"""

import math

def binarySearch(target, arr, low, high):
    while (low <= high):
        mid = math.floor(low + (high - low) / 2)
        if (target == arr[mid]):
            return mid
        elif (target < arr[mid]):
            high = mid - 1
            binarySearch(target, arr, low, high)
        else:
            low = mid + 1
            binarySearch(target, arr, low, high)
    return -1

def main():
    arr = [2, 3, 10, 17, 19, 23]
    target = 19
    result = binarySearch(target, arr, 0, len(arr) - 1)

    if (result != -1):
        print("Target is found at index " + str(result))
    else:
        print("Target is not found!")

main()
    
