import pygame


class Renderer:
    def __init__(self, screen, level, assets, sword_icon, health_bar_dict, font, red, green):
        self._screen = screen
        self._level = level
        self._assets = assets
        self._sword_icon = sword_icon
        self.show_sword_icon = False
        self._font = font
        self._health_bar_dict = health_bar_dict
        self._red = red
        self._green = green

    def render(self):

        self._draw_background()
        self._draw_floor()

        self._draw_panel()

        self._draw_sprite()

        self._draw_mouse_icon()

        pygame.display.update()

    def _draw_mouse_icon(self):
        if self.show_sword_icon:
            self._screen.blit(self._sword_icon.image_scaled,
                              self._sword_icon.rect)

    def _draw_background(self):
        self._screen.blit(self._level.room_background, (0, 0))

    def _draw_floor(self):
        self._screen.blit(self._assets.floor, (0, 640))

    def _draw_panel(self):
        self._screen.blit(self._assets.panel, (0, 720))
        index = 0
        for sprite in self._level.sprites_list:
            if sprite.name == "Knight":
                self._draw_text(f"{sprite.name} HP: {sprite.hp}", 200, 730)
                health_bar = self._health_bar_dict[sprite.name]
                self._draw_health_bar(sprite.hp, health_bar, index)
            else:
                self._draw_text(
                    f"{sprite.name} HP: {sprite.hp}", 900, (730 + index * 50))
                health_bar = self._health_bar_dict[sprite.name]
                self._draw_health_bar(sprite.hp, health_bar, index)
                index += 1

    def _draw_text(self, text, x, y):
        img = self._font.render(text, True, self._red)
        self._screen.blit(img, (x, y))

    def _draw_health_bar(self, sprite_hp, health_bar, index):
        health_bar.current_hp = sprite_hp
        ratio = health_bar.current_hp / health_bar.max_hp
        pygame.draw.rect(self._screen, self._red,
                         (health_bar.pos_x, health_bar.pos_y + (index*50), 150, 15))
        pygame.draw.rect(self._screen, self._green, (health_bar.pos_x,
                         health_bar.pos_y + (index*50), 150 * ratio, 15))

    def _draw_sprite(self):
        self._level.sprites_list.draw(self._screen)
