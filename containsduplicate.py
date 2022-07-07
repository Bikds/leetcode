def containsDuplicate(nums):
    n = set()
    for elem in nums:
        if elem in n:
            return True
        else:
            n.add(elem)
    return False
