arr = [3,4,5,1,3,9,7,8,6]

def funct(nums, left, right):
    if left>=right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    funct(nums, left+1, right-1)

funct(arr, 2, 7)

print(arr)


arr = [3,4,5,1,3,9,7,8,6]

left = 0
right = len(arr)-1

