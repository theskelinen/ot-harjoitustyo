import pygame

class GameLoop:
    def __init__(self, renderer):
        self._renderer = renderer

    def start(self):
        clock = pygame.time.Clock()
        fps = 60
        run = True
        while run:

            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self._render()

    pygame.quit()

    def _render(self):
        self._renderer.render()