names = ["Иван", "Мария", "Пётр", "Анна"]
ages = [25, 22, 30, 20]
scores = [4.50, 4.85, 4.20, 4.95]

print(f'{"Имя":<10}{"Возраст":>10}{"Балл":>10}')
print("-" * 30)

total = 0
for i in range(len(names)):
    print(f'{names[i]:<10}{ages[i]:>10}{scores[i]:>10.2f}')
    total += scores[i]

print("-" * 30)
average = total / len(scores)
print(f'{"Средний балл":<10}{"":>10}{average:>10.2f}')
