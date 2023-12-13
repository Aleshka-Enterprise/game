import pygame
import random
from models.entity import Entity


player = {
    'position_x': 50,
    'position_y': 600,
    'shoot': 0,
    'sits': False,
}

keys = {
    'right': [pygame.K_RIGHT, pygame.K_d],
    'left': [pygame.K_LEFT,pygame.K_a],
    'dows': [pygame.K_DOWN, pygame.K_s],
    'jump': [pygame.K_SPACE, pygame.K_w],
}

# Переменные
g = 25
shoot = 0
xs = 0
xsz = 0
ysz = 30
ys = 30
jump = 0
pos = 1
shift = 0
stanina = 350
HP = 350
zombi = True
xz = 1400
yz = 600
shootZ = 4
zombiHP = 1000
trap = 500

zemx = 500
zemy = 650
timer = 0

def check_pressed_keys(keys_list, pressed_keys):
    return any(map(lambda x: pressed_keys[x], keys_list))

def update_timer(frames):
    global timer
    timer = frames if timer == 0 else timer - 1

# Мувы
while HP > 0:

    pygame.time.delay(15)
    window = pygame.display.set_mode((1500, 800))
    pygame.draw.rect(window, (25, 150, 250), (0, 0, 1500, 800))
    pygame.draw.rect(window, (0, 250, 0), (0, 700, 1500, 100))
    if not player['sits']:
        pygame.draw.rect(window, (250, 0, 0), (player['position_x'], player['position_y'], 50, 100))
        if pos == -1:
            pygame.draw.rect(window, (0, 0, 0), (player['position_x'] - 15, player['position_y'] + 30, 20, 5))
        if pos == 1:
            pygame.draw.rect(window, (0, 0, 0), (player['position_x'] + 45, player['position_y'] + 30, 20, 5))
    pygame.event.get()
    pressed_keys = pygame.key.get_pressed()

#pressed_keys
    if player['position_x'] <= 1440 and check_pressed_keys(keys['right'], pressed_keys):
        player['position_x'] += 5 + (3 * int(not player['sits']))
        pos = 1
    if player['position_x'] >= 10 and check_pressed_keys(keys['left'], pressed_keys):
        player['position_x'] -= 5 + (3 * int(not player['sits']))
        pos = -1
        player['position_x'] -= 5 + (3 * int(not player['sits']))
        pos = -1

    if player['position_x'] <= 1440:
        if pressed_keys[pygame.K_RIGHT] and pressed_keys[pygame.K_UP]:
            if not player['sits']:
                pygame.draw.line(window,(0, 0, 0), (player['position_x'] + 25, player['position_y'] + 10),(player['position_x'] + 50, player['position_y'] - 20), (8))
                pos = 2

    if pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_LEFT]:
        if not player['sits'] and (pressed_keys[pygame.K_LEFT] and pressed_keys[pygame.K_UP]):
            pygame.draw.line(window, (0, 0, 0), (player['position_x'] + 25, player['position_y'] + 10), (player['position_x'] - 20, player['position_y'] - 20), (8))
            pos = 4
        else:
            pos = -1
    if pressed_keys[pygame.K_UP] and (pos != 2):
        if pos != 4:
            if not player['sits'] and pressed_keys[pygame.K_UP]:
                pygame.draw.line(window, (0, 0, 0), (player['position_x'] + 25, player['position_y'] + 20), (player['position_x'] + 25, player['position_y'] - 40), (8))
                pos = 3
    if pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_LEFT] and pressed_keys[pygame.K_RIGHT]:
        pygame.draw.rect(window, (0, 0, 150),(player['position_x'] + 5, player['position_y'] + 5, 40, 40))
        pygame.draw.rect(window, (0, 0, 0), (player['position_x'] + 35, player['position_y'] + 50, 10, 10))

    if jump == 0 and check_pressed_keys(keys['jump'], pressed_keys):
        if stanina > 100:
            jump = 1
            stanina -= 100
    if jump:
        player['position_y'] -= jump * 2 * g
        g -= jump * 2
        if g <= 1:
            jump = -1
        elif g >= 25:
            jump = 0
            player['position_y'] += 48

    if check_pressed_keys(keys['dows'], pressed_keys):
        player['sits'] = True
        pygame.draw.rect(window, (250, 0, 0), (player['position_x'], player['position_y'] + 70, 50, 30))
    else:
        player['sits'] = False
    if stanina >= 3 and pressed_keys[pygame.K_x] and not player['sits']:
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_RIGHT]:
            if pressed_keys[pygame.K_RIGHT] and player['position_x'] < 1440:
                player['position_x'] += 10
                stanina -= 3
            if pressed_keys[pygame.K_LEFT] and player['position_x'] > 5:
                player['position_x'] -= 10
                stanina -= 3
