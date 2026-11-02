print("Введите строку")
text = input()

clean = ""
for c in text.lower():
    if c.isalnum():
        clean += c

print("Очищенная строка:", clean)

if len(clean) == 0:
    print("В строке нет букв и цифр")
elif clean == clean[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")
