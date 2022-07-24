def removeDuplicates(nums) -> int:
    i = 0
    # iterate through the list
    for j in range(0, len(nums)):
        # if j is on a new value
        if nums[i] != nums[j]:
            # increment i to the next position to be filled
            i += 1
            # fill i
            nums[i] = nums[j]
    # i is zero indexed so return one more than i
    return i+1





if __name__ == "__main__":
    print(removeDuplicates([1, 1, 2, 3, 3, 4, 4, 4, 5, 5]) == 5)
    print(removeDuplicates([1, 2]) == 2)
    print(removeDuplicates([1]) == 1)
    print(removeDuplicates([1, 2, 2, 3]) == 3)