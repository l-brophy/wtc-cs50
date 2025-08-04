import random


def main():
    
    nums = generate_integers(get_level())
    score = 0
    
    for question in nums:
        incorrect_answers = 0
        x, y = question[0], question[1]
        
        while incorrect_answers < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                continue

            if answer == sum(question):
                score += 1
                break
            else:
                print("EEE")
                incorrect_answers += 1
        
        if incorrect_answers == 3:
            print(f"{x} + {y} = {sum(question)}")
    
    print(score)


def get_level():
    # perform level checks here instead of requiring generate_ints to do so
    try:
        while True:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                return level
            
    except ValueError:
        return get_level()


def generate_integers(level):
    
    # check level once instead of for every individual int
    if level == 1:
        x, y = 1, 9
    elif level == 2:
        x, y = 10, 99
    elif level == 3:
        x, y = 100, 999
    
    # list comp to generate 2d list of questions[ints]
    return [[random.randint(x, y) for _ in range(2)] for _ in range(10)]


if __name__ == "__main__":
    main()