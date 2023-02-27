from flight_info import FlightInfo
from csv_helper import import_csv
import csv


def generate_flight_info(filepath: str, flight_delimiter: str = ';') -> list[FlightInfo]:
    results = []
    
    csv_data = import_csv(filepath, delimiter=flight_delimiter)
    for row in csv_data[1:]:
        results.append(FlightInfo(*row))

    return results


def export_flight_info(filepath:str, data_filepath: str) -> None:
    flight_data = generate_flight_info(data_filepath)

    with open(filepath, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = [
            'Sigla ICAO Empresa Aérea',
            'Sigla ICAO Aeroporto Origem',
            'Sigla ICAO Aeroporto Destino',
            'Número de Assentos',
            'Partida Real',
            'Chegada Real'
        ]

        flight_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        flight_writer.writeheader()

        for flight in flight_data:
            flight_writer.writerow({
                'Sigla ICAO Empresa Aérea': flight.ICAO_acronym, 
                'Sigla ICAO Aeroporto Origem': flight.ICAO_airport_origin,
                'Sigla ICAO Aeroporto Destino': flight.ICAO_airport_destination,
                'Número de Assentos': flight.number_of_seats,
                'Partida Real': flight.actual_departure,
                'Chegada Real': flight.actual_arrival
            })
