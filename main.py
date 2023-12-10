import pygame
from models.entity import Shoot
from models.player import Player
from settings import keys

player = Player(hp=350, position_x=500, position_y=600, direction=1, height=100, width=50, color=[255, 0, 0], speed=10)
shoot_list: list[Shoot] = []

def check_pressed_keys(keys_list: dict[str, list[int]], pressed_keys) -> bool:
    """Проверка была ли нажата кнопка"""
    return any(map(lambda x: pressed_keys[x], keys_list))

def player_interface(window: pygame.SurfaceType):
    """Отрисовка интерфейса игрока"""
    pygame.draw.rect(window, (0, 0, 0), (1090, 40, 360, 50))
    pygame.draw.rect(window, (0, 250, 0), (1100, 100, player.energy, 20))
    pygame.draw.rect(window, (255, 30, 0), (1100, 50, player.hp, 40))

def main_location(window: pygame.SurfaceType):
    """Отрисовка локации"""
    pygame.draw.rect(window, (25, 150, 250), (0, 0, 1500, 800))
    pygame.draw.rect(window, (0, 250, 0), (0, 700, 1500, 100))

def player_move(pressed_keys) -> None:
    """Обработчик движения игрока"""
    if player.position_x <= 1440 and check_pressed_keys(keys['right'], pressed_keys):
        player.direction = 1
        player.move()
    if player.position_x >= 10 and check_pressed_keys(keys['left'], pressed_keys):
        player.direction = -1
        player.move()

def player_run(pressed_keys) -> None:
    """Обработчик бега игрока"""
    run_key_presed = check_pressed_keys(keys['run'], pressed_keys)
    if run_key_presed and player.energy > 50:
        player.set_run(True)
    elif player.is_runing and player.energy < 10 or not run_key_presed:
        player.set_run(False)

def player_shoot(pressed_keys) -> None:
    """Обрабочик выстрелов игрока"""
    players_shoots = [*filter(lambda shoot: shoot.player_shoot, shoot_list)]
    if check_pressed_keys(keys['shoot'], pressed_keys) and len(players_shoots) < 3:
        shoot = player.shoot()
        if shoot:
            shoot_list.append(shoot)

def display_shoots(window) -> None:
    """Отрисовывает выстрелы"""
    for value in shoot_list:
        if -10 < value.position_x < 1550:
            pygame.draw.rect(window, value.color, (value.position_x, value.position_y, value.width, value.height))
            value.move()
        else:
            shoot_list.remove(value)

while player.hp > 0:
    player.set_energy(player.energy + 1)

    pygame.time.delay(15)
    window = pygame.display.set_mode((1500, 800))
    pygame.event.get()

    pressed_keys = pygame.key.get_pressed()

    player_move(pressed_keys)
    player_run(pressed_keys)
    player_shoot(pressed_keys)

    main_location(window)
    player_interface(window)
    display_shoots(window)

    pygame.draw.rect(window, player.color, (player.position_x, player.position_y, player.width, player.height))
    pygame.display.update()
    player.update_timer()