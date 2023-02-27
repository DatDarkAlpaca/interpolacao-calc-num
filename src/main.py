from flight_info_generator import export_flight_info, generate_flight_info


def main():
    export_flight_info('res/flight_data.csv', generate_flight_info('res/flight_data_MAO_to_PIN.csv'))


if __name__ == '__main__':
    main()
