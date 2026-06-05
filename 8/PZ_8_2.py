
'''
2

Дан словарь на 6 персон, найти и вывести их средний возраст.
(Пример, {"Андрей": 32, "Виктор": 29, "Максим": 18, ... }, среднее 26,33).
'''

people_age = {
    "Андрей": 32,
    "Виктор": 29,
    "Максим": 18,
    "Дмитрий": 41,
    "Елена": 24,
    "Анна": 35
}

total_age = 0

for name in people_age:
    total_age += people_age[name]


average_age = total_age / len(people_age)

print(f"Среднее : {average_age:.2f}")