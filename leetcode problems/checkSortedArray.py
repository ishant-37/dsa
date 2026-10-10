def isSorted(arr):

    n = len(arr)

    for i in range (0, n-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True
    
# arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
arr = [1, 1, 2, 2, 3, 4, 4, 5, 6]

print(isSorted(arr))