import pygame

class Renderer:
    def __init__(self, screen, level):
        self._screen = screen
        self._level = level

    def render(self):
        self._screen.blit(self._level.background, (0, 0))
        self._screen.blit(self._level.panel, (0, 720))
        self._screen.blit(self._level.floor, (0, 640))
        self._screen.blit(self._level.character.image_scaled, self._level.character.rect)

        pygame.display.update()