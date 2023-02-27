import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from flight_info_generator import generate_flight_info
import numpy as np


SAMPLE_SIZE = -1
DATE_INTERVAL = 15


def get_sorted_data():
    flight_info = generate_flight_info('../res/VRA_MAO_to_PIN_PAM.csv')[:SAMPLE_SIZE]
    def sorting(L):
        splitup = L[0].split('/')
        return splitup[2], splitup[1], splitup[0]
    
    data = [(x.actual_arrival.split(' ')[0], int(x.number_of_seats)) for x in flight_info if x.actual_arrival != '']
    data_sorted = sorted(data, key=sorting)

    return data_sorted


def a():
    # x = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in [k[0] for k in data_sorted]]
    
    # Settings:
    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    # plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=DATE_INTERVAL))
    # plt.gcf().autofmt_xdate()
    pass


def main():
    data_sorted = get_sorted_data()

    y = [k[1] for k in data_sorted]
    alpha_x = range(len(y))

    # A matrix:
    A = np.vstack([alpha_x, np.ones(len(alpha_x))]).T
    alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)

    plt.ylabel('Número de Assentos')
    plt.plot(alpha_x, y, 'b.')
    plt.plot(alpha_x, alpha[0] * alpha_x + alpha[1], 'r')

    plt.show()


if __name__ == '__main__':
    main()
