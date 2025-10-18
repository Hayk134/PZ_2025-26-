def check_point_in_rectangle_while(x, y, x1, y1, x2, y2):
"""
    Проверяет, лежит ли точка (x, y) строго внутри прямоугольника,
    используя цикл while (выполняется 1 раз).
    """
is_inside = False

# Искусственное использование цикла while для однократного выполнения
while True:
# Условие по оси X: x между x1 (левая) и x2 (правая)
is_x_inside = (x1 < x < x2)

# Условие по оси Y: y между y2 (нижняя) и y1 (верхняя)
is_y_inside = (y2 < y < y1)

is_inside = is_x_inside and is_y_inside

# Прерываем цикл, так как расчет завершен
break

return is_inside

# Пример использования
x, y = 3, 3 # Проверяемая точка
x1, y1 = 1, 5 # Левая верхняя
x2, y2 = 5, 1 # Правая нижняя

result = check_point_in_rectangle_while(x, y, x1, y1, x2, y2)
print(f"Точка ( {
    x
}, {
    y
}) внутри прямоугольника: {
    result
}")