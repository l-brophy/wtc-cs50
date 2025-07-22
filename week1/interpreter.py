expression = input("enter calculation: ").split(" ")
x, y = float(expression[0]), float(expression[2])

arithmetic = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y
}

print(arithmetic.get(expression[1]))