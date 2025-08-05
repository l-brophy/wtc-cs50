import sys
from tabulate import tabulate


if len(sys.argv) < 2:
    raise SystemExit("Too few command-line arguments")

if len(sys.argv) > 2:
    raise SystemExit("Too many command-line arguments")

if ".csv" not in sys.argv[1] or sys.argv[1].split(".")[1] != "csv":
    raise SystemExit("Not a csv file")


try:
    
    with open(sys.argv[1], "r") as file:
        table = file.readlines()

    for i in range(len(table)):
        table[i] = table[i].strip("\n").split(",")

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    
except FileNotFoundError:
    raise SystemExit("CSV file does not exist")