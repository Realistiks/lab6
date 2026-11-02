print("Введите текст")
text = input()
print("Ключевое слово")
key = input().lower()

ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ru_up = ru.upper()

key = "".join(c for c in key if c in ru)

if len(key) == 0:
    print("Ключ должен содержать русские буквы")
else:
    result = ""
    index = 0
    for c in text:
        if c.lower() in ru:
            shift = ru.index(key[index % len(key)])
            if c in ru:
                result += ru[(ru.index(c) + shift) % len(ru)]
            else:
                result += ru_up[(ru_up.index(c) + shift) % len(ru_up)]
            index += 1
        else:
            result += c

    print("Зашифровано:", result)

    decoded = ""
    index = 0
    for c in result:
        if c.lower() in ru:
            shift = ru.index(key[index % len(key)])
            if c in ru:
                decoded += ru[(ru.index(c) - shift) % len(ru)]
            else:
                decoded += ru_up[(ru_up.index(c) - shift) % len(ru_up)]
            index += 1
        else:
            decoded += c

    print("Расшифровано:", decoded)
