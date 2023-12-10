from uuid import uuid4

class BaseEntity:
    def __init__(self, direction, position_x, position_y, width=20, height=6, color=((0, 0, 250)), damage=0, speed=0) -> None:
        self.direction = direction
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color
        self.damage = damage
        self.speed = speed

    def update_position(self, position_x, position_y):
        self.position_x = position_x or self.position_x
        self.position_y = position_y or self.position_y

    def move(self):
        self.position_x += self.speed * self.direction


class LivingEntity(BaseEntity):
    def __init__(self, hp, direction, position_x, position_y, width=20, height=6, damage=0, speed=0, color=[0, 0, 0]) -> None:
        super().__init__(direction, position_x, position_y, width, height, color, damage, speed)
        self.uuid: str = uuid4()
        self.hp: int = hp
        self.position_x: int = position_x
        self.position_y: int = position_y
        self.gravity: int = 25
        self.timer: None | int = None
        # Атакует ли объект и тип атаки
        self._atac: int = 0
        self.jump: int = 0

    def set_damage(self, damage):
        self.hp -= damage

    def update_timer(self):
        if not self.timer is None:
            self.timer -= 1
            if self.timer <= 0:
                self.timer = None

    def set_timer(self, timer):
        self.timer = timer

    @property
    def atac(self):
        return self._atac
    
    @property
    def direction_t(self):
        return self.direction
    

class Shoot(BaseEntity):
    def __init__(self, direction, position_x, position_y, player_shoot: bool, width=20, height=6, color=(0, 0, 250), speed=25) -> None:
        super().__init__(direction, position_x, position_y, width, height, color, speed)
        self.player_shoot = player_shoot
        self.speed = speed
    
    def move(self):
        return super().move()

