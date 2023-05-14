import pygame
from .game_state import GameState


class Intro(GameState):

    """
    Pelin intro tila

    """

    def __init__(self):
        """
        Parametrit:
                    title_1: str
                        intro teksti
                    title_2: str
                        käyttäjäohje syötteelle
                    next_state: str
                        seuraavan tilan nimi
        """

        super().__init__()
        self.title_1 = self.font.render(
            "Welcome to Luolasto", True, self.white)
        self.title_2 = self.font.render(
            "Press a to start game", True, self.white)
        self.next_state = "Splash"

    def get_event(self, event):
        """
        Metodi vastaa pelitapahtumista ja käyttäjän syötteistä

        """

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.done = True
                    self.title_update()

    def title_update(self):
        """
        Metodi vastaa tilan titlen päivittämisestä

        """

        self.title_1 = self.font.render("Level Completed!", True, self.white)
        self.title_2 = self.font.render(
            "Press a to proceed", True, self.white)

    def draw(self, screen):
        """
        Metodi vastaa tilan titlen piirtämisestä

        """

        screen.fill(self.black)
        screen.blit(self.title_1, (100, 100))
        screen.blit(self.title_2, (100, 140))
