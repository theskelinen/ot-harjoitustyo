import pygame
from .game_state import GameState


class Menu(GameState):

    """
    Pelitila, joka vastaa menu-valikosta

    """

    def __init__(self):
        """
        Parametrit:
                    item_1: str
                        menu teksti
                    item_2: str
                        käyttäjäohje syötteelle
                    next_state: str
                        seuraavan tilan nimi
        """

        super().__init__()
        self.item_1 = self.font.render(
            "Menu", True, self.white)
        self.item_2 = self.font.render(
            "Press m to continue in game", True, self.white)
        self.next_state = "Game"

    def get_event(self, event):
        """
        Metodi vastaa pelitapahtumista ja käyttäjän syötteistä

        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                self.done = True

    def draw(self, screen):
        """
        Metodi vastaa tilan titlen piirtämisestä

        """

        screen.fill(self.black)
        screen.blit(self.item_1, (100, 100))
        screen.blit(self.item_2, (100, 140))
