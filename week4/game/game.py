import random

n = input("Level: ")
number = random.randint(1, int(n))

guess = -1
while guess < 0:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass

if guess == number:
    print("Just right!")
elif guess > number:
    print("Too large!")
elif guess < number:
    print("Too small!")