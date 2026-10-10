def merge_array(left, right):
  # left = [1 2 3 4]
  # right = [1 1 3 4 5 6 7]
    i,j=0,0
    results = []
    n = len(left)
    m = len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            results.append(left[i])
            i+=1
        else:
            results.append(right[j])
            j+=1
    # Add remaining elements form Left
    if i<n:
        while i<n:
            results.append(left[i])
            i+=1
    # Add remaining elements form right
    if j<m:
        while j<m:
            results.append(right[j])
            j+=1
    return results

def merge_sort(arr):
    
    # base case
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left, right)

arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]

print("Original Array: ", arr)
print("Sorted Array: ", merge_sort(arr))