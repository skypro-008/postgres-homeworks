import csv


def get_csv_data(filename):
    table_scv_data = []
    with open(filename, newline='') as f:
        rows = csv.reader(f)
        for row in rows:
            table_scv_data.append(row)
    return table_scv_data
