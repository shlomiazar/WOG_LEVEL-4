import requests
import random


def getCurrencyRate():
    rate = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=0cab4400-4d70-11ec-a03b-6bfc73494580")
    respones = rate.json()
    respones = respones["data"]["ILS"]
    return respones


def get_money_interval(diff):
    rand = random.randint(1, 100)
    print(f"Please guess the right amount in ILS of {rand}")
    t = rand * getCurrencyRate()
    interval = (t - (5 - diff), t + (5 - diff))
    return interval


def get_guess_from_user():
    x = int(input("Please enter you guess:"))
    return x


def play(diff):
    range = get_money_interval(diff)
    guess = get_guess_from_user()
    if range[0] <= guess <= range[1]:
        print("congratulations,You Won")
    else:
        print("sorry, You lost!")
