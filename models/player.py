from models.atac import Shoot
from models.entity import LivingEntity
from models.weapon import Automat, Pistol, Shotgun, Weapon


class Player(LivingEntity):
    def __init__(self, energy=350, **kwargs) -> None:
        super().__init__(**kwargs)
        self.energy = energy
        self._is_siting = False
        self._is_runing = False
        self.max_energy = energy
        self.weapon_list = list[Weapon]
        self.current_weapon = Pistol(self)
        self.speed = 10

    def set_weapon(self, weapon: Weapon) -> None:
        self.current_weapon = weapon

    def shoot(self) -> list[Shoot] | None:
        if self._is_siting:
            return None
        self.shoot_position = self.direction
        if self.current_weapon.timer is None:
            return self.current_weapon.shoot()
    
    def move(self) -> None:
        if self._is_siting:
            self.position_x += int(self.speed / 4) * self.direction
        elif self._is_runing:
            self.position_x += self.speed * self.direction * 2
            self.energy -= 10
        else:
            self.position_x += (self.speed - (0 if self.energy > 500 else 3)) * self.direction
    
    def sit(self, type: bool) -> None:
        if type:
            if not self._is_siting:
                height = int(self.height / 2)
                self.height = height
                self.position_y += height
            self._is_siting = True
        elif not type and self._is_siting:
            if self._is_siting:
                self.position_y -=  self.height
                self.height *= 2
            self._is_siting = False

    def set_energy(self, energy):
        self.energy = energy if energy < self.max_energy else self.max_energy

    @property
    def is_runing(self):
        return self._is_runing

    def set_run(self, type: bool) -> None:
        self._is_runing = type