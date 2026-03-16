import json
import os

DB_FILE = "planner.json"

def get_data():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content: return []
            data = json.loads(content)
            # Перевірка: якщо там словник (старий формат), скидаємо на список
            return data if isinstance(data, list) else []
    except:
        return []

def save(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_task(tasks):
    print("\n--- Нова подія ---")
    
    # Визначаємо ID безпечно
    if tasks and isinstance(tasks[-1], dict) and 'id' in tasks[-1]:
        idx = tasks[-1]['id'] + 1
    else:
        idx = 1
    
    item = {
        "id": idx,
        "title": input("Що плануємо? "),
        "day": input("Дата: "),
        "time": input("Час: "),
        "note": input("Деталі: ")
    }
    
    tasks.append(item)
    save(tasks)
    print("👍 Збережено")

def list_tasks(tasks):
    if not tasks:
        print("\nСписок порожній :(")
        return

    print(f"\n{'ID':<3} | {'Коли':<10} | {'Що робити'}")
    print("-" * 35)
    for t in tasks:
        # Перевірка на випадок бітого елемента в списку
        if isinstance(t, dict):
            print(f"\033[94m{t.get('id', '?'):<3}\033[0m | {t.get('day', '')} {t.get('time', '')} | \033[1m{t.get('title', 'Без назви')}\033[0m")

def delete_task(tasks):
    try:
        val = input("\nЯкий ID видаляємо? ")
        if not val: return
        num = int(val)
        
        new_list = [t for t in tasks if isinstance(t, dict) and t.get('id') != num]
        
        if len(new_list) == len(tasks):
            print("Не знайшов такого ID")
        else:
            tasks[:] = new_list
            save(tasks)
            print(f"Запис {num} видалено")
    except ValueError:
        print("Треба ввести саме число!")

def main():
    data = get_data()
    
    while True:
        print("\n1. Додати | 2. Глянути | 3. Видалити | 0. Вихід")
        cmd = input("Вибір: ").strip()

        if cmd == "1":
            add_task(data)
        elif cmd == "2":
            list_tasks(data)
        elif cmd == "3":
            delete_task(data)
        elif cmd in ("0", "exit", "quit"):
            print("Бувай!")
            break
        elif not cmd:
            continue
        else:
            print("Ем, спробуй ще раз")

if __name__ == "__main__":
    main()