import csv

class ParsingCSVFiles:

    def parsing_customers_file(self):
        customers_data = []

        with open('north_data/customers_data.csv', 'r') as f:
            read_csv = csv.reader(f, delimiter=",")

            for row in read_csv:
                customer_id = row[0]
                company_name = row[1]
                contact_name = row[2]
                global_tuple = (customer_id, company_name, contact_name)
                customers_data.append(global_tuple)

        return customers_data

    def parsing_employees_file(self):

        employees_data = []
        with open('north_data/employees_data.csv', 'r') as f:
            read_csv = csv.reader(f, delimiter=",")

            for row in read_csv:
                employee_id = row[0]
                first_name = row[1]
                last_name = row[2]
                title = row[3]
                birth_date = row[4]
                notes = row[5]
                global_tuple = (employee_id, first_name, last_name, title, birth_date, notes)  #
                employees_data.append(global_tuple)

        return employees_data

    def parsing_orders_file(self):
        orders_data = []
        with open('north_data/orders_data.csv', 'r') as f:
            read_csv = csv.reader(f, delimiter=",")

            for row in read_csv:
                # print(row)
                order_id = row[0]
                customer_id = row[1]
                employee_id = row[2]
                order_date = row[3]
                ship_city = row[4]  #
                global_tuple = (order_id, customer_id, employee_id, order_date, ship_city)  #
                orders_data.append(global_tuple)

        return orders_data
