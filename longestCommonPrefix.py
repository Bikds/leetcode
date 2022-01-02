def longestCommonPrefix(input):
    if input == []:
        return ""
    first_word = input[0]
    common_pref = ""

    for j in range(0, len(first_word)):
        for elem in input:
            if common_pref + first_word[j] != elem[0:j+1]:
                return common_pref
        common_pref += first_word[j]

    return common_pref

print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "cat", "mouse"]))
print(longestCommonPrefix([]))
print(longestCommonPrefix(["c", "acc", "cac"]))