import pygame
from kink import inject


@inject
class GameState():

    def __init__(self, font):
        self.done = False
        self.font = font
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.screen_rect = pygame.display.get_surface().get_rect()

    def start(self):
        pass

    def update(self):
        pass

    def get_event(self, event):
        pass

    def draw(self, surf):
        pass
