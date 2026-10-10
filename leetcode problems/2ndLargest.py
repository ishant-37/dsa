def sec_largest(arr):

    largest = float("-inf")
    s_largest = float("-inf")
    n = len(arr)

    for i in range (0, n):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]

        elif arr[i] > s_largest and arr[i] != largest:
            s_largest = arr[i]
    return s_largest

arr = [4, 1, 7, 6, 3, 2, -8]
print(arr)
print(sec_largest(arr))