from collections import defaultdict


# 1 way: sort both arrays, and iterate through O(m+n log (m+n))
# dictionary with count of key and number, then compare keys and take min to make list O(m+n)

def intersect(nums1, nums2):

    # nums1.sort()
    # nums2.sort()
    #
    # ptr1 = ptr2 = 0
    #
    # inter = []
    #
    # while (ptr1 < len(nums1) and ptr2 < len(nums2)):
    #     if nums1[ptr1] < nums2[ptr2]:
    #         ptr1+=1
    #     elif nums1[ptr1] > nums2[ptr2]:
    #         ptr2+=1
    #     else:
    #         inter.append(nums1[ptr1])
    #         ptr1+=1
    #         ptr2+=1
    # return inter

    count1 = defaultdict(int)
    count2 = defaultdict(int)

    for num in nums1:
        count1[num] += 1
    for num in nums2:
        count2[num] += 1

    intersect = []

    for key in count1.keys():
        if key in count2.keys():
            for _ in range(min(count1[key], count2[key])):
                intersect.append(key)
    return intersect


if __name__ == "__main__":
    print(intersect([1,2,2,1], [2,2]))
    print(intersect([4,9,5], [9,4,9,8,4]))