import math


def binary_search(l, i):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = math.floor((low + high) / 2)
        guess = l[mid]
        if guess == i:
            return mid
        if guess > i:
            high = mid - 1
        else:
            low = mid + 1
    return