# СТРЕЛЬБАz
    if pressed_keys[pygame.K_z] and not player['sits']:
        shoot = 1
    if shoot == 1:
        if pos in [-1, 1]:
            pygame.draw.rect(window, (0, 0, 250), (player['position_x'] + xs * pos, player['position_y'] + ys, 20, 6))
            xs += 20
        elif pos == 2:
            pygame.draw.rect(window, (0, 0, 255), (player['position_x'] + xs, player['position_y'] - ys, 20, 6))
            xs += 20
            ys += 20
        elif pos == 3:
            pygame.draw.rect(window, (0, 0, 250), (player['position_x'] + 25, player['position_y'] - ys, 6, 20))
            ys += 20
            xs += 1
        elif pos == 4:
            pygame.draw.rect(window, (0, 0, 250), (player['position_x'] - xs, player['position_y'] - ys, 20, 6))
            xs += 20
            ys += 20

        if (xs <= 0 or xs >= 1500) or (ys <= 0 or ys >= 1500):
            shoot = 0
            xs = 0
            ys = 30
    pygame.draw.rect(window, (0, 0, 0), (1090, 40, 360, 50))
    pygame.draw.rect(window, (0, 250, 0), (1100, 100, stanina, 20))
    pygame.draw.rect(window, (255, 30, 0), (1100, 50, HP, 40))
    if stanina < 350:
        stanina += 1
# ЗОМБИ
    if zombi:
        pygame.draw.rect(window, (56, 150, 100), (xz, yz, 50, 100))
        posz = -1 if xz > player['position_x'] else 1
        xz += posz * 2
        if timer <= 0 and shootZ > 1:
            shootZ = 1
        if not shootZ in range(1, 5):
            shootZ = random.randint(1, 6)
            trap = random.randint(400, 900)
        if shootZ == 1:
            pygame.draw.rect(window, (0, 0, 255), ((xz + xsz * posz), (yz + ysz), 20, 6))
            xsz += 20
            if xsz <= 0 or xsz >= 1500:
                shootZ = 0
                xsz = 0
                ysz = 30
        if shootZ == 2:
            pygame.draw.line(window, (250, 0, 0), (posz * 1500, yz + 30), (xz, yz + 30), (60 - timer))
            xz -= posz * 2
            update_timer(60)
        if shootZ == 3:
            pygame.draw.rect(window, (0, 50, 0), (xz, yz, 50, 100))
            update_timer(100)
            if timer > 70:
                player['position_x'] -= posz * 10
                if zombiHP <= 1500:
                    zombiHP += 1
            else:
                xz += posz * 5
        if shootZ == 4:
            update_timer(50)
            pygame.draw.rect(window, (128, 128, 128), (trap, 700, 50, 10))
            if player['position_x'] <= trap + 50 and player['position_x'] >= trap:
                if player['position_y'] >= 650:
                    HP-=5

    # УРОН ОТ ЗОМБИ
        if shootZ == 2 and timer >= 35 and not player['sits']:
            HP -= 10

        if not player['sits']:
            if player['position_y'] <= yz + 30 and player['position_y'] >= yz - 60:
                if (xz - xsz <= player['position_x'] + 1 and xz - xsz >= player['position_x'] - 50):
                        HP -= 50
                if xz + xsz <= player['position_x'] + 1 and xz + xsz >= player['position_x'] - 50:
                        HP -= 50
# ВЫСТРЕЛЫ
    if shoot == 1:
        if pos == -1:
            if player['position_x'] - xs <= xz + 50 and player['position_x'] - xs >= xz - 1:
                if yz <= player['position_y'] + 30 and yz >= player['position_y'] - 60:
                    zombiHP -= 50
        if pos == 1:
            if player['position_x'] + xs <= xz + 1 and player['position_x'] + xs >= xz - 50:
                if yz <= player['position_y'] + 30 and yz >= player['position_y'] - 60:
                    zombiHP -= 50
    if xz >= player['position_x'] and xz <= player['position_x'] + 50:
        if yz >= player['position_y'] and yz <= player['position_y'] + 100:
            HP -= 3
            zombiHP += 15

    zombi = zombiHP > 0
    pygame.draw.rect(window, (200, 0, 0), (xz - 30, yz - 50, zombiHP/10, 10))
    pygame.display.update()