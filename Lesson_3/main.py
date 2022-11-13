from Lesson_2.character import Character
from berserk import Berserk
from knight import Knight

player1 = Berserk(name='Vasya', damage=10)
player2 = Knight(name='Petya', damage=15, defence=2)

print(player1)
print(player2)

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)

    print(player1)
    print(player2)