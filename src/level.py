import pygame
from sprites.character import Character

class Level:
    def __init__(self):
        self.character = Character(200, 580, "Knight", 3, 10)
        self.panel = None
        self.floor = None
        self.background = None

        self._load_background()
        self._load_floor()
        self._load_panel()

    def _load_background(self):
        background = pygame.image.load("src/assets/Background/background.png").convert_alpha()
        background = pygame.transform.scale(background, (1280, 640))
        self.background = background

    def _load_floor(self):
        floor = pygame.image.load("src/assets/Background/ground.png").convert_alpha()
        floor = pygame.transform.scale(floor, (1280, 80))
        self.floor = floor

    def _load_panel(self):
        panel = pygame.image.load("src/assets/Panel/panel.png").convert_alpha()
        panel = pygame.transform.scale(panel, (1280, 150))
        self.panel = panel