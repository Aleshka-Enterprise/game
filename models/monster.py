from models.atac import Atac, Shoot
from models.entity import LivingEntity
from models.weapon import Automat, Pistol, Shotgun, Weapon


class Monster(LivingEntity):
    def __init__(self, target, **kwargs) -> None:
        super().__init__(**kwargs)
        self._is_siting = False
        self.weapon = Shotgun(self)
        self.atac_list: list[Atac] = []
        self.target = target
        self.speed = 3
        self.color = (125, 125, 125)

    def set_weapon(self, weapon: Weapon) -> None:
        self.current_weapon = weapon

    def shoot(self) -> list[Shoot] | None:
        self.shoot_position = self.direction
        if self.current_weapon.timer is None:
            return self.current_weapon.shoot()
    
    def move(self) -> None:
            self.position_x += self.speed * (-1 if self.position_x > self.target.position_x else 1)
    
    def sit(self, type: bool) -> None:
        if (type):
            self._is_siting = True


class Zombie(Monster):
    def __init__(self, target, **kwargs) -> None:
        super().__init__(target, **kwargs)
        self.color = (125, 125, 125)
        self.speed = 3