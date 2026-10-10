def largestElement(arr):
    largest = arr[0]
    n = len(arr)

    for i in range(0,n):
        if arr[i]>largest:
            largest = arr[i]
    return largest

arr = [4, 1, 7, 6, 3, 2, -8]
print(largestElement(arr))
