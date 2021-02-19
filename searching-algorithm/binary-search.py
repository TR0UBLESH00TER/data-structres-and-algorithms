# Binary Search - Sorted Array

def search(Array,Element):
    """Binary Search Algorithm implemented in Python3"""
    high, low = len(Array)-1, 0
    while low <= high:
        mid = (low+high)//2
        if Array[mid]==Element:
            return mid
        elif Array[mid] < Element:
            low = mid + 1
        else:
            high = mid - 1
    return -1