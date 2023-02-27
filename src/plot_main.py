from flight_info_generator import generate_flight_info
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np

RANGE_START = 0
RANGE_STOP = 20
RANGE_INTE = 1


def get_sorted_data(filepath: str):
    flight_info = generate_flight_info(filepath)[RANGE_START:RANGE_STOP:RANGE_INTE]
    def sorting(L):
        splitup = L[0].split('/')
        return splitup[2], splitup[1], splitup[0]
    
    data = [(x.actual_arrival.split(' ')[0], int(x.number_of_seats)) for x in flight_info if x.actual_arrival != '']
    data_sorted = sorted(data, key=sorting)

    return data_sorted


def plot_least_minimum_squares(filepath: str, title):
    data_sorted = get_sorted_data(filepath)

    y = [k[1] for k in data_sorted]
    x = range(len(y))

    # A matrix:
    A = np.vstack([x, np.ones(len(x))]).T
    alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)

    plt.title(title)
    plt.ylabel('Número de Assentos')
    plt.plot(x, y, 'b.')
    plt.plot(x, alpha[0] * x + alpha[1], 'r')

    plt.show()


def generate_lagrange(filepath):
    data_sorted = get_sorted_data(filepath)
    y = [k[1] for k in data_sorted]

    x = range(0, len(y))

    for px, py in zip(x, y):
        print(px, py)


def main():
    # Least Square Method:

    # plot_least_minimum_squares('../res/VRA_MAO_to_PIN.csv', 'VRA: MAO -> PIN')
    # plot_least_minimum_squares('../res/VRA_MAO_to_PIN_AZU.csv', 'VRA: MAO -> PIN [AZUL]')
    # plot_least_minimum_squares('../res/VRA_MAO_to_PIN_PAM.csv', 'VRA: MAO -> PIN [PAM]')
    # plot_least_minimum_squares('../res/VRA_MAO_to_PIN_TTL.csv', 'VRA: MAO -> PIN [TTL]')

    # Lagrange:
    # generate_lagrange('../res/VRA_MAO_to_PIN_TTL.csv')
    # generate_lagrange('../res/VRA_MAO_to_PIN_AZU.csv')
    generate_lagrange('../res/VRA_MAO_to_PIN_PAM.csv')
    # generate_lagrange('../res/VRA_MAO_to_PIN.csv')


if __name__ == '__main__':
    main()
