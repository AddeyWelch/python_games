import random
import time
from gladiator import Gladiator

max1 = random.randint(11, 20)
min1 = random.randint(5, 10)
max2 = random.randint(11, 20)
min2 = random.randint(5, 10)

player_1 = Gladiator(100, 0, min1, max1)
player_2 = Gladiator(100, 0, min2, max2)


def turn1():
    # what action do you want to do?
    action = input('What action do you want to complete?\n').strip().lower()
    if action == 'attack':
        return player_1.attack(player_2)
    elif action == 'heal':
        return player_1.heal()


def turn2():
    # what action do you want to do?
    action = input('What action do you want to complete?\n').strip().lower()
    if action == 'attack':
        return player_2.attack(player_1)
    elif action == 'heal':
        return player_2.heal()


print("""  ▄▄▄▄    ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████
▓█████▄ ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀
▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███
▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄
░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░
▒░▒   ░   ▒   ▒▒ ░   ░        ░    ░ ░ ▒  ░ ░ ░  ░
 ░    ░   ░   ▒    ░        ░        ░ ░      ░
 ░            ░  ░                     ░  ░   ░  ░
      ░                                            """)
time.sleep(1)
print("""  _____
|___ |
    / /
    \ |
.___/ /
\____/
        """)
time.sleep(1)
print("""  _____
/ __  |
`' / /'
  / /
./ /___
\_____/
        """)
time.sleep(1)
print("""  __
/  |
`| |
 | |
_| |_
\___/ """)
time.sleep(1)
print("""  _ ___  __    ___
 |_  |  /__ |_| |
 |  _|_ \_| | | | """)
print('_' * 50)
print('\n')


def show():
    linef = "{0:<20}  {1:<20}"
    print(linef.format('PLAYER 1:', 'PLAYER 2: '))
    print(linef.format('Health: {0}'.format(player_1.health),
                       'Health: {0}'.format(player_2.health)))
    print(linef.format('Rage: {0}'.format(player_1.rage), 'Rage: {0}'.format(
        player_2.rage)))
    print('_' * 50)
    print('\n')


show()
while (player_1.is_dead() or player_2.is_dead()) is False:
    turn1()
    if player_1.is_dead():
        print('\n**PLAYER 2 IS DEAD, PLAYER 1 WINS!**')
        break
    elif player_2.is_dead():
        print('\n**PLAYER 1 IS DEAD, PLAYER 2 WINS!**')
        break
    print('\n')
    show()

    turn2()
    if player_1.is_dead():
        print('\n**PLAYER 2 IS DEAD, PLAYER 1 WINS!**')
        break
    elif player_2.is_dead():
        print('\n**PLAYER 1 IS DEAD, PLAYER 2 WINS!**')
        break
    print('\n')
    show()
