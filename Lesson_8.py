def draw_line(length, direction, symbol):
    """
    Відображає лінію з символу.
    :param length: довжина лінії (кількість символів)
    :param direction: 'h' для горизонтальної, 'v' для вертикальної
    :param symbol: символ, з якого будується лінія
    """
    if direction.lower() == 'h':
        print(symbol * length)
    elif direction.lower() == 'v':
        for _ in range(length):
            print(symbol)
    else:
        print("Помилка: напрямок має бути 'h' (horizontal) або 'v' (vertical)")

# Приклади використання:
print("Горизонтальна лінія:")
draw_line(10, 'h', '*')

print("\nВертикальна лінія:")
draw_line(5, 'v', '#')