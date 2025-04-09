import random

class Mob:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return f"{self.name} (HP: {self.health}, Attack: {self.attack})"


def spawn_mobs(num_mobs):
    mob_types = [
        Mob("Скелет", 30, 5),
        Mob("Зомби", 40, 7),
        Mob("Паук", 20, 3),
        Mob("Орк", 50, 10)
    ]

    spawned_mobs = []
    for _ in range(num_mobs):
        mob = random.choice(mob_types)
        position = (random.randint(0, 100), random.randint(0, 100))  # Случайная позиция на карте
        spawned_mobs.append((mob, position))

    return spawned_mobs


# Пример спавна 5 мобов
if __name__ == "__main__":
    mobs = spawn_mobs(5)
    for mob, position in mobs:
        print(f"{mob} spawned at position {position}")
