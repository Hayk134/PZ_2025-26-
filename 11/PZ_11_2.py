'''
 Составить генератор (yield), который преобразует все буквенные символы в заглавные
'''
yeld = lambda generator: (yield from (char.upper() for char in generator))

text = "Hello, World!"
result = ""

for char in yeld(text):
    result += char

print(result)