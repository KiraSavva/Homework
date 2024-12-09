def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[i].append(value)
    return matrix
print(get_matrix(3,5,42))




