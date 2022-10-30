from character import Character

player1 = Character(name='Vasya', health=30, damage=4)
player2 = Character(name='Petya', health=30, damage=3)

player1.take_damage(1)

print(player1)
print(player2)

player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)