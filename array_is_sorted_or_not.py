def sorted_arr(nums):
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
nums = nums = [3,6,2,1,4,7,]
print(sorted_arr(nums))