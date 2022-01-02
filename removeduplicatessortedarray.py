

def removeDuplicates(nums) -> int:
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] in nums[j:i]:
            nums.pop(i)
        else:
            j = i
            i+=1
    return (nums)


    # for i in range(len(nums)):
    #     if nums[i] in nums[0:i]:
    #         duplicates += 1
    # print(len(nums) - duplicates)
    # return len(nums) - duplicates

nums = [0,1,1,2,3,3,4]
print(removeDuplicates(nums))

nums = [1,1]
print(removeDuplicates(nums))