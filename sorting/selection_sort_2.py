# arr = [5,1,6,8,9,4]

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[min_idx]:
                min_idx=j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

# arr = list(map(int, input("Enter array: ").split()))
arr = [5,1,6,8,9,4]

print("Original Array: ", end="")
print_array(arr)

selection_sort(arr)


print("Sorted Array: ", end="")
print_array(arr)