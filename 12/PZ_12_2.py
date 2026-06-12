'''
2. В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
'''
from hashlib import new

matrix = [
    [2,  3,  4],
    [5,  6,  7],
    [8,  9,  1]
]


new_matrix = [
    [matrix[i][j] * 2 if i != j else matrix[i][j] for j in range(len(matrix[i]))]
    for i in range(len(matrix))
]

for row in new_matrix:
    print(row)