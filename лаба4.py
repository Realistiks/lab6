print("Валидация email")
email = input("Email: ").strip()
parts = email.split("@")

ok = len(parts) == 2
if ok:
    name = parts[0]
    domain = parts[1]
    ok = len(name) > 0 and "." in domain and len(domain.split(".")[-1]) >= 2

if ok:
    print("Корректный email")
else:
    print("Некорректный email")

print()
print("Валидация телефона")
phone = input("Телефон: ").strip()

digits = ""
allowed = True
for c in phone:
    if c.isdigit():
        digits += c
    elif c not in " +-()":
        allowed = False

if allowed and (len(digits) == 10 or len(digits) == 11):
    print("Корректный телефон")
else:
    print("Некорректный телефон")

print()
print("Валидация URL")
url = input("URL: ").strip()

ok = url.startswith("http://") or url.startswith("https://")
if ok:
    rest = url.split("://")[1]
    ok = "." in rest and len(rest) > 3

if ok:
    print("Корректный URL")
else:
    print("Некорректный URL")
