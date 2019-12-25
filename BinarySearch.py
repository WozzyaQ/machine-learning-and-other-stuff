from __future__ import annotations


def binary_search(arr: list, key: int) -> int:
    if arr:
        left: int = 0
        right: int = len(arr)
        while left < right:
            middle: int = (left+right)//2
            if arr[middle] > key:
                right = middle
            else:
                left = middle + 1

        return left - 1
    else:
        return -1


a: list = [item for item in range(10000)]
print(binary_search(a, 20))
