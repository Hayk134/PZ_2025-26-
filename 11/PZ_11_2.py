'''
 Составить генератор (yield), который преобразует все буквенные символы в заглавные
'''
def yeld(text):
    for char in text:
        yield char.upper()


source = "Hello, World!"
result = ""
for sym in yeld(source):
    result += sym


print(source)
print(result)
