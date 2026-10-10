arr = [5, 1, 6, 8, 2, 4, 9] 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):  # i will initially on second last element. at element 4, which is on n-2
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                # for sorting descending condition will: "if arr[j] < arr[j+1]:"
                arr[j], arr[j+1] = arr[j+1], arr[j]

def print_array(arr):
    for value in arr:
        print(value, end=" ")
    print()

print("Original Array: ", end=" ")
print_array(arr)

bubble_sort(arr)

print("Sorted Array: ", end=" ")
print_array(arr)