import sqlite3

DB_NAME = "rental_spaces.db"


with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS retail_outlets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            floor INTEGER, area REAL, has_ac TEXT, daily_rent REAL
        )
    """)

    cursor.execute("DELETE FROM retail_outlets")
    initial_data = [
        (1, 45.5, "Да", 1500), (1, 120.0, "Да", 3500), (1, 25.0, "Нет", 900),
        (2, 60.0, "Да", 1800), (2, 35.0, "Нет", 1100), (2, 85.0, "Да", 2400),
        (3, 15.0, "Нет", 500), (3, 50.0, "Да", 1400), (3, 110.0, "Да", 3000),
        (4, 75.0, "Да", 2000)
    ]
    cursor.executemany("INSERT INTO retail_outlets (floor, area, has_ac, daily_rent) VALUES (?, ?, ?, ?)", initial_data)
    conn.commit()


def show_all(title="ТЕКУЩИЕ ДАННЫЕ"):
    """Красивый вывод всей таблицы"""
    print(f"\n=== {title} ===")
    print(f"{'ID':<4} | {'Этаж':<4} | {'Площадь':<8} | {'Конд.':<5} | {'Цена/День':<10}")
    print("-" * 45)
    with sqlite3.connect(DB_NAME) as conn:
        for r in conn.execute("SELECT * FROM retail_outlets"):
            print(f"{r[0]:<4} | {r[1]:<4} | {r[2]:<8} | {r[3]:<5} | {r[4]:<10}")
    print("-" * 45)


def print_search(rows):
    """Вывод результатов поиска"""
    if not rows:
        print("\nНичего не найдено!")
        return
    print(f"\n{'ID':<4} | {'Этаж':<4} | {'Площадь':<8} | {'Конд.':<5} | {'Цена/День':<10}")
    print("-" * 45)
    for r in rows:
        print(f"{r[0]:<4} | {r[1]:<4} | {r[2]:<8} | {r[3]:<5} | {r[4]:<10}")


# menu
while True:
    print("\n      --- МЕНЮ УПРАВЛЕНИЯ ---")
    print("1. Показать всю таблицу")
    print("2. Добавить новую торговую точку (Ввод)")
    print("3. Поиск: По этажу")
    print("4. Поиск: Без кондиционера")
    print("5. Поиск: Дешевле заданной цены")
    print("6. Редактировать: Изменить цену по ID")
    print("7. Редактировать: Включить конд. для всего этажа")
    print("8. Редактировать: Скидка 10% на площади от 100 кв.м")
    print("9. Удалить: По конкретному ID")
    print("10. Удалить: Дороже заданной цены")
    print("11. Удалить: Маленькие площади (<30 кв.м) без конд.")
    print("0. Выход")

    choice = input("\nВыберите действие (введите число): ").strip()

    with sqlite3.connect(DB_NAME) as conn:
        if choice == "1":
            show_all()

        elif choice == "2":
            fl = int(input("Введите этаж: "))
            ar = float(input("Введите площадь (кв.м): "))
            ac = input("Есть кондиционер? (Да/Нет): ")
            pr = float(input("Введите цену аренды в день: "))
            conn.execute("INSERT INTO retail_outlets (floor, area, has_ac, daily_rent) VALUES (?, ?, ?, ?)",
                         (fl, ar, ac, pr))
            conn.commit()
            print("[Успешно добавлено]")

        elif choice == "3":
            fl = int(input("Какой этаж искать?: "))
            res = conn.execute("SELECT * FROM retail_outlets WHERE floor = ?", (fl,)).fetchall()
            print_search(res)

        elif choice == "4":
            res = conn.execute("SELECT * FROM retail_outlets WHERE has_ac = 'Нет'").fetchall()
            print_search(res)

        elif choice == "5":
            max_p = float(input("Показать точки дешевле чем (руб): "))
            res = conn.execute("SELECT * FROM retail_outlets WHERE daily_rent <= ?", (max_p,)).fetchall()
            print_search(res)

        elif choice == "6":
            idx = int(input("Введите ID точки: "))