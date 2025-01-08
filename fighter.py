from abc import ABC, abstractmethod


# Абстрактный класс для оружия
class Weapon(ABC):
    # Абстрактный метод атаки
    @abstractmethod
    def attack(self):
        pass


# Класс для меча
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


# Класс для лука
class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


# Класс бойца
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} сменил оружие.")

    def fight(self, monster):
        print(self.weapon.attack())
        monster.take_damage()
        if monster.is_defeated():
            print("Монстр побежден!")
        else:
            print("Монстр еще жив!")


# Класс монстра
class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self):
        self.health -= 1  # Уменьшаем здоровье на 1

    def is_defeated(self):
        return self.health <= 0


# Пример использования
if __name__ == "__main__":
    # Создаем монстра с 2 единицами здоровья
    monster = Monster(health=2)

    # Создаем бойца с мечом
    fighter = Fighter(name="Артур", weapon=Sword())

    print("Боец выбирает меч.")
    fighter.fight(monster)  # Первый бой

    # Смена оружия на лук
    fighter.change_weapon(Bow())
    print("Боец выбирает лук.")
    fighter.fight(monster)  # Второй бой