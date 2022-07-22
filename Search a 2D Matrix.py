def searchMatrix(matrix, target):
    row = 0
    # first find the correct row
    for i in range(len(matrix) - 1):
        if matrix[i][0] <= target < matrix[i + 1][0]:
            break
        row += 1

    low = 0
    high = len(matrix) - 1
    i = 0
    while low <= high:
        i = (low + high) // 2
        if matrix[i][0] <= target <= matrix[i][len(matrix[0]) - 1]:
            break
        elif matrix[i][0] > target:
            high = i - 1
        else:
            low = i + 1
    low = 0
    high = len(matrix[0]) - 1
    j = (low + high) // 2
    while low <= high:
        if matrix[i][j] < target:
            low = j + 1
        elif matrix[i][j] > target:
            high = j - 1
        else:
            return True
        j = (low + high) // 2
    return False


    # row = 0
    # # first find the correct row
    # for i in range(len(matrix) - 1):
    #     if matrix[i][0] <= target < matrix[i + 1][0]:
    #         break
    #     row += 1
    #
    # # then find the correct column
    # for j in range(len(matrix[row])):
    #     if matrix[row][j] == target:
    #         return True
    # return False

if __name__ == "__main__":
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True)
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False)
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34) == True)
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 359) == False)
    print(searchMatrix([[1]], 1) == True)
    print(searchMatrix([[1], [3], [5]], 3) == True)


