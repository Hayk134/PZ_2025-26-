def swap(x, y):
    return x, y
A = 10.4
B = 23.6
C = 17.5
D = 19.5
#исходные значения
print(f"A = {A}, B = {B}, C = {C}, D = {D}")
#последовательный обмен
B, A = swap(A, B)
D, C = swap(C, D)
C, B = swap(B, C)
#применяем новые значения
print(f"A = {A},B = {B},C = {C},D =
