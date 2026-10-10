def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j] > key: 
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def printarr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [3, 5, 6, 4, 8, 9, 10, 7, 1]
    print("Original Array: ", printarr(arr))
    insertion_sort(arr)
    print("Sorted Array: ",printarr(arr))

    