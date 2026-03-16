import sqlite3

def init_db():
    # Коннектимось (файл створиться сам)
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    
    # Створюємо таблицю, якщо її ще нема
    cur.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def add_books(conn):
    cur = conn.cursor()
    # Перевіримо, чи таблиця порожня, щоб не дублювати книги щоразу
    cur.execute("SELECT COUNT(*) FROM books")
    if cur.fetchone()[0] == 0:
        books = [
            ('Кобзар', 'Тарас Шевченко'),
            ('1984', 'Джордж Орвелл'),
            ('Відьмак', 'Анджей Сапковський')
        ]
        cur.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books)
        conn.commit()
        print("--- Книги додано ---")

def show_books(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    
    print("\n Список книг:")
    print(f"{'ID':<3} | {'Назва':<15} | {'Автор'}")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<15} | {row[2]}")

def delete_book(conn):
    try:
        book_id = int(input("\nВведіть ID книги для видалення: "))
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"✅ Книгу з ID {book_id} видалено.")
        else:
            print("❌ Книги з таким ID не знайдено.")
    except ValueError:
        print("Потрібно ввести число!")

def main():
    db = init_db()
    
    add_books(db)
    
    show_books(db)
    
    delete_book(db)
    
 
    show_books(db)
    
    db.close()

if __name__ == "__main__":
    main()