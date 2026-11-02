log = """
2026-11-02 10:15:01 INFO Сервер запущен
2026-11-02 10:15:42 ERROR Не удалось подключиться к базе данных
2026-11-02 10:16:03 WARNING Мало свободной памяти
2026-11-02 10:17:25 ERROR Пользователь admin не найден
2026-11-02 10:18:10 INFO Синхронизация завершена
2026-11-02 10:19:47 ERROR Таймаут запроса к API
"""

lines = log.strip().split("\n")

print("Записи уровня ERROR:")
count = 0
for line in lines:
    if " ERROR " in line:
        words = line.split()
        date = words[0]
        time = words[1]
        message = " ".join(words[3:])
        count += 1
        print(f"{count}. [{date} {time}] {message}")

print()
print("Всего ошибок:", count)
