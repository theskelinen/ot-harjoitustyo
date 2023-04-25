import pygame


class GameState(object):

    def __init__(self):
        self.done = False
        self.font = pygame.font.SysFont("Verdana", 20)
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
