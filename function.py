import sqlite3

def Connection(DB):
    return sqlite3.connect(f"DB/{DB}.db")

def create():
    # 1я таблица
    cur = Connection("main")
    cur.execute("CREATE TABLE IF NOT EXISTS users(id_users TEXT UNIQUE ON CONFLICT IGNORE)")
    cur.commit()
    cur.close()
    # 2я таблица
    cur = Connection("slova")
    cur.execute("CREATE TABLE IF NOT EXISTS slova(slovo TEXT UNIQUE ON CONFLICT IGNORE, otvet TEXT UNIQUE ON CONFLICT IGNORE)")
    
    cur.execute(f"INSERT INTO slova (slovo, otvet) VALUES ('привет', 'hello');")
    cur.execute(f"INSERT INTO slova (slovo, otvet) VALUES ('как дела?', 'Все хорошо.');")
    cur.execute(f"INSERT INTO slova (slovo, otvet) VALUES ('что?', 'Что?');")
    cur.execute(f"INSERT INTO slova (slovo, otvet) VALUES ('проверка', 'работаю');")
    cur.execute(f"INSERT INTO slova (slovo, otvet) VALUES ('спам', 'Я не спамер!');")
    cur.execute(f"INSERT INTO slova (slovo, otvet) VALUES ('зачем?', 'зачем?');")
    cur.commit()
    cur.close()

def check_user(user_id):
    user_id = Clear_Text(user_id)
    cur = Connection("main")
    cur.execute(f"INSERT INTO users (id_users) VALUES ('{user_id}');")
    cur.commit()
    cur.close()
    return True

def select(Message_Text):
    Message_Text = Clear_Text(Message_Text)
    cur = Connection("slova")
    otvet = cur.execute(f"SELECT otvet FROM slova where slovo = '{Message_Text}'").fetchone()
    cur.close()
    return otvet

def AddNew(slovo, otvet):
    slovo = Clear_Text(slovo)
    otvet = Clear_Text(otvet)
    cur = Connection("slova")
    cur.execute(f"INSERT INTO slova (slovo, otvet) VALUES ('{slovo}', '{otvet}');")
    cur.commit()
    cur.close()
    return True


def Clear_Text(insert_text):
    return str(insert_text).replace("\\", "\\").replace("'", "\'").lower()
