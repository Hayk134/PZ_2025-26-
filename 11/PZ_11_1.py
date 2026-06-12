'''
1. Даны средние значения температур за каждый месяц в году. Найти минимальное и
максимальное значения температур за год. Вывести значения температур по временам года.
'''
temps = [-10, -8, -2, 6, 15, 20, 23, 21, 14, 7, 0, -6]
min_temp = min(temps)
max_temp = max(temps)

winter = [temps[i] for i in [0, 1, 11]]
spring = [temps[i] for i in range(2, 5)]
summer = [temps[i] for i in range(5, 8)]
autumn = [temps[i] for i in range(8, 11)]

print(f"Минимальная температура: {min_temp}")
print(f"Максимальная температура: {max_temp}")
print(f"Зима: {winter}, Весна: {spring}, Лето: {summer}, Осень: {autumn}")




