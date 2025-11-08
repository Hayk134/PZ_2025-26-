'''
Дан символ С и строки S, S₀. После каждого вхождения символа С в строку S вставить строку S₀.
'''

def stroka (text):
    f, l = text.find(''), text.rfind('')
    
    if f != l :
        return text[f + 1 : l]
    else :
        return""
test = "Тут есть много пробл в " 
print(stroka("Тут есть много про"))
