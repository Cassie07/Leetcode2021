def binary_search(low, high, arr, target):

    mid = low + (high-low)/2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(mid + 1, high, arr, target)
    else:
        return binary_search(low, mid - 1, arr, target)
