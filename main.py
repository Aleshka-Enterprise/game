import pygame
from models.atac import Shoot
from models.player import Player
from settings import keys
from pygame.sprite import Group

player = Player(hp=350, position_x=500, position_y=600, direction=1, height=100, width=50, color=[255, 0, 0], speed=10)
shoot_list: list[Shoot] = []
shoot_group = Group()

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

def check_pressed_keys(keys_list: dict[str, list[int]], pressed_keys) -> bool:
    """Проверка была ли нажата кнопка"""
    return any(map(lambda x: pressed_keys[x], keys_list))


def player_events(pressed_keys) -> None:
    """ Обработчик событй игрока """
    players_shoots = list(filter(lambda shoot: shoot.player_shoot, shoot_list))

    # Обработчик движения игрока
    if player.position_x <= 1440 and check_pressed_keys(keys['right'], pressed_keys):
        player.direction = 1
        player.move()
    if player.position_x >= 10 and check_pressed_keys(keys['left'], pressed_keys):
        player.direction = -1
        player.move()

    # Обработчик бега игрока
    run_key_presed = check_pressed_keys(keys['run'], pressed_keys)
    if run_key_presed and player.energy > 50:
        player.set_run(True)
    elif player.is_runing and player.energy < 10 or not run_key_presed:
        player.set_run(False)

    # Обрабочик выстрелов игрока
    if check_pressed_keys(keys['shoot'], pressed_keys) and len(players_shoots) < 3:
        shoot = player.shoot()
        if shoot:
            for i in shoot:
                shoot_list.append(i)

def render_and_update(window: pygame.Surface) -> None:
    """ Отрисовка и обновление """
    weapon = player.current_weapon

    # Отрисовка локации
    pygame.draw.rect(window, (25, 150, 250), (0, 0, 1500, 800))
    pygame.draw.rect(window, (0, 250, 0), (0, 700, 1500, 100))

    # Отрисовка интерфейса игрока
    pygame.draw.rect(window, (0, 0, 0), (1090, 40, 360, 50))
    pygame.draw.rect(window, (0, 250, 0), (1100, 100, player.energy, 20))
    pygame.draw.rect(window, (255, 30, 0), (1100, 50, player.hp, 40))

    # Отрисовка игрока
    if (weapon.entity.direction == 1):
        weapon_x = weapon.entity.position_x + (weapon.entity.width * weapon.entity.direction)
    else:
        weapon_x =  weapon.entity.position_x - weapon.width
    weapon_y = weapon.entity.position_y + 20
    pygame.draw.rect(window, player.color, (player.position_x, player.position_y, player.width, player.height))
    pygame.draw.rect(window, weapon.color, (weapon_x, weapon_y, weapon.width, weapon.height))

    # Отрисовывает выстрелы
    for value in shoot_list:
        if -10 < value.position_x < 1550:
            pygame.draw.rect(window, value.color, (value.position_x, value.position_y, value.width, value.height))
            value.move()
        else:
            shoot_list.remove(value)
    
    weapon.update_timer()


while player.hp > 0 and running:
    player.set_energy(player.energy + 1)
    window = pygame.display.set_mode((1500, 800))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    player_events(pressed_keys)

    render_and_update(window)

    pygame.display.update()
    player.update_timer()
    clock.tick(60)