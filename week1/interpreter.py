expression = input("enter calculation: ").split(" ")
x, y = float(expression[0]), float(expression[2])

rename_this = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y
}

print(rename_this.get(expression[1]))