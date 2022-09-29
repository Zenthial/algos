def matrix_partition(matrix):
    return matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

# can use the naive algo since it involves less multiplications if we know its a 2x2 matrix
def matrix_multiplication(mat1, mat2):
    a11, a12, a21, a22 = matrix_partition(mat1)
    b11, b12, b21, b22 = matrix_partition(mat2)
    return [[a11 * b11 + a12 * b21, a11 * b12 + a12 * b22], [a21 * b11 + a22 * b21, a21 * b12 + a22 * b22]]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    elif n == 0:
        return [[0,0], [0,0]]
    else:
        new_matrix = matrix_power(matrix, n // 2)
        if n % 2 == 0:
            return matrix_multiplication(new_matrix, new_matrix)
        else:
            return matrix_multiplication(matrix_multiplication(new_matrix, new_matrix), matrix)


# L is a matrix
def fibPow(n):
    l_matrix = [[1, 1], [1, 0]]
    ret_matrix = matrix_power(l_matrix, n)
    return ret_matrix[0][1]

for i in range(10):
    print(fibPow(i))