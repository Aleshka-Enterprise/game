from models.entity import BaseEntity


class Shoot(BaseEntity):
    def __init__(self, direction, position_x, position_y, player_shoot: bool, width=20, height=6, color=(0, 0, 250), speed=25) -> None:
        super().__init__(direction, position_x, position_y, width, height, color, speed)
        self.player_shoot = player_shoot
        self.speed = speed
    
    def move(self):
        return super().move()

