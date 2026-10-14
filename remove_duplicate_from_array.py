def duplicate(nums):
    dict = {}
    n = len(nums)
    for i in range(0,n):
        dict[nums[i]]=0
    j =0
    for k in dict:
        nums[j]=k
        j+=1
    return j
nums = [1,1,1,2,4,5,5,7,6,9,8,9]
print(duplicate(nums))
        