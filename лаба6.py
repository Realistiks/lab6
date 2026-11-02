print("Введите текст")
text = input().strip()

sentences = []
current = ""
for c in text:
    current += c
    if c in ".!?":
        sentences.append(current.strip())
        current = ""

if len(current.strip()) > 0:
    sentences.append(current.strip())

if len(sentences) == 0:
    print("Предложений не найдено")
else:
    print(f"Предложений: {len(sentences)}")
    for i in range(len(sentences)):
        print(f"{i + 1}. {sentences[i]}")
