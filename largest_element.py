nums = [55,35,78,9,90]
largest=nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i]>largest:
        largest = nums[i]
print(largest)