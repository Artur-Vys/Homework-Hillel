import random

# --- 1. СТВОРЕННЯ ПЕРСОНАЖА ---
def create_character():
    print("=== Вітаємо у Світі Руїн ===")
    print("У вас є 10 очок для розподілу.")
    
    while True:
        try:
            strength = int(input("Скільки очок вкласти в СИЛУ (урон)? Решта піде в ЖИТТЯ: "))
            if 0 <= strength <= 10:
                hp_points = 10 - strength
                # Повертаємо словник - це зручно для передачі між функціями
                return {
                    "name": "Син Сюжету",
                    "hp": hp_points * 15 + 10, # Трохи базового HP для виживання
                    "max_hp": hp_points * 15 + 10,
                    "dmg": strength + 2,
                    "gold": 0,
                    "inventory": []
                }
            else:
                print("⚠️ Введіть число від 0 до 10!")
        except ValueError:
            print("⚠️ Будь ласка, використовуйте лише цифри.")

# --- 2. СТАТУС ТА ІНВЕНТАР ---
def show_status(player):
    print(f"\n--- ГЕРОЙ: {player['name']} ---")
    print(f"❤️ HP: {player['hp']}/{player['max_hp']} | ⚔️ Сила: {player['dmg']} | 💰 Золото: {player['gold']}")
    if player['inventory']:
        print(f"🎒 Інвентар: {', '.join(player['inventory'])}")
    print("-" * 25)

# --- 3. МЕХАНІКА БОЮ ---
def handle_fight(player, enemy_name, enemy_hp, enemy_dmg):
    print(f"\n⚔️ НАПАД: {enemy_name} (HP: {enemy_hp}, Шкода: {enemy_dmg})")
    
    while enemy_hp > 0 and player['hp'] > 0:
        action = input("\nВаша дія: (а)такувати, (в)текти: ").lower()
        
        if action == 'в':
            if random.random() > 0.4:
                print("🏃 Ви вдало втекли!")
                return True # Живий, але не переміг
            else:
                print("🐢 Ви спіткнулися! Втекти не вдалося.")

        if action == 'а' or action == 'в':
            # Хід гравця (кубик d20)
            dice = random.randint(1, 20)
            print(f"🎲 На кубику: {dice}")
            
            damage = 0
            if dice >= 18:
                print("🔥 КРИТИЧНИЙ УДАР!")
                damage = player['dmg'] * 3
            elif dice <= 4:
                print("💨 Промах...")
            else:
                damage = player['dmg'] + random.randint(1, 3)
            
            enemy_hp -= damage
            print(f"Ви нанесли {damage} шкоди.")

            if enemy_hp <= 0:
                gold_found = random.randint(5, 15)
                player['gold'] += gold_found
                print(f"🏆 {enemy_name} подоланий! Ви знайшли {gold_found} золота.")
                return True

            # Хід ворога
            print(f"👿 {enemy_name} атакує!")
            player['hp'] -= enemy_dmg
            print(f"Ваше HP: {player['hp']}")
            
    return player['hp'] > 0

# --- 4. ВИПАДКОВІ ПОДІЇ ---
def random_event(player):
    event_type = random.choice(["treasure", "rest", "nothing"])
    
    if event_type == "treasure":
        print("\n✨ Ви знайшли стару скриню!")
        player['gold'] += 10
        player['inventory'].append("Зілля")
        print("Ви отримали 10 золота та 'Зілля'.")
    elif event_type == "rest":
        print("\n🔥 Ви знайшли безпечне вогнище. HP відновлено.")
        player['hp'] = player['max_hp']
    else:
        print("\n🍃 Ви йдете порожньою дорогою. Нічого не сталось.")

# --- 5. ГОЛОВНИЙ ЦИКЛ ---
def main():
    player = create_character()
    enemies = [("Дика Криса", 20, 3), ("Орк-вигнанець", 40, 6), ("Сталевий Голем", 70, 10)]
    enemy_index = 0

    while player['hp'] > 0:
        show_status(player)
        print("\nЩо робитимете?")
        print("1. Йти далі за сюжетом")
        print("2. Дослідити околиці (випадкова подія)")
        print("3. Випити зілля (якщо є)")
        
        try:
            choice = input("Ваш вибір: ")
            
            if choice == "1":
                if enemy_index < len(enemies):
                    name, hp, dmg = enemies[enemy_index]
                    if handle_fight(player, name, hp, dmg):
                        enemy_index += 1
                        if enemy_index == len(enemies):
                            print("\n👑 ВІТАЄМО! Ви здолали всіх ворогів і врятували світ!")
                            break
                    else:
                        break # Поразка в бою
                else:
                    print("Ворогів більше немає.")
                    
            elif choice == "2":
                random_event(player)
                
            elif choice == "3":
                if "Зілля" in player['inventory']:
                    player['hp'] += 30
                    if player['hp'] > player['max_hp']: player['hp'] = player['max_hp']
                    player['inventory'].remove("Зілля")
                    print("🧪 Ви випили зілля. +30 HP!")
                else:
                    print("❌ У вас немає зілля!")
            else:
                print("⚠️ Оберіть дію зі списку.")
                
        except Exception as e:
            print(f"Помилка: {e}")

    if player['hp'] <= 0:
        print("\n💀 Гра закінчена. Ваше ім'я забудуть у пісках часу...")

if __name__ == "__main__":
    main()