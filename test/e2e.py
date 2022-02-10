from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import sys

url = 'http://127.0.0.1:5000/'


# noinspection PyDeprecation
def test_score_service():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        score = int(driver.find_element('Score').text)
        driver.close()
        return 0 <= score <= 1000
    except BaseException:
        print("cannot open the server")


def main_function():
    if test_score_service():
        print(0)
        return sys.exit(0)
    else:
        print(-1)
        return sys.exit(-1)
    return sys.exit(-1)


if __name__ == '__main__':
    main_function()
