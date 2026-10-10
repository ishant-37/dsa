arr = [3,4,5,1,3,9,7,8,6]

left=2
right=len(arr)-1
def funct(nums, left, right):
    if left>=right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    funct(nums, left+1, right-1)

funct(arr, 0, 8)

print(arr)