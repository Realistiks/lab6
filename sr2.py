print("Введите текст")
text = input().lower()

clean = ""
for c in text:
    if c.isalnum():
        clean += c
    else:
        clean += " "

words = clean.split()

unique = []
counts = []
for w in words:
    if w in unique:
        i = unique.index(w)
        counts[i] += 1
    else:
        unique.append(w)
        counts.append(1)

n = len(unique)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if counts[j] < counts[j + 1]:
            counts[j], counts[j + 1] = counts[j + 1], counts[j]
            unique[j], unique[j + 1] = unique[j + 1], unique[j]

print()
print("Топ-10 слов:")
limit = 10
if len(unique) < 10:
    limit = len(unique)

for i in range(limit):
    print(f"{i + 1:>2}. {unique[i]:<15} {counts[i]}")
