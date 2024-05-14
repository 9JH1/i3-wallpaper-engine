import requests

def test_scrape(): 

    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    print(page.text)