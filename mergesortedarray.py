def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # nums1[m:] = nums2
    # nums1.sort()

    # Approach is to insert elements starting at the end of nums1
    idx = m + n - 1
    i = m - 1
    j = n - 1

    while i > -1 and j > -1:
        if nums1[i] > nums2[j]:
            nums1[idx] = nums1[i]
            i -= 1
        else:
            nums1[idx] = nums2[j]
            j -= 1
        idx -= 1

    while i > -1:
        nums1[idx] = nums1[i]
        idx -= 1
        i -= 1
    while j > -1:
        nums1[idx] = nums2[j]
        idx -= 1
        j -= 1

    print(nums1)


if __name__ == "__main__":
    merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    merge([1], 1, [], 0)
    merge([0], 0, [1], 1)
    merge([2, 0], 1, [1], 1)