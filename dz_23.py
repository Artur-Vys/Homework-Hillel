import tkinter as tk
import random

root = tk.Tk()
root.title("Камінь-ножиці-папір")
root.geometry("350x300")

# список варіантів
items = ['Камінь', 'Ножиці', 'Папір']

def start(u):
    c = random.choice(items)
    
    if u == c:
        res = "Нічия"
    elif (u == 'Камінь' and c == 'Ножиці') or (u == 'Ножиці' and c == 'Папір') or (u == 'Папір' and c == 'Камінь'):
        res = "Ти виграв!"
    else:
        res = "Ти програв..."

    # міняємо текст у лейблах
    rezult_label.config(text=res)
    comp_label.config(text="Комп обрав: " + c)

# Текст зверху
tk.Label(root, text="Граймо!", font=("Arial", 15)).pack(pady=10)

# Кнопки робимо по-простому
btn1 = tk.Button(root, text="Камінь", width=15, command=lambda: start("Камінь"))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Ножиці", width=15, command=lambda: start("Ножиці"))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Папір", width=15, command=lambda: start("Папір"))
btn3.pack(pady=5)

# Сюди пишемо результат
comp_label = tk.Label(root, text="")
comp_label.pack(pady=10)

rezult_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
rezult_label.pack()

root.mainloop()