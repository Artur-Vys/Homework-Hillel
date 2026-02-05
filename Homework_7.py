# --- 1. Функция Калькулятор ---
def calc(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Ошибка: деление на 0"

print("1. Результат калькулятора (90 * 5)=", calc(90, 5, "*"))


# --- 2. Lambda: Последняя цифра числа ---
# abs(x) нужен на случай, если число отрицательное
get_last_digit = lambda x: abs(x) % 10

print("2. Последняя цифра числа 157:", get_last_digit(157))


# --- 3. Map и Lambda: Квадраты чисел ---
numbers = [2, 4, 6, 8]
squares = list(map(lambda x: x**2, numbers))

print("3. Список квадратов:", squares)


# --- 4. Filter: Слова длиннее 5 символов ---
words = ["дом", "программа", "код", "питон", "ноутбук"]
long_words = list(filter(lambda w: len(w) > 5, words))

print("4. Слова длиннее 5 символов:", long_words)


# --- 5. Сортировка списка словарей ⭐ ---
students = [
    {"name": "Ivan", "age": 18},
    {"name": "Olya", "age": 20},
    {"name": "Max", "age": 17}
]

# Ключ сортировки — возраст из каждого словаря
sorted_students = sorted(students, key=lambda s: s["age"])

print("5. Сортировка студентов по возрасту:")
for student in sorted_students:
    print(f"   - {student['name']}: {student['age']}")