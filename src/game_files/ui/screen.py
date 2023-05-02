import pygame


class Screen:
    def __init__(self):
        self.bottom_panel = 150
        self.screen_width = 1280
        self.screen_height = 720 + self.bottom_panel
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
