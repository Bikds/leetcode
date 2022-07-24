from collections import defaultdict


def isAnagram(s: str, t: str):
    # for c in s:
    #     if c in t:
    #         t = t.replace(c, "", 1)
    #     else:
    #         return False
    # return t == ""

    # a = defaultdict(int)
    # b = defaultdict(int)
    #
    # for c in s:
    #     a[c] += 1
    # for c in t:
    #     b[c] += 1
    #
    # return a == b

    a = defaultdict(int)

    for c in s:
        a[c] += 1
    for c in t:
        a[c] -= 1

    return all(x == 0 for x in a.values())
    # for c in a.keys():
    #     if a[c] != 0:
    #         return False
    # return True

if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram") == True)
    print(isAnagram("rat", "car") == False)
    print(isAnagram("ab", "a") == False)