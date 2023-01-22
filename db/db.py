import sqlite3


try:
    PATH = "db.sqlite"

    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
except sqlite3.Error as exc:
    print(exc)


# def is_user_exist(user_id):
#     query = cur.execute("SELECT * FROM users WHERE user_telegram_id = ?", (user_id,))
#     exist_tables = query.fetchall()
#     print(exist_tables)
#
#     return True if exist_tables else False
#
# print(is_user_exist("123"))


def add_new_user(user_id):
    try:
        cur.execute("INSERT INTO users (telegram_id) VALUES (?)", (user_id,))
        conn.commit()
    except sqlite3.IntegrityError:
        return None


def get_drink_types():
    query = cur.execute("SELECT type FROM drink_types")
    drinks = query.fetchall()

    return [i[0] for i in drinks]


async def add_statistics(state):
    async with state.proxy() as data:
        add_new_user(data['tg_id'])

        cur.execute("""INSERT INTO statistics (user_id, drink_id, date, quantity, price) VALUES (
                    (SELECT id FROM users WHERE telegram_id = ?),
                    (SELECT id FROM drink_types WHERE type = ?), (?), (?), (?))""", tuple(data.values()))
        conn.commit()


