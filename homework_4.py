# # Пункт 1
#
# with sqlite3.connect("data_base.db") as db:
#     cursor = db.cursor()
#
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             email TEXT
#         )
#     ''')
#
#     cursor.execute('''
#             INSERT INTO users (name, email)
#             VALUES
#             ('John', 'john1904@gmail.com'),
#             ('Ivan', 'ivanpetrenko99065@gmail.com'),
#             ('Petya', 'petya_krasnov84@ukr.net')
#         ''')
#
#     cursor.execute('''
#         SELECT name
#         FROM users
#         WHERE email LIKE '%@gmail.com'
#     ''')
#
#     gmail_users = cursor.fetchall()
#
#     for user in gmail_users:
#         print(user[0])
# Пункт 2

import sqlite3

with sqlite3.connect('toy_shop.db') as db:
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS toys (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT,
            price REAL,
            stock_quantity INTEGER
        )
    ''')

    cursor.execute("INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)",
                   ("М'яка ведмедиця", "м'яка іграшка", 25.99, 50))

    cursor.execute("INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)",
                   ("М'яка кішка", "м'яка іграшка", 10.99, 25))

    cursor.execute("INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)",
                   ("М'який пес", "м'яка іграшка", 12.99, 7))

    # cursor.execute("DELETE FROM toys WHERE stock_quantity <= 0")
    #
    #
    # cursor.execute('''
    #     SELECT *
    #     FROM toys
    #     WHERE type = "м'яка іграшка"
    #     ORDER BY price DESC;
    # ''')
    #
    # soft_toys = cursor.fetchall()
    #
    # for toy in soft_toys:
    #     print(toy)

    # Пункт 3
    # cursor.execute('''
    #         SELECT ROUND(AVG(price), 2)
    #         FROM toys
    #         WHERE type = "м'яка іграшка";
    #     ''')
    # average_price = cursor.fetchone()[0]
    # print("Середня ціна іграшок", average_price)

    # Пункт 4
    # cursor.execute('''
    # SELECT MAX(price)
    # FROM toys;
    # ''')
    # max_price = cursor.fetchone()[0]
    # print("Максимальна ціна іграшки", max_price)

    # Пункт 5
    # cursor.execute('''
    # SELECT MIN(price)
    # FROM toys;
    # ''')
    # min_price = cursor.fetchone()[0]
    # print("Мінімальна ціна іграшки", min_price)

    # Пункт 6
    # cursor.execute('''
    #         SELECT name, price,
    #         CASE
    #             WHEN price < 10 THEN 'Економна'
    #             WHEN price >= 10 AND price < 20 THEN 'Середня'
    #             WHEN price >= 20 AND price < 30 THEN 'Висока'
    #             ELSE 'Дуже висока'
    #         END AS price_category
    #         FROM toys
    #         WHERE type = "м'яка іграшка";
    #     ''')
    #
    # results = cursor.fetchall()
    #
    # for row in results:
    #     name, price, price_category = row
    #     print(f"Назва: {name}, Ціна: {price}, Категорія ціни: {price_category}")

    # Пункт 7
    # cursor.execute('''
    #         SELECT name, stock_quantity,
    #         CASE
    #             WHEN stock_quantity > 50 THEN '10%'
    #             WHEN stock_quantity >= 20 AND stock_quantity <= 50 THEN '5%'
    #             ELSE '0%'
    #         END AS discount
    #         FROM toys;
    #     ''')
    #
    # results = cursor.fetchall()
    #
    # for row in results:
    #     name, stock_quantity, discount = row
    #     print(f"Назва: {name}, Кількість на складі: {stock_quantity}, Знижка: {discount}")
