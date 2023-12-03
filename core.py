import requests
from getuseragent import UserAgent
from bs4 import BeautifulSoup


def create_user_agent():
    useragent = UserAgent()
    agent = useragent.Random()
    return {'User-agent': agent}


def soup(url, agent):
    response = requests.get(url, headers=agent)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'lxml')
    else:
        return False



def is_connected():
    print('Подключение к серверу...')
    url = 'https://sadovod-opt.com/shop/all'
    response = requests.get(url)
    if response.status_code == 200:
        print('Успешное подключение')
        return True
    else:
        return False



