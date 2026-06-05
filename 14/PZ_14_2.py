'''
Задание 2. Разработать программу с применением пакета tk, взяв в
качестве условия одн любую задачу из ПЗ №№ 1-9.
'''
import tkinter as tk

def check():
    txt.delete("1.0", tk.END)
    txt.insert(tk.END, "Канада: Вояж, Рейна Тур\n\nСША: Вояж, Радуга")

app = tk.Tk()
app.title("Вариант 30")
app.geometry("350x220")

tk.Button(app, text="Найти туры", command=check).pack(pady=15)
txt = tk.Text(app, height=5, width=35, bd=1, relief="solid")
txt.pack()

app.mainloop()