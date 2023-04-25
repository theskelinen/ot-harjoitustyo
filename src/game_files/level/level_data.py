import pygame


class LevelData:
    def __init__(self):
        self.current_fighter = 1
        self.total_fighters = 0
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.target = None
        self.clicked = False
        self.damage_text_group = pygame.sprite.Group()
