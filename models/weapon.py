import abc
import random
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

    def update_timer(self):
        if not self.timer is None:
            self.timer -= 1
            if self.timer <= 0:
                self.timer = None

    def _get_x(self):
        return self.entity.position_x - self.width if self.entity.direction == -1 else self.entity.position_x + self.entity.width

    @abc.abstractmethod
    def shoot(self):
        pass


class Pistol(Weapon):
    def __init__(self, entity: BaseEntity) -> None:
        super().__init__(entity)
        self.timer = None

    def shoot(self):
        self.shoot_position = self.entity.direction
        if self.timer is None:
            self.timer = 30
            return [Shoot(direction=self.entity.direction, position_x=self.entity.position_x, position_y=self.entity.position_y + 20, damage=self.damage)]


class Shotgun(Weapon):
    def __init__(self, entity: BaseEntity) -> None:
        super().__init__(entity)
        self.damage = 150
        self.color = (175, 75, 0)

    def shoot(self):
        self.shoot_position = self.entity.direction
        if self.timer is None:
            self.timer = 90
            direction = self.entity.direction
            res: list[Shoot] = []
            for _ in range(3):
                y = self.entity.position_y + 20 + random.randint(-20, 20)
                res.append(Shoot(direction=direction, position_x=self._get_x(), position_y=y, color=(0, 0, 0), width=10, damage=self.damage))
            return res
        

class Automat(Weapon):
    def __init__(self, entity: BaseEntity) -> None:
        super().__init__(entity)
        self.damage = 8
        self.speed = 10

    def shoot(self):
        self.shoot_position = self.entity.direction
        if self.timer is None:
            self.timer = 5
            y = self.entity.position_y + 20 + random.randint(-20, 20)
            direction = self.entity.direction
            return [Shoot(direction=direction, position_x=self._get_x(), position_y=y, damage=self.damage)]