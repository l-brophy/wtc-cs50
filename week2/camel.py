camel = input("camelCase: ")

snake = ""

for i in camel:
    if i.isupper():
        snake += f"_{i.lower()}"
    else:
        snake += i

print(f"snake_case: {snake}")