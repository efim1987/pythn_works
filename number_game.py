import random
number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess the number from 0 to 100: "))
    if guess < number:
        print("Число больше")
    elif guess > number:
        print("Число меньше")
print("You win")
