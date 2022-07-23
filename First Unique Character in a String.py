from collections import defaultdict


def firstUniqChar(s):
    m = defaultdict(int)

    for c in s:
        m[c] += 1  # increment count of the character by 1

    for i in range(len(s)):
        if m[s[i]] == 1:
            return i
    return -1

    # m = defaultdict(int)
    # curr_idx = 0
    #
    # for c in s:
    #     m[c] += 1   # increment count of the character by 1
    #
    #     # check and make sure that curr_idx is still a valid entry
    #     if m[c] > 1:
    #         while m[s[curr_idx]] > 1:
    #             curr_idx += 1
    #             if curr_idx >= len(s):
    #                 return -1
    # if m[curr_idx] > 1:
    #     return -1
    # return curr_idx




if __name__ == "__main__":
    print(firstUniqChar("leetcode") == 0)
    print(firstUniqChar("loveleetcode") == 2)
    print(firstUniqChar("aabb") == -1)
    print(firstUniqChar("aabbc") == 4)
    print(firstUniqChar("a") == 0)
    print(firstUniqChar("aadadaad") == -1)