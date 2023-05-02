import pygame
from kink import inject
from .game_state import GameState


@inject
class Game(GameState):

    def __init__(self, level, panel):
        super().__init__()
        self.level = level
        self.panel = panel
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
