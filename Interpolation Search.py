"""
Interpolation Search
is the improvement of binary search,
it works well in uniformly distributed array

pos = low + (((high - low) / arr[high] - arr[low]) * (target - arr[low]))

a. if target = arr[pos
    return pos
b. if target > arr[pos
    low = pos + 1
    count pos
    check
c. if target < arr[pos
    high = pos - 1
    count pos
    check
"""

import math

def interpolationSearch(arr, arr_length, target):
    low = 0
    high = arr_length - 1

    while (low <= high and target >= arr[low] and target <= arr[high]):

        # Last comparison, if it doesn't match,
        # so the target is not in the array
        if (low == high):
            if (target == arr[low]):
                return low
            return -1
        
        # Count the probe position
        pos = math.floor(low + (((high - low) / (arr[high] - arr[low])) * (target - arr[low])))

        # If match
        if (target == arr[pos]):
            return pos

        # If target is higher, so look for the higher part
        elif (target > arr[pos]):
            low = pos + 1

        # If target is lower, so look for the lower part
        else:
            high = pos - 1
        
    return -1

def main():
    arr = [1, 3, 5, 8, 10, 12, 15]
    target = 12
    result = interpolationSearch(arr, len(arr), target)

    if (result == -1):
        print('Target is not found!')
    else:
        print('Target is found at index ' + str(result))

main()
