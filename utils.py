import psycopg2


def write_in_customer(file):
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="55555"
    )
    id_cus, name_comp, name_cont = file

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (id_cus,
                                                                          name_comp,
                                                                          name_cont))

    finally:
        conn.close()


def write_in_employees(file):
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="55555"
    )
    employee_id, first_name, last_name, title, birth_date, notes = file

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (employee_id,
                                                                                      first_name,
                                                                                      last_name,
                                                                                      title,
                                                                                      birth_date,
                                                                                      notes
                                                                                      ))

    finally:
        conn.close()


def write_in_orders(file):
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="55555"
    )
    order_id, customer_id, employee_id, order_date, ship_city = file

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (order_id,
                                                                                customer_id,
                                                                                employee_id,
                                                                                order_date,
                                                                                ship_city
                                                                                ))

    finally:
        conn.close()
