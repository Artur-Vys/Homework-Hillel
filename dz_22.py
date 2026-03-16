import sqlite3

# База даних
db = sqlite3.connect('planner.db')
cur = db.cursor()

# Створюємо таблицю, якщо її немає
cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, date TEXT, time TEXT, info TEXT)")
db.commit()

def add():
    print("\n--- Додавання справи ---")
    t = input("Назва: ")
    d = input("Дата: ")
    tm = input("Час: ")
    i = input("Опис: ")
    
    cur.execute("INSERT INTO tasks (title, date, time, info) VALUES (?, ?, ?, ?)", (t, d, tm, i))
    db.commit()
    print("Ок, записав.")

def show():
    cur.execute("SELECT * FROM tasks")
    res = cur.fetchall()
    
    if not res:
        print("\nТут пусто.")
        return

    print("\nID | Коли | Що")
    for r in res:
        print(f"{r[0]} | {r[2]} {r[3]} | {r[1]}")

def delete():
    idx = input("\nЯкий ID видалити? ")
    cur.execute("DELETE FROM tasks WHERE id = ?", (idx,))
    db.commit()
    print(f"Запис {idx} видалено.")

while True:
    print("\n1. Додати, 2. Список, 3. Видалити, 0. Вихід")
    choice = input("> ")

    if choice == '1':
        add()
    elif choice == '2':
        show()
    elif choice == '3':
        delete()
    elif choice == '0':
        break
    else:
        print("Нема такої команди.")

db.close()