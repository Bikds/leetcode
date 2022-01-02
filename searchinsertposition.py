
#
# def searchInsert(nums, target: int) -> int:
#
#     arr_size = len(nums)
#     if target in nums:
#         return nums.index(target)
#     i = 0
#     while i < arr_size:
#         if nums[i] > target:
#             break
#         i += 1
#     return i

def searchInsert(nums, target: int) -> int:

    if target in nums:
        return nums.index(target)
    nums.append(target)
    nums.sort()
    return nums.index(target)

n1 = [1, 3, 5, 6]
# print(searchInsert(n1, 1))
print(searchInsert(n1, 2))
n1 = [1, 3, 5, 6]
print(searchInsert(n1, 4))
# print(searchInsert(n1, 6))
# print(searchInsert(n1, 7))