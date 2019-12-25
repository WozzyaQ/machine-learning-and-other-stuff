from __future__ import annotations


def binary_search(arr, key):
    if arr:
        left = 0
        right = len(arr)
        while left < right:
            middle = (left+right)//2
            if arr[middle] > key:
                right = middle
            else:
                left = middle + 1

        return left - 1
    else:
        return -1


a = [item for item in range(10000)]
print(binary_search(a,20))
