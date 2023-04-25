import pygame
from game_files.ui.healthbar import HealthBar


class Panel:
    def __init__(self, sprites):
        self.sprites = sprites
        self.font = pygame.font.SysFont("Arial", 20)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.panel = self._load_panel()
        self._health_bar_dict = self._load_health_bar()

    def _load_panel(self):
        panel = pygame.image.load("src/assets/Panel/panel.png").convert_alpha()
        panel = pygame.transform.scale(panel, (1280, 150))
        return panel

    def _load_health_bar(self):
        health_bar_dict = {}
        for sprite in self.sprites:
            if sprite.name == "Knight":
                knight_hb = HealthBar(200, sprite.current_hp, sprite.max_hp)
                health_bar_dict[sprite.name] = knight_hb
            if sprite.name == "Imp_Axe":
                imp_axe_hb = HealthBar(
                    900, sprite.current_hp, sprite.max_hp)
                health_bar_dict[sprite.name] = imp_axe_hb
            if sprite.name == "Death_Bringer":
                death_bringer_hb = HealthBar(
                    900, sprite.current_hp, sprite.max_hp)
                health_bar_dict[sprite.name] = death_bringer_hb

        return health_bar_dict

    def draw(self, screen):
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
        img = self.font.render(text, True, self.red)
        screen.blit(img, (x, y))

    def _draw_health_bar(self, screen, sprite_hp, health_bar, index):
        health_bar.current_hp = sprite_hp
        ratio = health_bar.current_hp / health_bar.max_hp
        pygame.draw.rect(screen, self.red,
                         (health_bar.pos_x, health_bar.pos_y + (index*50), 150, 15))
        pygame.draw.rect(screen, self.green, (health_bar.pos_x,
                                              health_bar.pos_y + (index*50), 150 * ratio, 15))
