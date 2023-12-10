from models.entity import LivingEntity, Shoot


class Player(LivingEntity):
    def __init__(self, energy=350, *args, **kwargs) -> None:
        super().__init__(**kwargs)
        self.energy = energy
        self._is_siting = False
        self._is_runing = False
        self.max_energy = energy

    def shoot(self) -> Shoot | None:
        self.is_shooting = True
        self.shoot_position = self.direction
        if self.timer is None:
            self.set_timer(30)
            return Shoot(direction=self.direction, position_x=self.position_x, position_y=self.position_y + 20, player_shoot=True)
    
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