'''
1. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
'''

matrix = [
    [5,  12,  3],
    [18,  7, 10],
    [1,  25,  8]
]
zero_matrix = [[0 if x > 10 else x for x in row] for row in matrix]


for row in zero_matrix:
    print(row)