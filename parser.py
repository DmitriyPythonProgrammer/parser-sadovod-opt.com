
import core
import time
import pandas as pd


def main(general_url, agent):
    column_name = {'Имя': [],
                   'Цена': [],
                   'Ссылка': []}
    dataframe = pd.DataFrame(column_name)
    time_sleep = 0.5
    i = 1
    while True:
        url = general_url + f'/{i}'
        soup = core.soup(url, agent)
        if not soup:
            break
        item = soup.find_all('div', class_='list-item')
        for el in item:
            item_info = el.find(class_='item-info')
            name = item_info.find('a', class_='item-name').contents[0]
            price = item_info.find('span').contents[0]
            adr_str = (el.find(class_='item-image')).find('a')
            adr = adr_str['href']
            dataframe.loc[len(dataframe.index)] = [name, price, adr]
        i += 1
        time.sleep(time_sleep)
    print(f'Парсинг закончен, страниц просканировано: {i}')
    dataframe.to_excel("data.xlsx", index=True)
