import sqlite3


try:
    PATH = "db.sqlite"

    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
except sqlite3.Error as exc:
    print(exc)


def is_user_exist(user_id: str):
    query = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    exist_tables = query.fetchall()

    return True if (user_id,) in exist_tables else False


def create_new_table(user_id: str):
    if not is_user_exist(user_id):
        cur.executescript(f"CREATE TABLE IF NOT EXISTS [{user_id}](drink TEXT, date TEXT, count REAL, price REAL)")


async def add_record(user_id: str, state):
    if not is_user_exist(user_id):
        create_new_table(user_id)

    async with state.proxy() as data:
        cur.execute(f"INSERT INTO [{user_id}] (drink, date, count, price) VALUES (?, ?, ?, ?)", tuple(data.values()))
        conn.commit()
