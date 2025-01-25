from bs4 import BeautifulSoup as bs
import requests
import time
import matplotlib.pyplot as plt



def str_to_float(price):

    price = price[1:].replace(',', '')
    return price

def sleeping(sleep_time):
    for i in range(1, sleep_time + 1):
        # Печатаем число с возвратом каретки в начало строки
        print(f'\rsleep {i} / {sleep_time}', end='', flush=True)
        time.sleep(1)  # Задержка на 1 секунду
    print()



def start_pars():

    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    url = 'https://coinmarketcap.com/currencies/'
    coins = {
        'ETH': 'ethereum/',
        'BTC': 'bitcoin/',
        'TON': 'toncoin/'
    }
    session = requests.Session()

    print('Information by CoinMarketCap\n')

    while True:

        try:
            for coin, coin_url in coins.items():

                req = session.get(url + coin_url, headers=headers)

                if req.status_code == 200:

                    soup = bs(req.content, 'html.parser')
                    divs = soup.find('div', attrs={
                        'class': 'sc-65e7f566-0 czwNaM flexStart alignBaseline'
                    })

                    with open(f'{coin.lower()}_price.txt', 'a') as file:
                        file.writelines(str_to_float(divs.find('span').text) + '\n')
                        file.close()

                else:

                    print('bad gateaway')

        except Exception:
            print('error')

        print("Prices updated")

        sleeping(300)

    print('Stopped without errors')