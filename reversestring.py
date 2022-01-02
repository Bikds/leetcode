def reverseString(s):
    beg = 0
    end = len(s) - 1

    while (beg < end):
        temp = s[end]
        s[end] = s[beg]
        s[beg] = temp

        beg += 1
        end -= 1
    return s

print(reverseString("hello"))