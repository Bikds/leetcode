def maxSubArray(nums):
    curr_max = nums[0]
    temp_sum = nums[0]

    for i in range(1, len(nums)):
        if temp_sum > 0:
            temp_sum += nums[i]
        else:
            temp_sum = nums[i]
        curr_max = max(temp_sum, curr_max)
    return curr_max