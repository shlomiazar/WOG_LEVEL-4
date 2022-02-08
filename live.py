from Games import memory_game as MemoryGame, GuessGame as guess, currency_roulette as currency
import Score
import MainScores


def welcome():
    x = input("please enter your name: ")
    print(f'Hello, {x} and welcome to the world of games(WoG)\nhere you can find many cool games to play.')
    print("Please choose a game to play:\n" +
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n" +
          "2. Guess Game - guess a number and see if you chose like the computer\n" +
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")


def load_game():
    x = input("please enter a number from 1 to 3: ")
    difficulty = difficulty_number()

    if int(x) == 1:
        print(
            "you have chosen: Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        if MemoryGame.m_game(difficulty):
            Score.add_score(difficulty)
        else:
            print("you've lost the game")

    elif int(x) == 2:
        print("you have chosen: Guess Game - guess a number and see if you chose like the computer")
        if guess.guess(difficulty):
            Score.add_score(difficulty)
        else:
            print("you've lost the game")

    elif int(x) == 3:
        print("you have chosen: Currency Roulette - try and guess the value of a random amount of USD in ILS")
        if currency.play(difficulty):
            Score.add_score(difficulty)
        else:
            print("you've lost the game")

    else:
        while x != (1, 2, 3):
            print("you have entered a incorrect number!")
            return load_game()
    MainScores.run()


def difficulty_number():
    y = input("please enter a number from 1 to 5: ")

    if int(y) == 1:
        print("you have chosen: difficulty number 1")

    elif int(y) == 2:
        print("you have chosen: difficulty number 2")


    elif int(y) == 3:
        print("you have chosen: difficulty number 3")

    elif int(y) == 4:
        print("you have chosen: difficulty number 4")

    elif int(y) == 5:
        print("you have chosen: difficulty number 5")


    else:
        while y != (1, 2, 3, 4, 5):
            print("you have entered a incorrect number!")
        return difficulty_number()
    return int(y)
