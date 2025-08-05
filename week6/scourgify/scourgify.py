import sys
# COME BACK TO THIS!!! IT LOOKS HIDEOUS

def clean(str):
    return str.replace("\"", "").replace(" ", "")


def swap(li):
    li[0], li[1] = li[1], li[0]
    return li


adj = len(sys.argv)
if adj != 3:
    adj = "many" if adj > 3 else "few"
    raise SystemExit(f"Too {adj} command-line arguments")


try:
    with open(sys.argv[1], "r") as file:
        students = file.readlines()
        students.pop(0)
except FileNotFoundError:
    raise SystemExit(f"Could not read {sys.argv[1]}")


for i in range(len(students)):
    students[i] = swap(clean(students[i]).split(","))


with open(sys.argv[2], "a", newline="\n") as newfile:
    for j in students:
        newfile.write(f"{" ".join(j[0:2])},{j[-1]}")