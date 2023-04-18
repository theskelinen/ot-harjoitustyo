import pygame


class SwordIcon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            "src/assets/Others/sword.png").convert_alpha()
        self.image_scaled = pygame.transform.scale(
            self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
