import csv


def import_csv(filepath: str, delimiter: str = ',') -> list:
    results = []

    with open(filepath, mode='r', encoding='utf-8-sig') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=delimiter)
        for row in csv_data:
            results.append(row)
    
    return results