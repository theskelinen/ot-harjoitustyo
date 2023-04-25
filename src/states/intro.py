import pygame
from .game_state import GameState


class Intro(GameState):

    def __init__(self):
        super().__init__()
        self.item1 = self.font.render("Tähän tulee intro", True, self.white)
        self.item2 = self.font.render(
            "...tai sitten outro :D", True, self.white)
        self.next_state = "Menu"

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.done = True

    def draw(self, surf):
        surf.fill(self.black)
        surf.blit(self.item1, (100, 100))
        surf.blit(self.item2, (100, 140))
