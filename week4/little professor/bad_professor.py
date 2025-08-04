import random
# will still work on this even though the desired logic is really weird to me
# but i wanted to do it well 

def main():
    return


def get_level():
    
    try:
        while True:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                return level
            
    except ValueError:
        return get_level()


def generate_integer(level):
    # wants to generate 1 integer at a time, weirdly? 20 if-checks???? stupid
    if level == 1:
        return random.randint(1, 9)
    
    if level == 2:
        return random.randint(10, 99)
    
    if level == 3:
        return random.randint(100, 999)


get_level()
