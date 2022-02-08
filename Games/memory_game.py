import random
from time import sleep


def m_game(diff):
    generated_list = random.sample(range(1, 101), diff)
    print(generated_list);
    sleep(0.7)
    print("\n" * 100)
    listA = []

    listA = list(map(int, input("Enter the numbers : ").strip().split()))[:diff]
    if listA != generated_list:
        print("you have entered an invalid elements")

    else:
        print("The entered list is: \n", listA)

    if generated_list == listA:
        print("well done")
        return True
    else:

        print("try next time")

        return False
