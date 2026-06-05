'''
1. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
'''

matrix = [
    [5,  12,  3],
    [18,  7, 10],
    [1,  25,  8]
]


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

for row in matrix:
    print(row)