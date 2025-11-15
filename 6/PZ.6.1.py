'''
1. Дан список А размера № и целое число К (1 < К< ). Преобразовать список, увеличив каждый его элемент на исходное значение элемента K.
'''


def task(A, K):
   
    value = A[K - 1]
    return [x + value for x in A]


A = [random.randit(1, 20) for _ in range(10)]
K = 4
result = task(A, K)

print(f"исходное {A}, k {K}, значение A[K]: {A[K-1]}")
print(f"{result}")
