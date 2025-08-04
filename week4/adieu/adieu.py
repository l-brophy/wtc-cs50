names = []

try:
    while True:
        names.append(input("Name: "))
except EOFError:
    pass

if len(names) <= 2:
    sep = " and "
else:
    sep = ", "
    names.append(f"and {names.pop()}")

print(f"\nAdieu, Adieu, to {sep.join(names)}")
