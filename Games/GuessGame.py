import random


def guess(diff):
    x = random.randint(1, diff)
    guess = int(input(f"please enter a number from 1 to {diff}: "))
    if x == guess:
        print("you won")
        return True
    else:
        print("you lost")
        return False
