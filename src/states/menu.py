import pygame
from .game_state import GameState


class Menu(GameState):

    def __init__(self):
        super().__init__()
        self.item1 = self.font.render(
            "Tähän tulee menu screeni", True, self.white)
        self.item2 = self.font.render(
            "Paina a-näppäintä jatkaaksesi", True, self.white)
        self.next_state = "Splash"

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.done = True

    def draw(self, surf):
        surf.fill(self.black)
        surf.blit(self.item1, (100, 100))
        surf.blit(self.item2, (100, 140))
