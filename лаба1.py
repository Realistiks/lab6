print("Введите текст")
text = input().strip()

if len(text) == 0:
    print("Текст пустой")
else:
    words = text.split()
    print(f"Слов в тексте: {len(words)}")
    print("Самое длинное слово:", max(words, key=len))
    print("Самое короткое слово:", min(words, key=len))
