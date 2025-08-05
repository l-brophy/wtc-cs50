try:
    lines = 0
    
    with open("hello_world.py", "r") as file:
        for line in file:
            if line != "\n" and line.strip()[0] != "#":
                    lines += 1
                    
    print(f"Lines of code: {lines}")
except FileNotFoundError:
    raise SystemExit("Could not locate file")