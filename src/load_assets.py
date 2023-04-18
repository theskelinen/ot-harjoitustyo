import pygame


class LoadAsset:
    def __init__(self):
        self.panel = self._load_panel()
        self.floor = self._load_floor()
        self.pointer = self._load_pointer()

    def _load_panel(self):
        panel = pygame.image.load("src/assets/Panel/panel.png").convert_alpha()
        panel = pygame.transform.scale(panel, (1280, 150))
        return panel

    def _load_floor(self):
        floor = pygame.image.load(
            "src/assets/Background/ground.png").convert_alpha()
        floor = pygame.transform.scale(floor, (1280, 80))
        return floor

    def _load_pointer(self):
        pointer = pygame.image.load(
            "src/assets/Others/sword.png").convert_alpha()
        # pointer = pygame.transform.scale(pointer, (80, 80))
        return pointer
