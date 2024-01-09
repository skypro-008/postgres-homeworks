import csv
from pathlib import Path


def open_csv_file(filepath: Path):
    """
    Функция читает данные из файла формата csv
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))
        return list(tuple(obj.values()) for obj in reader)
