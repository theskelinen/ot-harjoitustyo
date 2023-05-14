import pygame
from kink import inject


@inject
class Panel:

    """
    Näytön info-paneelista vastaava luokka

    Args:
        sprites: hahmot
        font: fontti
        hb_dict: sanakirja elämämittareista
        panel_img: paneelin kuva
    """

    def __init__(self, sprites, font, hb_dict, panel_img):
        self.sprites = sprites
        self.font = font
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.panel = panel_img
        self._health_bar_dict = hb_dict

    def draw(self, screen):
        """
        Paneelin piirtämisestä vastaava metodi

        """

        screen.blit(self.panel, (0, 720))
        index = 0
        for sprite in self.sprites:
            if sprite.name == "Knight":
                self._draw_text(
                    screen, f"{sprite.name} HP: {sprite.current_hp}", 200, 730)
                health_bar = self._health_bar_dict[sprite.name]
                self._draw_health_bar(
                    screen, sprite.current_hp, health_bar, index)
            else:
                self._draw_text(
                    screen, f"{sprite.name} HP: {sprite.current_hp}", 900, (730 + index * 50))
                health_bar = self._health_bar_dict[sprite.name]
                self._draw_health_bar(
                    screen, sprite.current_hp, health_bar, index)
                index += 1

    def _draw_text(self, screen, text, x, y):
        """
        Paneelin tekstin piirtämisestä vastaava metodi

        """

        img = self.font.render(text, True, self.red)
        screen.blit(img, (x, y))

    def _draw_health_bar(self, screen, sprite_hp, health_bar, index):
        """
        Paneelin elämämittarin piirtämisestä vastaava metodi

        """

        health_bar.current_hp = sprite_hp
        ratio = health_bar.current_hp / health_bar.max_hp
        pygame.draw.rect(screen, self.red,
                         (health_bar.pos_x, health_bar.pos_y + (index*50), 150, 15))
        pygame.draw.rect(screen, self.green, (health_bar.pos_x,
                                              health_bar.pos_y + (index*50), 150 * ratio, 15))
