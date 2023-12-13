import pygame


keys: dict[str, list[int]] = {
    'right': [pygame.K_RIGHT, pygame.K_d],
    'left': [pygame.K_LEFT, pygame.K_a],
    'dow': [pygame.K_DOWN, pygame.K_s],
    'jump': [pygame.K_SPACE, pygame.K_w],
    'run': [pygame.K_LSHIFT],
    'shoot': [pygame.K_z]
}