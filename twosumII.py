def twoSum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 <= p2:

        if numbers[p1] + numbers[p2] == target:
            return [p1 + 1, p2 + 1]
        elif numbers[p1] + numbers[p2] > target:
            p2 -= 1
        else:
            p1 += 1


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))
