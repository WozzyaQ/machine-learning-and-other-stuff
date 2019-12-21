from __future__ import annotations


def fibonacci_recursive(n: int):
    if n < 0:
        return -1
    if n == 0:
        return 1
    if n == 1:
        return 1

    return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)


def fibonacci_iterative(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a: int = 1
        b: int = 1
        result: int = 0
        for i in range(n-1):
            result = a + b
            a = b
            b = result
        return result

