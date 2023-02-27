from dataclasses import dataclass
from datetime import date
from enum import Enum


class FlightStatus(Enum):
    SCHEDULED = 1
    DELAYED = 2
    DEPARTED = 3
    IN_AIR = 4
    EXPECTED = 5
    DIVERTED = 6
    RECOVERY = 7
    LANDED = 8
    ARRIVED = 9
    CANCELLED = 10
    NO_TAKEOFF_INFO = 11


@dataclass
class FlightInfo:
    ICAO_acronym: str
    airline: str
    flight_number: int
    DI_code: int
    line_type_code: str
    equipment_model: str
    number_of_seats: int

    ICAO_airport_origin: str
    airport_origin_description: str
    scheduled_departure: date
    actual_departure: date

    ICAO_airport_destination: str
    airport_destination_description: str

    expected_arrival: date
    actual_arrival: date

    flight_status: FlightStatus
    justification: str
    reference: date

    departure_status: str
    arrival_status: str
