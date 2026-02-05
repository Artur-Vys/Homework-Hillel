import os

# --- ЗАВДАННЯ 1: Запитай число (цикл до перемоги) ---
print("--- 1. Перевірка на число ---")
while True:
    try:
        user_num = float(input("Введіть будь-яке число: "))
        print(f"Дякую! Ви ввели число {user_num}")
        break  # Виходимо з циклу, якщо ввід правильний
    except ValueError:
        print("Помилка! Це не число. Спробуйте ще раз.")

print("\n" + "-"*30 + "\n")

# --- ЗАВДАННЯ 2: Калькулятор з меню та обробкою помилок ---
print("--- 2. Калькулятор ---")
print("Меню:\n1 — Додати (+)\n2 — Відняти (-)\n3 — Помножити (*)\n4 — Поділити (/)")

try:
    choice = input("Оберіть дію (1-4): ")
    if choice in ['1', '2', '3', '4']:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        
        if choice == '1': print(f"Результат: {a + b}")
        elif choice == '2': print(f"Результат: {a - b}")
        elif choice == '3': print(f"Результат: {a * b}")
        elif choice == '4':
            try:
                print(f"Результат: {a / b}")
            except ZeroDivisionError:
                print("Помилка: Ділити на нуль не можна!")
    else:
        print("Помилка: Такого пункту в меню немає.")
except ValueError:
    print("Помилка: Потрібно було ввести цифри.")

print("\n" + "-"*30 + "\n")

# --- ЗАВДАННЯ 3: Ім'я та вік (1-120) ---
print("--- 3. Валідація віку ---")
name = input("Як вас звати? ")
try:
    age = int(input("Скільки вам років? "))
    if 1 <= age <= 120:
        print(f"Привіт, {name}! Ваш вік {age} прийнято.")
    else:
        print("Помилка: Вік має бути від 1 до 120 років.")
except ValueError:
    print("Помилка: Вік має бути числом.")

print("\n" + "-"*30 + "\n")

# --- ЗАВДАННЯ 4: Робота зі списком (індекс) ---
print("--- 4. Пошук за індексом ---")
numbers = [10, 20, 30, 40, 50]
print(f"Є список із 5 чисел. Індекси від 0 до 4.")
try:
    idx = int(input("Введіть індекс, щоб побачити число: "))
    print(f"Під індексом {idx} лежить число {numbers[idx]}")
except IndexError:
    print("Помилка: Такого індексу не існує (виберіть 0-4).")
except ValueError:
    print("Помилка: Введіть ціле число.")

print("\n" + "-"*30 + "\n")

# --- ЗАВДАННЯ 5: Читання файлу (без падіння) ---
print("--- 5. Безпечне читання файлу ---")
file_name = "data.txt"
try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        print("Вміст файлу:", content)
except FileNotFoundError:
    print(f"Попередження: Файл '{file_name}' не знайдено, але програма працює далі.")

print("\n" + "-"*30 + "\n")

# --- ЗАВДАННЯ 6: Конвертер валют (USD -> UAH) ---
print("--- 6. Конвертер валют (Курс 41.5) ---")
try:
    usd = float(input("Введіть суму в USD: "))
    if usd < 0:
        print("Помилка: Сума не може бути від'ємною.")
    else:
        print(f"Це буде {round(usd * 41.5, 2)} UAH")
except ValueError:
    print("Помилка: Неправильний формат суми.")

print("\n" + "-"*30 + "\n")

# --- ЗАВДАННЯ 7: Своя програма (Міні-Магазин) ---
print("--- 7. Творча програма: Каса магазину ---")
# Тут мінімум 3 try/except (вони вкладені або послідовні)
try:
    price = float(input("Введіть ціну товару: "))
    try:
        count = int(input("Введіть кількість: "))
        total = price * count
        print(f"Загальна вартість: {total}")
        
        try:
            money = float(input("Скільки грошей дає покупець? "))
            if money >= total:
                print(f"Решта: {money - total}")
            else:
                print("Недостатньо грошей!")
        except ValueError:
            print("Помилка в сумі грошей.")
            
    except ValueError:
        print("Помилка в кількості товару.")
except ValueError:
    print("Помилка в ціні товару.")

print("\nВсі завдання завершено!")