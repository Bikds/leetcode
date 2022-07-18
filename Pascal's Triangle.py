def generate(numRows):
    pt = []
    for i in range(1, numRows+1):
        pt.append([1] * i)
        for j in range(1, i-1):
            pt[i - 1][j] = pt[i - 2][j - 1] + pt[i - 2][j]
    return pt
    # pt = []
    # for i in range(1, numRows+1):
    #     if i < 2:
    #         pt.append([1] * i)
    #     else:
    #         # sum of your index and your index - 1
    #         temp = []
    #         for j in range(i):
    #             if j == 0 or j == i-1:
    #                 temp.append(1)
    #             else:
    #                 temp.append(pt[i-2][j-1] + pt[i-2][j])
    #         pt.append(temp)
    # return pt



if __name__ == "__main__":
    print(generate(1))
    print(generate(2))
    print(generate(3))
    print(generate(4))
    print(generate(5))