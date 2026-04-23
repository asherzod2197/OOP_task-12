class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, damage):
        self.health -= damage
        print(f"{self.name} zarar oldi: {self.health} HP qoldi")

    def heal(self, amount):
        self.health += amount
        print(f"Tiklandi: {self.health} HP")


# Obyekt
hero = GameCharacter("Ali", 100)
hero.attack(30)
hero.heal(20)
