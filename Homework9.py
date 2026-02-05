import random
import time
import string

# 1 и 2. Угадай число за 3 попытки
secret = random.randint(1, 10)
print("1-2. Загадал число от 1 до 10. У тебя 3 попытки!")
for attempt in range(3):
    guess = int(input("2 "))
    if guess == secret:
        print("Угадал!")
        break
    else:
        print("Мимо!")

# 3. Таймер
mins = float(input("\n3. На сколько минут завести таймер?: "))
print("Ждем...")
time.sleep(mins * 60) # Спим указанное время
print("Дзынь! Время вышло!")

# 4. Секундомер (3 замера)
print("\n4. Нажимай Enter для замера времени (всего 3 раза).")
start = time.time()
for i in range(1, 4):
    input(f"Замер {i}: ")
    print(f"Прошло: {round(time.time() - start, 2)} сек.")

# 5. Пароль (8 символов)
# Берем буквы и цифры, выбираем 8 случайных и склеиваем в строку
chars = string.ascii_letters + string.digits
password = "".join(random.sample(chars, 8))
print(f"\n5. Твой пароль: {password}")

# 6. Монетка
print(f"6. Монетка: {random.choice(['Орел', 'Решка'])}")

# 7. Время выполнения цикла
start_loop = time.time()
for x in range(1000000):
    pass
print(f"7. Миллион циклов прошли за {time.time() - start_loop} сек.")

# ⚡ Творческое: Кто быстрее нажмет?
print("\n⚡ МИНИ-ИГРА: Нажми Enter, когда увидишь БАБАХ!")
time.sleep(random.randint(2, 5))
print("БАБАХ!!!")
t1 = time.time()
input()
print(f"Твоя реакция: {round(time.time() - t1, 3)} сек.")
