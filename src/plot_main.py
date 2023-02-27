from flight_info_generator import generate_flight_info
from scipy.interpolate import lagrange
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

SAMPLE_SIZE = -1
DATE_INTERVAL = 15


def get_sorted_data(filepath: str):
    flight_info = generate_flight_info(filepath)[:SAMPLE_SIZE]
    def sorting(L):
        splitup = L[0].split('/')
        return splitup[2], splitup[1], splitup[0]
    
    data = [(x.actual_arrival.split(' ')[0], int(x.number_of_seats)) for x in flight_info if x.actual_arrival != '']
    data_sorted = sorted(data, key=sorting)

    return data_sorted


def plot_least_minimum_squares(filepath: str, title):
    data_sorted = get_sorted_data(filepath)

    y = [k[1] for k in data_sorted]
    alpha_x = range(len(y))

    # A matrix:
    A = np.vstack([alpha_x, np.ones(len(alpha_x))]).T
    alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)

    plt.title(title)
    plt.ylabel('Número de Assentos')
    plt.plot(alpha_x, y, 'b.')
    plt.plot(alpha_x, alpha[0] * alpha_x + alpha[1], 'r')

    plt.show()


def main():
    # Least Square Method:

    # plot_least_minimum_squares('../res/VRA_MAO_to_PIN.csv', 'VRA: MAO -> PIN')
    # plot_least_minimum_squares('../res/VRA_MAO_to_PIN_AZU.csv', 'VRA: MAO -> PIN [AZUL]')
    # plot_least_minimum_squares('../res/VRA_MAO_to_PIN_PAM.csv', 'VRA: MAO -> PIN [PAM]')
    plot_least_minimum_squares('../res/VRA_MAO_to_PIN_TTL.csv', 'VRA: MAO -> PIN [TTL]')


if __name__ == '__main__':
    main()
