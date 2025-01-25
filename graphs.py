# from parser import sleeping
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def unpack(coin_name):

    file = open(f'{coin_name}_price.txt', 'r')
    coin_price = [float(price[:-2]) for price in file]
    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.set_title('BTC')
    ax.plot([int(i) for i in range(len(coin_price))], coin_price)  # Plot some data on the Axes.
    plt.show()  # Show the figure.


def build_graph():

    # Стартовое время
    start_time = datetime.strptime("15:30", "%H:%M")


    file = open('btc_price.txt', 'r')
    btc_price = [float(price[:-2]) for price in file]

    num_intervals = len(btc_price)
    time_step = timedelta(minutes=5)

    # Массив для хранения временных промежутков
    time_intervals = []

    # Заполнение массива
    for i in range(num_intervals):
        current_time = start_time + i * time_step
        time_intervals.append(current_time.strftime("%H:%M"))


    choise = input("Select coin \n"
          "1: Bitcoin\n"
          "2: Ethereum\n"
          "3: Toncoin\n")

    if choise == "1":
        unpack('btc')

    elif choise =='2':
        unpack('eth')

    elif choise == '3':
        unpack('ton')





