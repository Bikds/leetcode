def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    new_num = "1"

    for i in range(1, n):
        temp = ""
        i = 0
        j = 0
        while j <= len(new_num):
            if (j == len(new_num)) or (new_num[i] != new_num[j]):
                temp += str(j - i) + new_num[i]
                i = j

            j += 1

        new_num = temp

    return new_num

print("1: ", countAndSay(1))
print("2: ", countAndSay(2))
print("3: ", countAndSay(3))
print("4: ", countAndSay(4))
print("5: ", countAndSay(5))