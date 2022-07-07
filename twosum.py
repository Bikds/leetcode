def twoSum(nums, target):
    d = {}

    if len(nums) == 2:
        return [0, 1]

    for i in range(len(nums)):
        opp = target - nums[i]
        if opp in d:
            return [i, d[opp]]
        else:
            d[nums[i]] = i