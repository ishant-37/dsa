# arr = [4 1 7 6 3 2 8]

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high-1:
            i+=1

        while arr[j] > pivot and j >= low+1:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

def quick_sort(arr, low, high):

    if low < high:
        p_idx = partition(arr, low, high)
        quick_sort = (arr, low, p_idx-1)
        quick_sort = (arr, p_idx+1, high)


arr = list(map(int, input ("Enter array: ").split()))

print( "Original array: ", arr)
quick_sort(arr, 0, len(arr)-1)
print( "Sorted array: ", arr)