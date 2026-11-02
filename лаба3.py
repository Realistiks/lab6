print("Введите текст")
text = input()
print("Сдвиг")
k = int(input())

ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ru_up = ru.upper()
en = "abcdefghijklmnopqrstuvwxyz"
en_up = en.upper()

result = ""
for c in text:
    if c in ru:
        result += ru[(ru.index(c) + k) % len(ru)]
    elif c in ru_up:
        result += ru_up[(ru_up.index(c) + k) % len(ru_up)]
    elif c in en:
        result += en[(en.index(c) + k) % len(en)]
    elif c in en_up:
        result += en_up[(en_up.index(c) + k) % len(en_up)]
    else:
        result += c

print("Зашифровано:", result)

decoded = ""
for c in result:
    if c in ru:
        decoded += ru[(ru.index(c) - k) % len(ru)]
    elif c in ru_up:
        decoded += ru_up[(ru_up.index(c) - k) % len(ru_up)]
    elif c in en:
        decoded += en[(en.index(c) - k) % len(en)]
    elif c in en_up:
        decoded += en_up[(en_up.index(c) - k) % len(en_up)]
    else:
        decoded += c

print("Расшифровано:", decoded)
