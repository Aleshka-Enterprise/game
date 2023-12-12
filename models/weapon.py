import abc
from models.atac import Shoot
from models.entity import BaseEntity

class Weapon(abc.ABC):
    def __init__(self, entity: BaseEntity) -> None:
        self.height = 5
        self.width = 20
        self.speed = 10
        self.color = (0, 0, 0)
        self.timer = None
        self.entity = entity
        self.damage = 10
    
    def move(self):
        self.x += self.speed * self.direction

    def update_timer(self):
        if not self.timer is None:
            self.timer -= 1
            if self.timer <= 0:
                self.timer = None

    @abc.abstractmethod
    def shoot(self):
        pass


class Pistol(Weapon):
    def __init__(self, entity: BaseEntity) -> None:
        super().__init__(entity)
        self.timer = None

    def shoot(self):
        self.is_shooting = True
        self.shoot_position = self.entity.direction
        if self.timer is None:
            self.timer = 30
            return [Shoot(direction=self.entity.direction, position_x=self.entity.position_x, position_y=self.entity.position_y + 20, player_shoot=True)]


class Shotgun(Weapon):
    def __init__(self, entity: BaseEntity) -> None:
        super().__init__(entity)
        self.timer = None
        self.damage = 10

    def shoot(self):
        self.is_shooting = True
        self.shoot_position = self.entity.direction
        if self.timer is None:
            self.timer = 90
            x = self.entity.position_x
            y = self.entity.position_y
            direction = self.entity.direction
            return [
                Shoot(direction=direction, position_x=x + 10, position_y=y + 10, player_shoot=True),
                Shoot(direction=direction, position_x=x, position_y=y + 20, player_shoot=True),
                Shoot(direction=direction, position_x=x + 20, position_y=y + 30, player_shoot=True),
                ]