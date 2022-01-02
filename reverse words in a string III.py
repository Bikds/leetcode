

def reverseWords(s):
    l = s.split()

    for i in range(len(l)):
        word = l[i]
        new_word = ""
        for j in range(len(word) - 1, -1, -1):
            new_word += word[j]
        l[i] = new_word

    return ' '.join(l)

print(reverseWords("Let's take LeetCode contest"))

