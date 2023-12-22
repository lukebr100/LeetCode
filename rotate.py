# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix):
    m = len(matrix)
    k = 1
    for i in range(m):
        for j in range(k, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        k = k + 1
    for i in range(m):
        for j in range(math.floor(m / 2)):
            t = matrix[i][j]
            matrix[i][j] = matrix[i][-(j+1)]
            matrix[i][-(j+1)] = t
    return matrix
