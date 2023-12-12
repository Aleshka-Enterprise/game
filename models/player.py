from models.atac import Shoot
from models.entity import LivingEntity
from models.weapon import Pistol, Shotgun, Weapon


class Player(LivingEntity):
    def __init__(self, energy=350, **kwargs) -> None:
        super().__init__(**kwargs)
        self.energy = energy
        self._is_siting = False
        self._is_runing = False
        self.max_energy = energy
        self.weapon_list = list[Weapon]
        self.current_weapon = Shotgun(self)

    def set_weapon(self, weapon: Weapon) -> None:
        self.current_weapon = weapon

    def shoot(self) -> list[Shoot] | None:
        self.is_shooting = True
        self.shoot_position = self.direction
        if self.current_weapon.timer is None:
            return self.current_weapon.shoot()
    
    def move(self) -> None:
        if self._is_runing:
            self.position_x += self.speed * self.direction * 2
            self.energy -= 10
        else:
            self.position_x += (self.speed - (0 if self.energy > 500 else 3)) * self.direction
    
    def sit(self, type: bool) -> None:
        if (type):
            self._is_siting = True

    def set_energy(self, energy):
        self.energy = energy if energy < self.max_energy else self.max_energy

    @property
    def is_runing(self):
        return self._is_runing
    

    def set_run(self, type: bool) -> None:
        self._is_runing = type