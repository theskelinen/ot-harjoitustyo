import pygame

class Character():
    def __init__(self, x, y, name, max_hp, strength):

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.image = pygame.image.load(f"src/assets/{self.name}/ready_1.png")
        self.image_scaled = pygame.transform.scale(self.image, (250, 240))
        self.rect = self.image_scaled.get_rect()
        self.rect.center = (x, y)