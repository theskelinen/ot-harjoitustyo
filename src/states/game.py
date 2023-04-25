import pygame
from .game_state import GameState
from game_files.level.level import Level
from game_files.ui.panel import Panel


class Game(GameState):

    def __init__(self):
        super().__init__()
        self.level = Level()
        self.panel = Panel(self.level.sprites)
        self.next_state = "Intro"

    def update(self):
        self.level.update()

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.level.level_data.clicked = True

    def draw(self, screen):
        self.level.draw(screen)
        self.panel.draw(screen)
