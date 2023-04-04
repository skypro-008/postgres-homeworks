import csv


def get_data_from_csv(key: str, path: str) -> list:
    """Получает нужные данные из файла"""
    with open(path, encoding='cp1251') as file:
        reader = csv.DictReader(file)
        data = []
        if key == 'employees':
            for row in reader:
                name = (row['first_name'] + ' ' + row['last_name'])
                profession = row['title']
                notes = row['notes']
                data.append((name, profession, notes))

        elif key == 'customers':
            for row in reader:
                customer_id = row['customer_id']
                company_name = row['company_name']
                data.append((customer_id, company_name))

        elif key == 'orders':
            for row in reader:
                order_id = row['order_id']
                customer_id = row['customer_id']
                emp_id = row['employee_id']
                date = row['order_date']
                city = row['ship_city']
                data.append((order_id, customer_id, emp_id, date, city))

        return data
