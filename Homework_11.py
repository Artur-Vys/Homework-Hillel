import os
import json
from datetime import datetime

# --- 1. Щоденник ---
def diary_task():
    note = input("Введіть запис для щоденника: ")
    with open("diary.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {note}\n")
    print("✅ Запис збережено у diary.txt")

# --- 2. Середнє значення оцінок ---
def grades_task():
    # Спершу створимо файл, якщо його немає, для тесту
    if not os.path.exists("grades.txt"):
        with open("grades.txt", "w") as f: f.write("10, 12, 8, 9, 11")
    
    with open("grades.txt", "r") as f:
        data = f.read()
        marks = [int(m.strip()) for m in data.split(",") if m.strip()]
        if marks:
            avg = sum(marks) / len(marks)
            print(f"📊 Оцінки: {marks}\nСередній бал: {avg:.2f}")

# --- 3. Логін та пароль ---
def auth_task():
    login = input("Логін: ")
    pwd = input("Пароль: ")
    with open("users.txt", "a") as f:
        f.write(f"{login}:{pwd}\n")
    print("🔐 Дані збережено у users.txt")

# --- 4. Перевірка існування файлу ---
def check_file_task():
    fname = input("Який файл перевірити? ")
    if os.path.exists(fname):
        print(f"📁 Файл '{fname}' існує.")
        with open(fname, "r") as f:
            print("Зміст:", f.read(50), "...")
    else:
        print(f"❌ Файлу '{fname}' не знайдено.")

# --- 5. Історія калькулятора ---
def calc_task():
    try:
        a = float(input("Число А: "))
        b = float(input("Число Б: "))
        res = a + b
        log = f"{a} + {b} = {res}\n"
        with open("calc_history.txt", "a") as f:
            f.write(log)
        print(f"Результат {res} збережено в історію.")
    except ValueError:
        print("Помилка вводу!")

# --- 6. Планувальник JSON ---
def planner_task():
    event = input("Яку подію додати? ")
    plans = {"event": event, "status": "new", "time": str(datetime.now())}
    with open("planner.json", "w", encoding="utf-8") as f:
        json.dump(plans, f, indent=4, ensure_ascii=False)
    print("📆 Подію збережено у форматі JSON.")

# --- 7. Сортування ---
def sort_task():
    # Створимо файл для сортування
    items = ["Яблуко", "Банан", "Апельсин", "Груша"]
    with open("items.txt", "w") as f:
        f.write("\n".join(items))
    
    with open("items.txt", "r") as f:
        lines = f.readlines()
    
    lines.sort()
    
    with open("items_sorted.txt", "w") as f:
        f.writelines(lines)
    print("⭐ Дані відсортовано у файл items_sorted.txt")

# --- ГОЛОВНЕ МЕНЮ ---
def main():
    tasks = {
        "1": diary_task,
        "2": grades_task,
        "3": auth_task,
        "4": check_file_task,
        "5": calc_task,
        "6": planner_task,
        "7": sort_task
    }
    
    while True:
        print("\n--- Домашнє завдання (Файли) ---")
        print("1. Щоденник | 2. Оцінки | 3. Логін | 4. Перевірка | 5. Кальк | 6. JSON | 7. Сортування")
        print("0. Вихід")
        
        choice = input("\nОберіть номер завдання: ")
        if choice == "0": break
        if choice in tasks:
            tasks[choice]()
        else:
            print("Неправильний вибір!")

if __name__ == "__main__":
    main()