groceries = {}

try:
    while True:
        i = input("")
        if i in groceries:
            groceries[i] += 1
        else:
            groceries[i] = 1
except EOFError:
    for k, v in groceries.items():
        print(f"{v} {k.upper()}")