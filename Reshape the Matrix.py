def matrixReshape(mat, r, c):

    if (len(mat) == r and len(mat[0]) == c) or (r * c != len(mat) * len(mat[0])):
        return mat

    newmat = [[None for _ in range(c)] for _ in range(r)]
    x = 0
    y = 0

    for i in range(r):
        for j in range(c):
            if y < len(mat[0]):
                newmat[i][j] = mat[x][y]
                y += 1
            elif y >= len(mat[0]):
                x += 1
                if x == len(mat):
                    print("here")
                    return newmat
                y = 1
                newmat[i][j] = mat[x][0]
    return newmat


if __name__ == "__main__":
    print(matrixReshape([[1, 2], [3, 4]], 1, 4))
    print(matrixReshape([[1, 2], [3, 4]], 4, 1))
    print(matrixReshape([[1, 2], [3, 4]], 2, 2))
