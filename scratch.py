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


