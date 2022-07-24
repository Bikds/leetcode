import collections
from collections import defaultdict


def canConstruct(ransomNote: str, magazine: str):
    # chars = defaultdict(int)
    #
    # for c in magazine:
    #     chars[c] += 1
    # for c in ransomNote:
    #     if chars[c] > 0:
    #         chars[c] -= 1
    #     else:
    #         return False
    # return True

    # queue = []
    #
    # for c in ransomNote:
    #     queue.append(c)
    # for c in magazine:
    #     if c in queue:
    #         queue.remove(c)
    #     if len(queue) == 0:
    #         return True
    # return False

    # for c in ransomNote:
    #     if c in magazine:
    #         magazine = magazine.replace(c, "", 1)
    #     else:
    #         return False
    # return True

    # print(collections.Counter(ransomNote) - collections.Counter(magazine))

    return not collections.Counter(ransomNote) - collections.Counter(magazine)






if __name__ == "__main__":
    print(canConstruct("a", "b") == False)
    print(canConstruct("aa", "ab") == False)
    print(canConstruct("aa", "aab") == True)
