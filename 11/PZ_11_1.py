'''
1. Даны средние значения температур за каждый месяц в году. Найти минимальное и
максимальное значения температур за год. Вывести значения температур по временам года.
'''

temperatures = [-10, -8, -2, 6, 15, 20, 23, 21, 14, 7, 0, -6]

min_temp = min(temperatures)
max_temp = max(temperatures)

winter = [temperatures[0], temperatures[1], temperatures[11]]
spring = temperatures[2:5]
summer = temperatures[5:8]
autumn = temperatures[8:11]

print("Минимальная температура за год:", min_temp)
print("Максимальная температура за год:", max_temp)
print("Зима:", winter)
print("Весна:", spring)
print("Лето:", summer)
print("Осень:", autumn)