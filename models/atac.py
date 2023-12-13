from models.entity import BaseEntity, LivingEntity


class Atac(BaseEntity):
    def __init__(self, direction, position_x, position_y, width=20, height=6, color=(0, 0, 250), speed=25) -> None:
        super().__init__(direction, position_x, position_y, width, height, color, speed)

class Shoot(Atac):
    def __init__(self, direction, position_x, position_y, width=20, height=6, color=(0, 0, 250), speed=25, damage=10) -> None:
        super().__init__(direction, position_x, position_y, width, height, color, speed)
        self.speed = speed
        self.damage = damage
    
    def move(self):
        return super().move()
    
    def check_collision(self, entity: LivingEntity) -> bool:
        if (entity.position_x < self.position_x + self.width and
            entity.position_x + entity.width > self.position_x and
            entity.position_y < self.position_y + self.height and
            entity.position_y + entity.height > self.position_y):
            entity.set_damage(self.damage)
            return True
        return False

