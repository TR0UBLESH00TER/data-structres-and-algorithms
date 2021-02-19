# Linear Search - Sorted Array

def search(Array,Element):
    """Linear Search Algorithm implemented in Python3"""
    for i in range(0,len(Array)):
        if Array[i] == Element:
            return i
    return -1