class BankAccount:
    def __init__(self, start_money):
        self.__balance = start_money

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if money <= self.__balance:
            self.__balance -= money
        else:
            print("Денег нет!")

    @property
    def balance(self):
        return self.__balance

class UserProfile:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, val):
        if "@" in val:
            self.__email = val
        else:
            print("Кривой email")

class Battery:
    def __init__(self, charge):
        self.__charge = charge

    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, val):
        if 0 <= val <= 100:
            self.__charge = val

class Speaker:
    def __init__(self, vol):
        self.__volume = vol

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, val):
        if 0 <= val <= 10:
            self.__volume = val

class Character:
    def __init__(self, hp):
        self.__health = hp

    def damage(self, val):
        self.__health = max(0, self.__health - val)

    def heal(self, val):
        self.__health = min(100, self.__health + val)

    @property
    def health(self):
        return self.__health

class PasswordManager:
    def __init__(self, pwd):
        self.__pwd = pwd

    def change_password(self, old, new):
        if old == self.__pwd and len(new) >= 8:
            self.__pwd = new
            print("Пароль изменен")
        else:
            print("Ошибка смены пароля")

# Проверка, чтобы в терминале был виден результат
if __name__ == "__main__":
    # Банк
    my_bank = BankAccount(1000)
    my_bank.deposit(500)
    print("В банке:", my_bank.balance)

    # Юзер
    me = UserProfile("admin@mail.com")
    me.email = "bad_mail" # Выдаст ошибку
    print("Почта:", me.email)

    # Батарея
    phone = Battery(50)
    phone.charge = 80
    print("Заряд:", phone.charge)

    # Персонаж
    hero = Character(100)
    hero.damage(40)
    print("ХП:", hero.health)

    # Пароль
    manage = PasswordManager("super_secret")
    manage.change_password("super_secret", "new_pass_123")