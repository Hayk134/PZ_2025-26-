'''
Вариант 30
Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой организации.
БД должна содержать таблицу Торговая точка со следующей структурой записи: этаж, площадь,
наличие кондиционера и стоимость аренды в день.
'''

import sqlite3

DB_NAME = "rental_spaces.db"

# Инициализация базы данных и создание таблицы
with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS retail_outlets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            floor INTEGER, 
            area REAL, 
            has_ac TEXT, 
            daily_rent REAL
        )
    """)

    # Очистка и заполнение начальными данными (для теста)
    cursor.execute("DELETE FROM retail_outlets")
    initial_data = [
        (1, 45.5, "Да", 1500), (1, 120.0, "Да", 3500), (1, 25.0, "Нет", 900),
        (2, 60.0, "Да", 1800), (2, 35.0, "Нет", 1100), (2, 85.0, "Да", 2400),
        (3, 15.0, "Нет", 500), (3, 50.0, "Да", 1400), (3, 110.0, "Да", 3000),
        (4, 75.0, "Да", 2000)
    ]
    cursor.executemany("INSERT INTO retail_outlets (floor, area, has_ac, daily_rent) VALUES (?, ?, ?, ?)", initial_data)
    conn.commit()


def show_all(title="Список всех точек"):
    """Отображает все записи в таблице"""
    print(f"\n=== {title} ===")
    print(f"{'ID':<4} | {'Этаж':<4} | {'Площадь':<8} | {'Конд.':<5} | {'Цена/день':<10}")
    print("-" * 45)
    with sqlite3.connect(DB_NAME) as conn:
        for r in conn.execute("SELECT * FROM retail_outlets"):
            print(f"{r[0]:<4} | {r[1]:<4} | {r[2]:<8} | {r[3]:<5} | {r[4]:<10}")
    print("-" * 45)


def print_search(rows):
    """Вспомогательная функция для вывода результатов поиска"""
    if not rows:
        print("\nЗаписи не найдены!")
        return
    print(f"\n{'ID':<4} | {'Этаж':<4} | {'Площадь':<8} | {'Конд.':<5} | {'Цена/день':<10}")
    print("-" * 45)
    for r in rows:
        print(f"{r[0]:<4} | {r[1]:<4} | {r[2]:<8} | {r[3]:<5} | {r[4]:<10}")


# Главный цикл меню
while True:
    print("\n      --- МЕНЮ УПРАВЛЕНИЯ ---")
    print("1. Показать все записи")
    print("2. Добавить новую торговую точку")
    print("3. Поиск: по этажу")
    print("4. Поиск: без кондиционера")
    print("5. Поиск: дешевле указанной цены")
    print("6. Редактировать: изменить цену по ID")
    print("7. Редактировать: наличие конд. для всего этажа")
    print("8. Редактировать: скидка 10% на площади > 100 кв.м")
    print("9. Удалить: по конкретному ID")
    print("10. Удалить: точки с ценой ниже указанной")
    print("0. Выход")

    choice = input("\nВыберите действие (введите цифру): ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        if choice == "1":
            show_all()

        elif choice == "2":
            fl = int(input("Введите этаж: "))
            ar = float(input("Введите площадь (кв.м): "))
            ac = input("Есть кондиционер (Да/Нет): ")
            pr = float(input("Дневная аренда: "))
            cursor.execute("INSERT INTO retail_outlets (floor, area, has_ac, daily_rent) VALUES (?, ?, ?, ?)",
                           (fl, ar, ac, pr))
            conn.commit()
            print("[Запись успешно добавлена]")

        elif choice == "3":
            fl = int(input("Введите номер этажа: "))
            res = cursor.execute("SELECT * FROM retail_outlets WHERE floor = ?", (fl,)).fetchall()
            print_search(res)

        elif choice == "4":
            res = cursor.execute("SELECT * FROM retail_outlets WHERE has_ac = 'Нет'").fetchall()
            print_search(res)

        elif choice == "5":
            max_p = float(input("Максимальная цена аренды: "))
            res = cursor.execute("SELECT * FROM retail_outlets WHERE daily_rent <= ?", (max_p,)).fetchall()
            print_search(res)

        elif choice == "6":
            idx = int(input("Введите ID точки для изменения цены: "))
            new_price = float(input("Введите новую цену: "))
            cursor.execute("UPDATE retail_outlets SET daily_rent = ? WHERE id = ?", (new_price, idx))
            conn.commit()
            print(f"[Цена для ID {idx} обновлена]")

        elif choice == "7":
            fl = int(input("Для какого этажа изменить статус кондиционера: "))
            status = input("Новый статус (Да/Нет): ")
            cursor.execute("UPDATE retail_outlets SET has_ac = ? WHERE floor = ?", (status, fl))
            conn.commit()
            print(f"[Статус кондиционеров на {fl} этаже изменен]")

        elif choice == "8":
            cursor.execute("UPDATE retail_outlets SET daily_rent = daily_rent * 0.9 WHERE area > 100")
            conn.commit()
            print("[Скидка 10% применена ко всем объектам площадью более 100 кв.м]")

        elif choice == "9":
            idx = int(input("Введите ID для удаления: "))
            cursor.execute("DELETE FROM retail_outlets WHERE id = ?", (idx,))
            conn.commit()
            print(f"[Запись ID {idx} удалена]")

        elif choice == "10":
            min_p = float(input("Удалить все точки с ценой ниже: "))
            cursor.execute("DELETE FROM retail_outlets WHERE daily_rent < ?", (min_p,))
            conn.commit()
            print(f"[Записи с ценой ниже {min_p} удалены]")

        else:
            print("Неверный ввод, попробуйте еще раз.")