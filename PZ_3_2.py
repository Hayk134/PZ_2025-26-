def find_closest_point_while(a_coord, b_coord, c_coord):
    """
    Определяет ближайшую к A точку (B или C), 
    используя цикл while (выполняется 1 раз).
    """
    closest_point = ""
    min_distance = 0
    
    # Искусственное использование цикла while для однократного выполнения
    while True:
        # Вычисляем расстояние от A до B
        distance_ab = abs(a_coord - b_coord)

        # Вычисляем расстояние от A до C
        distance_ac = abs(a_coord - c_coord)

        # Сравниваем расстояния
        if distance_ab <= distance_ac:
            closest_point = 'B'
            min_distance = distance_ab
        else:
            closest_point = 'C'
            min_distance = distance_ac
            
        # Прерываем цикл, так как расчет завершен
        break

    print(f"Координаты: A={a_coord}, B={b_coord}, C={c_coord}")
    print(f"Ближайшая точка к A: {closest_point}")
    print(f"Расстояние от A до ближайшей точки: {min_distance}")

# Пример использования
a, b, c = 10, 0, 8
find_closest_point_while(a, b, c)
