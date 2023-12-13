import pygame
from models.atac import Shoot
from models.monster import Monster, Zombie
from models.player import Player
from settings import keys

shoot_list: list[Shoot] = []
entity_list: list[Monster] = []
player = Player(hp=350, position_x=500, position_y=600, direction=1, height=100, width=50, color=[255, 0, 0])
entity_list.append(Zombie(target=player, hp=350, position_x=1500, position_y=600, direction=1, height=100, width=50))

running = True
clock = pygame.time.Clock()

def check_pressed_keys(keys_list: dict[str, list[int]], pressed_keys) -> bool:
    """Проверка была ли нажата кнопка"""
    return any(map(lambda x: pressed_keys[x], keys_list))


def player_events(pressed_keys) -> None:
    """ Обработчик событй игрока """

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

    # Обрабочик выстрелов
    if check_pressed_keys(keys['shoot'], pressed_keys):
        shoots = player.shoot()
        if shoots:
            for shoot in shoots:
                shoot_list.append(shoot)

    # Обрабочик приседания
    if check_pressed_keys(keys['dow'], pressed_keys) and not player._is_siting:
        player.sit(True)
    elif player._is_siting and not check_pressed_keys(keys['dow'], pressed_keys):
        player.sit(False)

def render_and_update(window: pygame.Surface) -> None:
    """ Отрисовка и обновление """
    weapon = player.current_weapon
    player.set_energy(player.energy + 1)

    # Отрисовка локации
    pygame.draw.rect(window, (25, 150, 250), (0, 0, 1500, 800))
    pygame.draw.rect(window, (0, 250, 0), (0, 700, 1500, 100))

    # Отрисовка интерфейса игрока
    pygame.draw.rect(window, (0, 0, 0), (1090, 40, 360, 50))
    pygame.draw.rect(window, (0, 250, 0), (1100, 100, player.energy, 20))
    pygame.draw.rect(window, (255, 30, 0), (1100, 50, player.hp, 40))

    # Отрисовка игрока
    if not player._is_siting:
        if (weapon.entity.direction == 1):
            ofset = 10 if not weapon.timer is None else 0
            weapon_x = weapon.entity.position_x + (weapon.entity.width * weapon.entity.direction) - ofset
        else:
            ofset = 10 if not weapon.timer is None else 0
            weapon_x =  weapon.entity.position_x - weapon.width + ofset
        weapon_y = weapon.entity.position_y + 20
        pygame.draw.rect(window, weapon.color, (weapon_x, weapon_y, weapon.width, weapon.height))
    pygame.draw.rect(window, player.color, (player.position_x, player.position_y, player.width, player.height))

    # Отрисовывает выстрелы
    for value in shoot_list:
        if -10 < value.position_x < 1550:
            pygame.draw.rect(window, value.color, (value.position_x, value.position_y, value.width, value.height))
            value.move()
        else:
            shoot_list.remove(value)
    
    weapon.update_timer()

    for monster in entity_list:
        pygame.draw.rect(window, monster.color, (monster.position_x, monster.position_y, monster.width, monster.height))
        monster.move()

    for shoot in shoot_list:
        for monster in entity_list:
            is_damaged = shoot.check_collision(monster)
            if (is_damaged):
                shoot_list.remove(shoot)
            if monster.hp < 0:
                entity_list.remove(monster)

# Основной игровой цикл
while player.hp > 0 and running:
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