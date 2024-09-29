import sqlite3

from run import BASE_DIR

conn = sqlite3.connect(f'{BASE_DIR}/my_data.db')
curr = conn.cursor()


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS user (
    chat_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR(50) NOT NULL, 
    lang VARCHAR(5) NOT NULL);
    """
    curr.execute(query)


def insert(chat_id, username, lang):
    query = f"""
    INSERT INTO user (chat_id, username, lang) VALUES ("{chat_id}", "{username}", "{lang}");
    """
    with conn:
        curr.execute(query)


def update(chat_id, set_lang):
    query = f"""
    UPDATE user SET lang="{set_lang}" WHERE chat_id="{chat_id}";
    """
    with conn:
        curr.execute(query)


def select(chat_id):
    query = f"""
    SELECT lang FROM user WHERE chat_id="{chat_id}";
    """
    data = curr.execute(query).fetchone()
    return data[0]


def active_followers():
    query = """
    SELECT COUNT(*) FROM user WHERE status=False;
    """
    return curr.execute(query).fetchone()[0]
