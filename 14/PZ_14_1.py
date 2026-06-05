'''
Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализоват его в
IDE PyCharm Community с применением пакета tk. Получить интерфейс максимальн приближенный к
оригиналу (см. таблицу 1).
'''


import tkinter as tk

root = tk.Tk()
root.title("Регистрационная страница")
root.geometry("600x670")
root.configure(bg="#ff9999")

tk.Label(root, text="Регистрационная страница электронной библиотеки", bg="#ff9999", font=("Arial", 12, "bold")).pack(anchor="w", padx=15, pady=(15, 5))
tk.Label(root, text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой", bg="#ff9999").pack(anchor="w", padx=15, pady=(0, 15))

frame_inputs = tk.Frame(root, bg="#ff9999")
frame_inputs.pack(anchor="w", padx=15)

tk.Label(frame_inputs, text="Введите регистрационное имя", bg="#ff9999").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(frame_inputs, width=30, bd=1, relief="solid").grid(row=0, column=1, padx=10)

tk.Label(frame_inputs, text="Введите пароль", bg="#ff9999").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(frame_inputs, width=30, show="*", bd=1, relief="solid").grid(row=1, column=1, padx=10)

tk.Label(frame_inputs, text="Подтвердите пароль", bg="#ff9999").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(frame_inputs, width=30, show="*", bd=1, relief="solid").grid(row=2, column=1, padx=10)

tk.Label(root, text="Ваш возраст", bg="#ff9999").pack(anchor="w", padx=15, pady=(15, 5))
frame_age = tk.Frame(root, bg="#ff9999")
frame_age.pack(anchor="w", padx=15)
age_var = tk.StringVar(value="До 20")
tk.Radiobutton(frame_age, text="До 20", value="До 20", variable=age_var, bg="#ff9999").pack(side="left", padx=(0, 15))
tk.Radiobutton(frame_age, text="20-30", value="20-30", variable=age_var, bg="#ff9999").pack(side="left", padx=(0, 15))
tk.Radiobutton(frame_age, text="30-50", value="30-50", variable=age_var, bg="#ff9999").pack(side="left", padx=(0, 15))
tk.Radiobutton(frame_age, text="Старше 50", value="Старше 50", variable=age_var, bg="#ff9999").pack(side="left", padx=(0, 15))

tk.Label(root, text="На каких языках читаете:", bg="#ff9999").pack(anchor="w", padx=15, pady=(15, 5))
frame_lang = tk.Frame(root, bg="#ff9999")
frame_lang.pack(anchor="w", padx=15)
v1 = tk.BooleanVar(value=True)
v2 = tk.BooleanVar()
v3 = tk.BooleanVar()
v4 = tk.BooleanVar()
tk.Checkbutton(frame_lang, text="русский", variable=v1, bg="#ff9999").pack(side="left", padx=(0, 15))
tk.Checkbutton(frame_lang, text="английский", variable=v2, bg="#ff9999").pack(side="left", padx=(0, 15))
tk.Checkbutton(frame_lang, text="французский", variable=v3, bg="#ff9999").pack(side="left", padx=(0, 15))
tk.Checkbutton(frame_lang, text="немецкий", variable=v4, bg="#ff9999").pack(side="left", padx=(0, 15))

tk.Label(root, text="Какой формат данных является для вас предпочтительным?", bg="#ff9999").pack(anchor="w", padx=15, pady=(15, 5))
listbox = tk.Listbox(root, height=2, width=15, bd=1, relief="solid")
listbox.insert(1, "HTML")
listbox.insert(2, "Plain text")
listbox.select_set(0)
listbox.pack(anchor="w", padx=15)

tk.Label(root, text="Ваши любимые авторы:", bg="#ff9999").pack(anchor="w", padx=15, pady=(15, 5))
tk.Text(root, height=4, width=50, bd=1, relief="solid").pack(anchor="w", padx=15)

frame_btn = tk.Frame(root, bg="#ff9999")
frame_btn.pack(anchor="w", padx=15, pady=15)
tk.Button(frame_btn, text="ОК", width=8).pack(side="left", padx=(0, 10))
tk.Button(frame_btn, text="Отменить", width=10).pack(side="left")

tk.Label(root, text="Проверка PHP Лабораторные по базам данных", bg="#ff9999").pack(anchor="w", padx=15, pady=(10, 5))

frame_foot = tk.Frame(root, bd=1, relief="solid", bg="#e1e1e1", padx=10, pady=10)
frame_foot.pack(fill="x", padx=15, pady=5)
tk.Label(frame_foot, text="Лабораторные по базам данных", bg="#e1e1e1").pack()

tk.Label(root, text="Сегодня замечательный день.", bg="#ff9999").pack(pady=(10, 0))
tk.Label(root, text="Я сделал свою первую интернет страничку.", bg="#ff9999").pack()
tk.Label(root, text="я буду богатым и свободным человеком !", bg="#ff9999", fg="blue", font=("Arial", 11, "underline")).pack()

root.mainloop()