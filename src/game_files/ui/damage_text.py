import pygame


class DamageText(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.font.SysFont(
            "Verdana", 20).render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 40:
            self.kill()
