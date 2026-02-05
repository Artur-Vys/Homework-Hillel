a = [1, 3, 5]
b = [2, 4, 6]

result = []

for i in range(3):
    result.append(a[i])
    result.append(b[i])

print(result)


text = input("Введи речення: ")
words = text.split()

result = []

for w in words:
    count = 0
    for x in words:
        if w == x:
            count += 1

    pair = (w, count)
    if pair not in result:
        result.append(pair)

print(result)



words = ["apple", "cat", "banana", "dog", "orange"]

long_words = []

for w in words:
    if len(w) > 4:
        long_words.append(w)

print(long_words)




products = []

for i in range(3):  # введемо 3 товари
    s = input("товар:ціна -> ")
    name, price = s.split(":")
    products.append((name, int(price)))

total = 0
for p in products:
    total += p[1]

average = total / len(products)

cheap = products[0]
for p in products:
    if p[1] < cheap[1]:
        cheap = p

print("Товари:", products)
print("Сума:", total)
print("Середня ціна:", average)
print("Найдешевший:", cheap)



t = [(1,2), (3,4), (1,2), (5,6)]

unique = []

for x in t:
    if x not in unique:
        unique.append(x)

print("ДЗ-4. Унікальні кортежі:", unique)