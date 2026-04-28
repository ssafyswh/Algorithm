def mult_sqr_matrix(size, mat1, mat2):
    result_mat = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            val = 0
            for i in range(size):
                val += mat1[row][i] * mat2[i][col]
            result_mat[row][col] = val % 1000
    return result_mat

def divide(mat, count):
    if count == 1:
        return mat
    elif count == 2:
        return mult_sqr_matrix(N, mat, mat)
    temp_mat = divide(mat, count // 2)
    if count % 2:
        return mult_sqr_matrix(N, mult_sqr_matrix(N, temp_mat, temp_mat), mat)
    else:
        return mult_sqr_matrix(N, temp_mat, temp_mat)

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [row[:] for row in matrix]
result = divide(matrix, B)
for r in range(N):
    for c in range(N):
        result[r][c] = result[r][c] % 1000
for row in result:
    print(*row)