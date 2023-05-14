import pygame


class DamageText(pygame.sprite.Sprite):

    """
    Vahinkotekstin luokka

    Args:
        pos_x: tekstin x-koordinaatti
        pos_y: tekstin y-koordinaatti
        damage: vahingon määrä
        colour: tekstin väri
    """

    def __init__(self, pos_x, pos_y, damage, colour):
        """
        Parametrit:
                    damage: vahingon määrä
                    image: tekstin kuva
                    rect: tekstin sijainti
                    rect.center: tekstin asemointi
                    counter: kuinka pitkään teksti on näkyvillä
        """

        pygame.sprite.Sprite.__init__(self)
        self.damage = damage
        self.image = pygame.font.SysFont(
            "Verdana", 20).render(self.damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 40:
            self.kill()
