import pygame


class GameState():

    """
    Luokka toimii pääluokkana eri pelitiloille.

    """

    def __init__(self):
        """
        Parametrit:
                    done: onko tila valmis
                    font: fontin luominen
                    white: valkoinen väri
                    black: musta väri
                    screen_rect: näytön tason rect objektin tallentaminen
        """

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

    def draw(self, screen):
        pass
