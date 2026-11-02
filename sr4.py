print("Введите JSON-строку")
text = input().strip()

correct = len(text) > 0 and (text[0] == "{" or text[0] == "[")

stack = []
quotes = 0
in_string = False

for c in text:
    if c == '"':
        in_string = not in_string
        quotes += 1
    elif not in_string:
        if c in "{[(":
            stack.append(c)
        elif c in "}])":
            if len(stack) == 0:
                correct = False
                break
            last = stack.pop()
            if (c == "}" and last != "{") or (c == "]" and last != "[") or (c == ")" and last != "("):
                correct = False
                break
            if c == "}" and last == "{" and len(stack) == 0 and text[-1] != "}":
                correct = False
            if c == "]" and last == "[" and len(stack) == 0 and text[-1] != "]":
                correct = False

if quotes % 2 != 0 or in_string:
    correct = False
if len(stack) != 0:
    correct = False

print()
if correct:
    print("JSON корректен")
else:
    print("JSON некорректен")
